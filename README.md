# Understanding the Mismatch in Job Market Skills

## Project Overview

This project delves into the dynamics of today's job market, driven by rapid technological advancements and changing economic conditions. We aim to explore several pressing questions: What skills are currently necessary for employment? Why is it easier for some individuals to find jobs than others? Is there a mismatch between the skills that job seekers possess and what industries require?

The modern job market landscape raises important questions about employment qualifications and accessibility. This research specifically targets the discrepancies between the skills held by job seekers and those demanded by industries. To address this, we will utilize Named Entity Recognition (NER) to extract the required skills from job descriptions systematically. Furthermore, we plan to develop a system that enables job seekers to find matching jobs based on their skills.

By investigating these mismatches and implementing these technological solutions, our goal is to provide actionable insights that will improve the employability of job seekers and ensure educational initiatives are more aligned with market needs. Through understanding the underlying causes of these discrepancies, we aim to devise strategies that address these issues, facilitating a better match between job seekers and industry requirements.

## Justification for Scalable Computing Methods

### Volume of Data

The digital transformation of recruitment processes has positioned platforms like LinkedIn at the forefront of data-driven hiring. LinkedIn, utilized by 97% of HR and staffing professionals, is not only a tool for recruitment but also a rich repository for job market analytics. With over 14 million open job listings, LinkedIn offers a macroscopic view of employment opportunities and skills demand across various industries. The magnitude of this data pool—ranging from job descriptions to applicant skills and hiring outcomes—requires robust scalable computing solutions to manage, process, and extract meaningful insights. The employment of advanced data architectures and scalable processing capabilities is imperative to handle this vast amount of data efficiently and effectively, allowing for sophisticated analysis that can adapt to the constantly evolving job market landscape.

### Complexity and Real-time Processing

The job market is characterized by its dynamic and ever-changing nature, where skill demands and job opportunities fluctuate rapidly in response to technological and economic shifts. To capture and analyze these real-time data streams, scalable computing employs advanced analytics that operate on large-scale data platforms, enabling real-time processing and analysis. This capability is essential for generating timely, actionable insights that can influence critical decisions in workforce development and recruitment strategies. By leveraging technologies such as stream processing and real-time data analytics frameworks, the project can provide stakeholders with up-to-the-minute insights into job market trends, helping them make informed decisions quickly.

### Distributed Computing

The challenge of managing and analyzing large-scale, multi-dimensional datasets is met with distributed computing technologies, which distribute data processing tasks across multiple computing resources. This approach not only accelerates the data processing speeds but also significantly enhances the capability to conduct deep, complex analyses on large datasets. Utilizing distributed systems like Hadoop or Spark allows for scalable and efficient processing of big data, enabling the exploration of complex patterns and relationships within the job market. Such technologies are crucial for dissecting the intricate web of variables that influence job trends, from regional economic conditions to emerging industry skills, providing a comprehensive analytical perspective that is both scalable and detailed.

## Scalable Computing Methods Employed

### EC2 and Local Scraper

Initially, the plan was to use Amazon EC2 (Elastic Compute Cloud) for its robust, always-online capabilities ideal for running a web scraper continuously. However, due to the risk of IP blocking by platforms such as LinkedIn, which has sophisticated systems to detect and prevent automated data extraction, we opted for a local scraping setup. Running the scraper locally minimizes the risk of detection and service interruption, ensuring a steady and consistent data flow. This hybrid approach allows for flexibility in data collection, maintaining the integrity and continuity of the scraping process while adhering to platform limitations and data usage policies.

### RDS and Data Storage

Once data is collected, it is stored in Amazon RDS (Relational Database Service). RDS provides a scalable, cloud-based database environment that supports SQL (Structured Query Language), making it ideal for handling and querying large datasets efficiently. This setup facilitates not only robust data management but also enhances security and recovery features, which are critical in maintaining data integrity and availability. The scalability of RDS ensures that as the volume of data grows, the database can scale to meet increased demands without compromising performance, crucial for the ongoing analytical needs of this project.

### S3 and EMR Spark Cluster

