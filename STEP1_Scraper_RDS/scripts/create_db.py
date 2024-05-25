def create_tables(conn, cursor):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS jobs (
            job_id BIGINT PRIMARY KEY,
            scraped TINYINT NOT NULL DEFAULT 0,
            company_id INT,
            work_type VARCHAR(255),
            formatted_work_type VARCHAR(255),
            location VARCHAR(255),
            job_posting_url VARCHAR(255),
            applies INT,
            original_listed_time VARCHAR(255),
            remote_allowed TINYINT,
            application_url VARCHAR(255),
            application_type VARCHAR(255),
            expiry VARCHAR(255),
            inferred_benefits VARCHAR(255),
            closed_time VARCHAR(255),
            formatted_experience_level VARCHAR(255),
            years_experience INT,
            description TEXT,
            title VARCHAR(255),
            skills_desc TEXT,
            views INT,
            job_region VARCHAR(255),
            listed_time VARCHAR(255),
            degree VARCHAR(255),
            posting_domain VARCHAR(255),
            sponsored TINYINT
        );
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS skills (
            skill_abr VARCHAR(255) PRIMARY KEY,
            skill_name TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS job_skills (
            job_id BIGINT,
            skill_abr VARCHAR(255),
            FOREIGN KEY (job_id) REFERENCES jobs(job_id),
            FOREIGN KEY (skill_abr) REFERENCES skills(skill_abr),
            PRIMARY KEY (job_id, skill_abr)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS industries (
            industry_id INT AUTO_INCREMENT PRIMARY KEY,
            industry_name TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS job_industries (
            job_id BIGINT,
            industry_id INT,
            FOREIGN KEY (job_id) REFERENCES jobs(job_id),
            FOREIGN KEY (industry_id) REFERENCES industries(industry_id),
            PRIMARY KEY (job_id, industry_id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS salaries (
            salary_id INT AUTO_INCREMENT PRIMARY KEY,
            job_id BIGINT NOT NULL,
            max_salary FLOAT,
            med_salary FLOAT,
            min_salary FLOAT,
            pay_period VARCHAR(255),
            currency VARCHAR(45),
            compensation_type VARCHAR(255),
            FOREIGN KEY (job_id) REFERENCES jobs(job_id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS benefits (
            job_id BIGINT NOT NULL,
            inferred TINYINT NOT NULL,
            type VARCHAR(255) NOT NULL,
            FOREIGN KEY (job_id) REFERENCES jobs(job_id),
            PRIMARY KEY (job_id, type)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS companies (
            company_id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            description TEXT,
            company_size INT,
            state VARCHAR(255),
            country VARCHAR(255),
            city VARCHAR(255),
            zip_code VARCHAR(20),
            address VARCHAR(255),
            url VARCHAR(255)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employee_counts (
            company_id INT NOT NULL,
            employee_count INT,
            follower_count INT,
            time_recorded INT NOT NULL,
            FOREIGN KEY (company_id) REFERENCES companies(company_id),
            PRIMARY KEY (company_id, employee_count)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS company_specialities (
            company_id INT NOT NULL,
            speciality INT NOT NULL,
            FOREIGN KEY (company_id) REFERENCES companies(company_id),
            PRIMARY KEY (company_id, speciality)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS company_industries (
            company_id INT NOT NULL,
            industry INT NOT NULL,
            FOREIGN KEY (company_id) REFERENCES companies(company_id),
            PRIMARY KEY (company_id, industry)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ner_skills (
            job_id BIGINT PRIMARY KEY,
            ner_skills TEXT
        )
    ''')

    conn.commit()
    return True
