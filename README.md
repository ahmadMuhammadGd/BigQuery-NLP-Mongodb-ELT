# BigQuery-NLP-Mongodb-ELT

## Introduction
Analyzing a collection of articles from BigQuery's open datasets using NLP, this project focuses on extracting data from BigQuery, loading it into MongoDB, and enhancing documents by adding extracted keywords using NLP technology.

## Components
### Orchestration Tools:
- **Airflow**

### Databases:
- **BigQuery** as the source database
- **MongoDB** as the destination database

### Neural Language Processing (NLP):
- **Yake**

### Containerization:
- **Docker Compose**

## Airflow Dags
- Articles_Keywords_ELT
- Update_source_view

## Features
- `Update_source_view` triggers `Articles_Keywords_ELT` to run, ensuring coordination between teams.
- Applying SOLID principles for future development.

## Project Structure
```plaintext
.
├── airflow.cfg
├── credentials
│   └── my-project-428316-bad106950325.json
├── dags
│   ├── BQ2MongoArticlesPipeline.py
│   ├── globalVaribles
│   │   ├── BQ2Mongo.py
│   │   └── CleanedArticleView.py
│   └── UpdateSourceCleanedView.py
├── docker-compose.yml
├── dockerfile
├── Notebooks
│   └── ArticlesSourceEDA.ipynb
├── pipeline_config
│   ├── articlesPipelineConfig.json
│   └── sourceCleanedViewConfig.json
├── README.md
├── requirements.txt
├── setup.sh
└── src
    ├── Config_parser.py
    ├── KeywordExtraction
    │   ├── base.py
    │   ├── KeywordExtractor.py
    │   └── Yake.py
    ├── NoSQLDist
    │   ├── base.py
    │   ├── Loader.py
    │   └── Mongodb_client.py
    └── TabularSource
        ├── base.py
        ├── BigQuery_client.py
        └── Extractor.py
```

## Exploring Source Data
Insights and results are documented in `./Notebooks/ArticlesSourceEDA.ipynb`.

## Setting Up The Project
To set up the project, run `./setup.sh` to launch Docker Compose.

## Destination Database
### Collections
Extracted unique collections from the BigQuery source dataset and created corresponding collections.

### Views
- Created a view for unique keywords and their frequencies per collection.
- Created a view for unique articles, titles, and keywords and their frequencies per collection.