For data analysis, the collected data in RDA will be exported periodically, using the snapshot function, in Parquet format (an optimized columnar storage format) to Amazon S3 (Simple Storage Service). S3 offers high scalability, data availability, and security, making it suitable for storing large volumes of data. Subsequent analysis is performed using Amazon EMR (Elastic MapReduce) with Apache Spark. EMR, a managed cluster platform, simplifies running big data frameworks like Spark and Hadoop to process vast amounts of data efficiently. Using Spark on EMR provides powerful processing capabilities necessary to handle complex analyses, including data aggregation, machine learning models, and real-time analytics, which are essential for developing the job recommendation system envisioned in this project.

### Future Considerations: IP Rotation Strategy

To enhance future data collection efforts and mitigate the risk of IP blocking, an IP rotation strategy is under consideration. This approach would involve dynamically changing the IP addresses used by our scrapers to avoid detection and blacklisting by job platforms. Implementing this strategy would allow us to move our scraping operations back to EC2, leveraging its continuous operation capabilities and thus ensuring more robust, uninterrupted data collection. This strategic shift would not only stabilize data acquisition but also expand our capacity to capture a broader dataset, enhancing the overall quality and scope of our market analysis.

## Repository Guide and Project Walkthrough

### Overview

This project is structured into multiple stages to efficiently handle data scraping, storage, analysis, and the development of a job recommendation system. Below, you will find detailed instructions on how to navigate and utilize the components and files within this repository.

### Folder Structure

