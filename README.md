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

## Repo Guidance

TBC

## Analysis, Findings and Applications

TBC

## Credit

TBC
