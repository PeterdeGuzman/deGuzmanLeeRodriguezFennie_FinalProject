# Mystery Book Query System with AWS and Google Gemini API Integration 

## Authors: Peter de Guzman, Ilseop Lee, Eric Ortega Rodriguez, and Zachary Fennie

## Status Badges
[![IaC](https://github.com/PeterdeGuzman/deGuzmanLeeRodriguezFennie_FinalProject/actions/workflows/IaC.yml/badge.svg)](https://github.com/PeterdeGuzman/deGuzmanLeeRodriguezFennie_FinalProject/actions/workflows/IaC.yml)
[![Install Required Dependencies](https://github.com/PeterdeGuzman/deGuzmanLeeRodriguezFennie_FinalProject/actions/workflows/install.yml/badge.svg)](https://github.com/PeterdeGuzman/deGuzmanLeeRodriguezFennie_FinalProject/actions/workflows/install.yml)
[![Format Code in Repository](https://github.com/PeterdeGuzman/deGuzmanLeeRodriguezFennie_FinalProject/actions/workflows/format.yml/badge.svg)](https://github.com/PeterdeGuzman/deGuzmanLeeRodriguezFennie_FinalProject/actions/workflows/format.yml)
[![Lint Code in Repository](https://github.com/PeterdeGuzman/deGuzmanLeeRodriguezFennie_FinalProject/actions/workflows/lint.yml/badge.svg)](https://github.com/PeterdeGuzman/deGuzmanLeeRodriguezFennie_FinalProject/actions/workflows/lint.yml)
[![Test Code in Repository](https://github.com/PeterdeGuzman/deGuzmanLeeRodriguezFennie_FinalProject/actions/workflows/test.yml/badge.svg)](https://github.com/PeterdeGuzman/deGuzmanLeeRodriguezFennie_FinalProject/actions/workflows/test.yml)

## Our project developed a microservice that interfaces with a data pipeline, built using Python or Rust and containerized with a Distroless Docker image. The microservice includes logging functionality and is capable of handling 10,000 requests per second, with a load test verifying its performance. For the data engineering aspect, we utilized libraries such as Spark, Pandas, SQL, and a vector database. We implemented Infrastructure as Code (IaC) using tools like AWS CloudFormation, AWS SAM, AWS CDK, or the Serverless Framework to manage the infrastructure. The project also includes a CI/CD pipeline for seamless integration and delivery. Our repository contains a comprehensive README.md, an architectural diagram, and proper GitHub/GitLab configurations to ensure the project is fully reproducible. Additionally, we performed a quantitative assessment of the system's reliability and stability, analyzing performance metrics like latency at different request rates. The project is accompanied by a demo video that showcases the application, load test, and system performance. Each team member also submitted a reflection report, including a peer evaluation and feedback session for improving team collaboration.

#### Demo Video (Click the image to view the YouTube video)


### Project Diagram 
<img width="960" alt="Screenshot 2024-12-02 at 6 47 18 PM" src="https://github.com/user-attachments/assets/c8f60fc3-5eb7-4d2a-bc2a-eff656597d58">

### Data - Goodreads.com Mystery, Thriller & Crime Genre Dataset
Our dataset, created by Mengting Wan, was collected in late 2017 from Goodreads.com. It specifically focuses on users' public shelves, which are accessible to everyone on the web without requiring a login. The dataset includes anonymized User IDs and Review IDs to protect privacy. Specifically, the data we used was the Mystery, Thriller & Crime genre, containing data on 219,235 books, 24,799,896 interactions, and 1,849,236 detailed reviews. This rich dataset is used to analyze user behavior, book preferences, and interactions within the genre, providing valuable insights for recommendations and data-driven decision-making in our microservice. The data can be accessed via Menting Wan's repository at https://github.com/MengtingWan/goodreads.

### ETL Pipeline

Two Python scripts are used to orchestrate the Extract-Transform-Load pipeline. `extract.py` is used to parse the JSON files downloaded from the GitHub repository into CSV files. Once the mystery books and authors datasets are both in CSV format, a left join is performed to integrate author names, ratings, and other information into the mystery books dataset and relevant variables are selected for analysis. 

The `load.py` script contains multiple functions to facilitate data loading and table management in AWS DynamoDB. The `create_table()` function creates a DynamoDB table with "book_id" as the partition key. The next function `load_csv_to_dynamodb()` loads the merged book-author data from a CSV into the DynamoDB table. This is done through batch processing to account for the large volume of books in the dataset. 

### DynamoDB Table Items Summary
![DynamoDBScreenshot.png](deGuzmanLeeRodriguezFennie_FinalProject/DynamoDBscreenshot.png)

### Core Files of the Repo:
* `Dockerfile`
* `mylib`
    - `extract.py`
    - `gemini.py`
    - `load.py`
    - `query.py`
    - `test_app.py`
* `static`
    - `style.css`
* `template`
    - `homepage.html`
    - `project.html`
    - `result.html`
* `app.py`
* `LICENSE`
* `load_test.py`
* CI/CD pipeline
* `Makefile`
* `requirements.txt`
* `README.md`

### Infrastructure as Code (IaC)

To implement Infrastructure as Code, this project has a `IaC.yml` file which is configured to run through GitHub Actions. By following the commands in order, you can see that this automated redeployment works through multiple steps. The process begins by checking out the code and authenticating with AWS Elastic Container Registry (ECR) and Docker. Then, it continues by building and tagging the Docker image, pushing the Docker image to AWS ECR, and updating the AWS AppRunner service to deploy the Flask application. 

### Load Test 

### Quantitative Assessment

### Use of GenAI:
Our team used Generative AI to explore tools and packages that were new to us in conjunction with seeking out the software documentation and other learning resources. This included using the `locust` package in Python for load testing and the Google Gemini API to integrate prompts into our Flask app. 