1. **[Step1_Scraper_RDS](https://github.com/macs30123-s24/final-project-42/tree/main/STEP1_Scraper_RDS)**
2. **[STEP2&3_Skill_LDA_Analysis&Job_Recommender](https://github.com/macs30123-s24/final-project-42/tree/main/STEP2%263_Skill_LDA_Analysis%26Job_Recommender)**

### Step 1: Scraper and RDS

#### Location

`Step1_Scraper_RDS` folder

#### Contents

- `main.ipynb`: Jupyter notebook containing the code to run the scraper and update the RDS database.
- `some SkillNER files`: Required files for Named Entity Recognition (NER) to extract skills from job descriptions.
- `template for logins.csv`: File to input login credentials for platforms to be scraped.

#### Instructions

1. **Prepare the Environment**:
   - Navigate to the `Step1_Scraper_RDS` folder.
   - Ensure that you have follow the guidance on [Github - SkillNER by AnasAito](https://github.com/AnasAito/SkillNER) to install it correctly. This package is crucial for processing and extracting skills from job descriptions using NER.
2. **Configure Credentials**:
   - Open `template for logins.csv` and add your login credentials for Linkedin. It is recommended to use a test account, rather than personal credentials, to avoid any potential security or privacy issues.
3. **Run the Notebook**:
   - Open `main.ipynb` in a Jupyter environment.
   - Execute the cells in the notebook to start the scraping process and update the RDS database with the collected data.
4. **Export Data to S3**:
   - Once the data is updated in RDS, use the AWS Management Console to export a snapshot of the RDS database to an S3 bucket in Parquet format. This format is optimized for high-performance computing environments.

### Step 2 & 3: Skill Analysis and Job Recommender

#### Location

`STEP2&3_Skill_LDA_Analysis&Job_Recommender` folder

#### Contents

- `2&3_local_setup.ipynb`: Jupyter notebook for setting up the EMR cluster.
- `2&3_main.ipynb`: Main notebook to run on the AWS EMR Spark cluster for LDA analysis and job recommendation system.
- `ner_skills_sample.parquet & stopwords`: Data files used in the main notebook, also stored in S3 bucket.

#### Instructions

1. **EMR Cluster Setup**:
   - Follow the instructions in `2&3_local_setup.ipynb` to configure and launch your AWS EMR cluster appropriately for the project's needs.
2. **LDA Analysis and Recommender System**:
   - Open `2&3_main.ipynb` on your AWS EMR Spark cluster.
   - This notebook contains the logic for performing Latent Dirichlet Allocation (LDA) analysis on the skills extracted from job descriptions.
   - It also includes the implementation of a simple job recommender system that matches job seekers with jobs based on the skills they input.
3. **Data Management**:
   - Ensure that all required data files are correctly placed in S3 and accessible from the EMR cluster. The main notebook should be able to read these files without issues.

## Analysis and Findings

### Integration of Soft and Technical Skills

Across nearly all topics, there's a clear intersection between soft skills (like communication and management) and technical skills (such as data analysis, software development, and medical expertise). This blending underscores a labor market that increasingly values professionals who are not only technically proficient but also capable of leading teams, managing projects, and communicating effectively. Businesses and organizations are seeking individuals who can bridge the gap between technical execution and strategic management.

### Sector-Specific Trends

The analysis also reveals distinct sector-specific trends:

- **Technology and IT**: There's an ongoing demand for skills in software development, cybersecurity, and data management, reflecting the sector's rapid growth and its critical role in digital transformation across industries.
- **Healthcare**: Both clinical (nurses, patient care) and administrative (healthcare benefits management) skills are highlighted, pointing to a healthcare industry that is expanding in response to global health challenges and demographic changes. The emphasis on certifications and licensure indicates a highly regulated environment where continuing education and compliance are crucial.
- **Construction and Engineering**: Skills related to project management and quality assurance in construction show the need for professionals who can oversee complex projects from conception through completion, ensuring they meet regulatory and safety standards.

### Technology Integration

Lastly, the frequent mention of cloud technologies, data management, and cybersecurity across various topics highlights the ongoing shift towards an economy that is deeply integrated with technology. Companies and individuals alike need to prioritize the adoption and proficient use of these technologies to remain competitive and efficient.

These broader insights provide a multi-dimensional view of the labor market, helping stakeholders from across sectors to make informed decisions about career development, hiring, and policy-making.

## Application: Job Recommender

This application is designed to help job seekers find positions that closely match their skills. Users provide a list of their skills, and the system leverages a recommender algorithm to find and suggest the top five job postings that best fit their qualifications.

### User Input

- **Input Format**: Users input their skills as a comma-separated list. For example, "data analysis, Python, business analytics."
- **Processing**: The input is processed to match the format expected by the underlying machine learning model, which is designed to parse and understand natural language inputs related to job skills.

### Backend Processing

- **Skill Extraction**: The application utilizes Named Entity Recognition (NER) to extract relevant skills from the user's input. This ensures that even if the input is slightly varied or contains synonyms, the system can accurately interpret and map the skills.
- **Skill Matching**: Using a pre-calculated matrix of job skills (extracted and transformed into a TF-IDF (Term Frequency-Inverse Document Frequency) matrix from a dataset of job postings), the application computes the cosine similarity between the user's skills and each job's skill requirements.
- **Recommendation Algorithm**: The system applies a cosine similarity function to determine how closely the user's skills align with the skills required by various job postings. The jobs are then ranked based on this similarity score.

### Output

- **Top Job Recommendations**: The top five jobs, ranked by their relevance to the user's skills, are displayed. This output includes the job ID and a brief description of the job skills required, providing the user with clear and actionable information.

### Integration with Job Databases

The application can be integrated with real-time job databases to continuously update the job listings and ensure that the recommendations are up-to-date and relevant. This dynamic linkage allows the system to adapt to the ever-changing job market, providing current and prospective job seekers with valuable job matching opportunities.

## Credits and Acknowledgments

### Data & Code Source

The sample data used in this project was sourced from the LinkedIn Job Postings dataset available on Kaggle. Special thanks to the dataset provider and the creator of the repository which can be found here:

- **Dataset**: [LinkedIn Job Postings on Kaggle](https://www.kaggle.com/datasets/arshkon/linkedin-job-postings/data)
- **Repository**: [GitHub - LinkedIn Job Scraper by ArshKA](https://github.com/ArshKA/LinkedIn-Job-Scraper)

In the **Step1_Scraper_RDS** folder, the original scraping code by **ArshKA** was significantly modified to integrate with AWS RDS and enhance its functionality by incorporating Skill NER (Named Entity Recognition). These adaptations were crucial for tailoring the scraper to the specific needs of this project, enabling more effective data collection and analysis.

### Educational Support

Profound gratitude is extended to **Professor Clindaniel** and the teaching assistants (**Won Je Yun** and **Adam Wu**) who have provided continuous support throughout this project and the entire quarter. Their expert guidance, valuable instructions, and provided code notebooks have been essential not only in the successful completion of this project but also in enriching the overall learning experience in this course.

### Final Thoughts

The insights and skills gained from this project are attributed to the collaborative efforts of many, including the broader academic and online communities (special thanks to Reddit and Stack Overflow!). I'm deeply thankful to all who contributed directly or indirectly to my learning and project execution.
