import time
import spacy
from spacy.matcher import PhraseMatcher
from skillNer.general_params import SKILL_DB
from skillNer.skill_extractor_class import SkillExtractor

# Init skill extractor for ner_skills
nlp = spacy.load("en_core_web_lg")
skill_extractor = SkillExtractor(nlp, SKILL_DB, PhraseMatcher)


# Insert job detail into the database
def insert_data(data, conn, cursor):
    allowed_tables = {'jobs', 'benefits', 'industries', 'skills', 'salaries', 'companies', 'employee_counts', 'company_industries', 'company_specialities'}

    for job_id, job_info in data.items():
        if 'error' in job_info:
            cursor.execute("UPDATE jobs SET scraped = -1 WHERE job_id = %s", (job_id,))
            continue

        # Handle jobs data separately due to its unique structure
        if 'jobs' in job_info:
            jobs_data = job_info['jobs']
            company_id = jobs_data.get('company_id')
            column_names = list(jobs_data.keys())
            values = tuple(jobs_data[column] for column in column_names)
            set_clause = ", ".join([f"{column} = %s" for column in column_names])
            set_clause += ", scraped = %s"
            values_for_update = values + (round(time.time()),)
            query = f"UPDATE jobs SET {set_clause} WHERE job_id = %s"
            cursor.execute(query, values_for_update + (job_id,))

            # Extract skills from job description and put them into the ner_skills table
            description = jobs_data.get('description')
            if description:
                skill_extractor = SkillExtractor(nlp, SKILL_DB, PhraseMatcher)
                annotations = skill_extractor.annotate(description)
                doc_node_values = [match['doc_node_value'] for match in annotations['results']['full_matches']]
                doc_node_values_string = ", ".join(doc_node_values)
                insert_query = '''
                    INSERT INTO ner_skills (job_id, ner_skills) VALUES (%s, %s) ON DUPLICATE KEY UPDATE ner_skills=VALUES(ner_skills);
                    '''
                # Execute the insert query
                cursor.execute(insert_query, (job_id, doc_node_values_string))
        
        # Iterate over other specified tables if specified data exists
        for table_name in job_info:
            if table_name in allowed_tables and job_info[table_name]:
                table_data = job_info[table_name]

                if table_name == 'companies' and company_id:
                    column_names = list(table_data.keys())
                    values = tuple(table_data[column] for column in column_names)
                    query = f"INSERT INTO companies (company_id, {', '.join(column_names)}) VALUES (%s, {', '.join(['%s'] * len(values))}) ON DUPLICATE KEY UPDATE " + ", ".join([f"{col}=VALUES({col})" for col in column_names])
                    cursor.execute(query, (company_id,) + values)

                elif table_name == 'benefits':
                    for benefit in table_data.get('listed_benefits', []):
                        cursor.execute(
                            f'INSERT INTO benefits (job_id, type) VALUES (%s, %s) ON DUPLICATE KEY UPDATE type=VALUES(type)',
                            (job_id, benefit))
                
                elif table_name == 'salaries':
                    for salary_detail_list in table_data.values():
                        for salary_detail in salary_detail_list:
                            cursor.execute(
                                'INSERT INTO salaries (job_id, max_salary, med_salary, min_salary, pay_period, currency, compensation_type) VALUES (%s, %s, %s, %s, %s, %s, %s)',
                                (job_id, salary_detail.get('maxSalary'), salary_detail.get('medianSalary'), salary_detail.get('minSalary'),
                                salary_detail.get('payPeriod'), salary_detail.get('currencyCode'), salary_detail.get('compensationType')))
                    
                elif table_name == 'industries':
                    for industry_id, industry_name in zip(table_data.get('industry_ids', []), table_data.get('industry_names', [])):
                        cursor.execute(
                            'INSERT INTO industries (industry_id, industry_name) VALUES (%s, %s) ON DUPLICATE KEY UPDATE industry_name=VALUES(industry_name)',
                            (industry_id, industry_name))
                        cursor.execute('INSERT IGNORE INTO job_industries (job_id, industry_id) VALUES (%s, %s)',
                                       (job_id, industry_id))

                elif table_name == 'skills':
                    for skill_abr, skill_name in zip(table_data.get('skill_abrs', []), table_data.get('skill_names', [])):
                        cursor.execute(
                            'INSERT INTO skills (skill_abr, skill_name) VALUES (%s, %s) ON DUPLICATE KEY UPDATE skill_name=VALUES(skill_name)',
                            (skill_abr, skill_name))
                        cursor.execute('INSERT IGNORE INTO job_skills (job_id, skill_abr) VALUES (%s, %s)',
                                       (job_id, skill_abr))

                elif table_name == 'employee_counts' and company_id:
                    query = f"INSERT INTO employee_counts (company_id, employee_count, follower_count, time_recorded) VALUES (%s, %s, %s, %s) ON DUPLICATE KEY UPDATE employee_count=VALUES(employee_count), follower_count=VALUES(follower_count), time_recorded=VALUES(time_recorded)"
                    cursor.execute(query, 
                                   (company_id, 
                                    table_data['employee_count'], 
                                    table_data['follower_count'], 
                                    round(time.time())))

                elif table_name == 'company_industries' and company_id:
                    for industry in table_data.get('industries', []):
                        cursor.execute('INSERT IGNORE INTO company_industries (company_id, industry) VALUES (%s, %s)', (company_id, industry))

                elif table_name == 'company_specialities' and company_id:
                    for speciality in table_data.get('specialities', []):
                        cursor.execute('INSERT IGNORE INTO company_specialities (company_id, speciality) VALUES (%s, %s)', (company_id, speciality))
        
        # Commit changes to the database
        conn.commit()
    return True


# Insert job overview into the database
def insert_job_postings(job_ids, conn, cursor):
    for job_id, info in job_ids.items():
        
        # Convert boolean True/False to integer 1/0
        sponsored_int = 1 if info['sponsored'] else 0
        
        # Prepare the SQL statement
        sql = ('INSERT INTO jobs (job_id, title, sponsored) VALUES (%s, %s, %s) '
               'ON DUPLICATE KEY UPDATE title = VALUES(title), sponsored = VALUES(sponsored)')

        # Add job posting
        cursor.execute(sql, (job_id, info['title'], sponsored_int))
    
    # Commit change to the database
    conn.commit()
    print("Jobs insertion/update completed.")
    
    return True
