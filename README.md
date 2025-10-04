# ETL Pipeline

This is a simple ETL (Extract, Transform, Load) pipeline built for a students dataset from Kaggle. The pipeline demonstrates data extraction, cleaning/transformation, and loading into a PostgreSQL database using Docker.

Dataset used:  
[Student Exam Score Dataset Analysis](https://www.kaggle.com/datasets/grandmaster07/student-exam-score-dataset-analysis)


## Requirements

- [Docker](https://www.docker.com/get-started)

---

## Getting Started

1. **ENV variables**
   
   make a .env file at the root of the project, then add these variables:
   
   `DB_USR=admin`

   `DB_PWD=admin`
