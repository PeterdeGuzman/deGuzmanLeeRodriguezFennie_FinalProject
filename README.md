# Peter, Ilseop, Eric, and Zachary Data Engineering Project

## Status Badges
[![IaC](https://github.com/PeterdeGuzman/deGuzmanLeeRodriguezFennie_FinalProject/actions/workflows/IaC.yml/badge.svg)](https://github.com/PeterdeGuzman/deGuzmanLeeRodriguezFennie_FinalProject/actions/workflows/IaC.yml)
[![Install Required Dependencies](https://github.com/PeterdeGuzman/deGuzmanLeeRodriguezFennie_FinalProject/actions/workflows/install.yml/badge.svg)](https://github.com/PeterdeGuzman/deGuzmanLeeRodriguezFennie_FinalProject/actions/workflows/install.yml)
[![Format Code in Repository](https://github.com/PeterdeGuzman/deGuzmanLeeRodriguezFennie_FinalProject/actions/workflows/format.yml/badge.svg)](https://github.com/PeterdeGuzman/deGuzmanLeeRodriguezFennie_FinalProject/actions/workflows/format.yml)
[![Lint Code in Repository](https://github.com/PeterdeGuzman/deGuzmanLeeRodriguezFennie_FinalProject/actions/workflows/lint.yml/badge.svg)](https://github.com/PeterdeGuzman/deGuzmanLeeRodriguezFennie_FinalProject/actions/workflows/lint.yml)
[![Test Code in Repository](https://github.com/PeterdeGuzman/deGuzmanLeeRodriguezFennie_FinalProject/actions/workflows/test.yml/badge.svg)](https://github.com/PeterdeGuzman/deGuzmanLeeRodriguezFennie_FinalProject/actions/workflows/test.yml)

## Our project developed a microservice that interfaces with a data pipeline, built using Python or Rust and containerized with a Distroless Docker image. The microservice includes logging functionality and is capable of handling 10,000 requests per second, with a load test verifying its performance. For the data engineering aspect, we utilized libraries such as Spark, Pandas, SQL, and a vector database. We implemented Infrastructure as Code (IaC) using tools like AWS CloudFormation, AWS SAM, AWS CDK, or the Serverless Framework to manage the infrastructure. The project also includes a CI/CD pipeline for seamless integration and delivery. Our repository contains a comprehensive README.md, an architectural diagram, and proper GitHub/GitLab configurations to ensure the project is fully reproducible. Additionally, we performed a quantitative assessment of the system's reliability and stability, analyzing performance metrics like latency at different request rates. The project is accompanied by a demo video that showcases the application, load test, and system performance. Each team member also submitted a reflection report, including a peer evaluation and feedback session for improving team collaboration.

### Diagram Example
<img width="960" alt="Screenshot 2024-12-02 at 6 47 18 PM" src="https://github.com/user-attachments/assets/c8f60fc3-5eb7-4d2a-bc2a-eff656597d58">

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

## Data
### Goodreads.com Mystery, Thriller & Crime Genre Dataset
Our dataset, created by Mengting Wan, was collected in late 2017 from Goodreads.com. It specifically focuses on users' public shelves, which are accessible to everyone on the web without requiring a login. The dataset includes anonymized User IDs and Review IDs to protect privacy. Specifically, the data we used was the Mystery, Thriller & Crime genre, containing data on 219,235 books, 24,799,896 interactions, and 1,849,236 detailed reviews. This rich dataset is used to analyze user behavior, book preferences, and interactions within the genre, providing valuable insights for recommendations and data-driven decision-making in our microservice. The data can be accessed via Menting Wan's repository at https://github.com/MengtingWan/goodreads .
