# BigQuery-NLP-Mongodb-ELT

## Introduction
![pipeline](./ReadMeAssets/pipeline.gif)

Analyzing a collection of articles from BigQuery's open datasets `BBC_news` using the Yake keywords extractor, this project focuses on the following steps:
1. **Extracting data from BigQuery**
2. **Loading data into MongoDB**
3. **Enhancing documents by adding extracted keywords using language models technology**

This project applies `SOLID` principles and class injections to ensure scalability and maintainability. 
> ## Streamlit Dashboard
> ![streamlit dashboard](./ReadMeAssets/dashboard.gif)
>**Check out the streamlit dashboard code at**: https://github.com/ahmadMuhammadGd/Mongodb-Streamlit-Report
## Pipeline Components
|                      | **Tools/Technologies**              |
|------------------------------|----------------------------------|
| **Orchestration Tools**      | - Airflow                        |
| **Databases**                | - BigQuery (source), MongoDB (destination)             |
| **Neural Language Processing (NLP)** | - Yake                         |
| **Containerization**         | - Docker Compose                 |
| **Report**        | - Streamlit
## Airflow Dags
- Update_source_view
- Articles_Keywords_ELT

## Workflow
> `Update_source_view` triggers `Articles_Keywords_ELT` to run, ensuring coordination between teams.
>![dags](./ReadMeAssets/dags.png)

## NoSQL Documents Examples
### Collections
An example from business collection. 
```json
{
  "_id": {
    "$oid": "6697feb71048a62901c6e1f3"
  },
  "filename": "bbc/business/458.txt",
  "body": "The founder and former boss of Parmalat has apologised to investors who lost money as a result of the Italian dairy firm's collapse.\n\nCalisto Tanzi said he would co-operate fully with prosecutors investigating the background to one of Europe's largest financial scandals. Parmalat was placed into bankruptcy protection in 2003 after a 14bn euro black hole was found in its accounts. More than 130,000 people lost money following the firm's collapse. Mr Tanzi, 66, issued a statement through his lawyer after five hours of questioning by prosecutors in Parma on 15 January.\n\nProsecutors are seeking indictments against Mr Tanzi and 28 others - including several members of his family and former Parmalat chief financial officer Fausto Tonna - for alleged manipulation of stock market prices and making misleading statements to accountants and Italy's financial watchdog. Two former Parmalat auditors will stand trial later this month for their role in the firm's collapse.\n\n\"I apologise to all who have suffered so much damage as a result of my schemes to make my dream of an industrial project come true,\" Mr Tanzi's statement said. \"It is my duty to collaborate fully with prosecutors to reconstruct the causes of Parmalat's sudden default and who is responsible.\" Mr Tanzi spent several months in jail in the wake of Parmalat's collapse and was kept under house arrest until last September. Parmalat is now being run by a state appointed administrator, Enrico Bondi, who has launched lawsuits against 80 banks in an effort to recover money for the bankrupt company and its shareholders. He has alleged that these companies were aware of the true state of Parmalat's finances but continued to lend money to the company. The companies insist they were the victims of fraudulent book-keeping. Parmalat was declared insolvent after it emerged that 4 billion euros (£2.8bn; $4.8bn) it supposedly held in an offshore account did not in fact exist. The firm's demise sent shock waves through Italy, where its portfolio of top-selling food brands and its position as the owner of leading football club Parma had turned it into a household name.\n",
  "random": 0.0006982499583650813,
  "title": "Parmalat founder offers apology",
  "keywords": [
    {
      "kw": "Italian dairy",
      "score": 0.013367307591868544
    },
    {
      "kw": "Parmalat",
      "score": 0.027950299081548495
    },
    {
      "kw": "Tanzi",
      "score": 0.04550597019923868
    },
    {
      "kw": "firm collapse",
      "score": 0.05602066230363478
    },
    {
      "kw": "Italian",
      "score": 0.06858188436226552
    },
    {
      "kw": "dairy firm",
      "score": 0.07361442107985204
    },
    {
      "kw": "firm",
      "score": 0.0891224126128558
    },
    {
      "kw": "collapse",
      "score": 0.10090128236005153
    },
    {
      "kw": "Europe largest",
      "score": 0.10154966381865103
    },
    {
      "kw": "lost money",
      "score": 0.10215472001201979
    },
    {
      "kw": "prosecutors",
      "score": 0.10468421268755809
    },
    {
      "kw": "Calisto Tanzi",
      "score": 0.10645232260575588
    },
    {
      "kw": "Parmalat collapse",
      "score": 0.1130006854040157
    },
    {
      "kw": "money",
      "score": 0.11561567670057422
    },
    {
      "kw": "Tanzi statement",
      "score": 0.1241301320727035
    },
    {
      "kw": "Fausto Tonna",
      "score": 0.1442827943131141
    },
    {
      "kw": "financial",
      "score": 0.14665078856152797
    },
    {
      "kw": "lost",
      "score": 0.18341870819798636
    },
    {
      "kw": "Parma",
      "score": 0.18387860016817345
    },
    {
      "kw": "Italy",
      "score": 0.18594613475620947
    }
  ]
}
```
### Views
>Views were made for analytical porpuses
#### business_keywords_freq_view
```json
[
  {
    "avg_score": 0.111338258204852,
    "freq": 22,
    "keyword": "year"
  },
  {
    "avg_score": 0.09752931847683353,
    "freq": 12,
    "keyword": "economy"
  },
  {
    "avg_score": 0.05581532139028804,
    "freq": 11,
    "keyword": "Russian"
  },
  {
    "avg_score": 0.05484452196956291,
    "freq": 11,
    "keyword": "dollar"
  },
  {
    "avg_score": 0.10877142304975647,
    "freq": 10,
    "keyword": "prices"
  },
  {
    "avg_score": 0.07934415679812448,
    "freq": 10,
    "keyword": "Bank"
  },
  {
    "avg_score": 0.08305731846809183,
    "freq": 9,
    "keyword": "European"
  },
  {
    "avg_score": 0.09940168001874845,
    "freq": 9,
    "keyword": "euro"
  },
  {
    "avg_score": 0.11052457035380452,
    "freq": 9,
    "keyword": "December"
  },
  {
    "avg_score": 0.046666928383127686,
    "freq": 9,
    "keyword": "Yukos"
  }
]
```
### business_top_articles_view
```json
[
  {
    "title": "German growth goes into reverse",
    "body": "Germany's economy shrank 0.2% in the last three months of 2004, upsetting hopes of a sustained recovery.\n\nThe figures confounded hopes of a 0.2% expansion in the fourth quarter in Europe's biggest economy. The Federal Statistics Office said growth for the whole of 2004 was 1.6%, after a year of contraction in 2003, down from an earlier estimate of 1.7%. It said growth in the third quarter had been zero, putting the economy at a standstill from July onward. Germany has been reliant on exports to get its economy back on track, as unemployment of more than five million and impending cuts to welfare mean German consumers have kept their money to themselves. Major companies including Volkswagen, DaimlerChrysler and Siemens have spent much of 2004 in tough talks with unions about trimming jobs and costs. According to the statistics office, Destatis, rising exports were outweighed in the fourth quarter by the continuing weakness of domestic demand.\n\nBut the relentless rise in the value of the euro last year has also hit the competitiveness of German products overseas. The effect has been to depress prospects for the 12-nation eurozone as a whole, as well as Germany. Eurozone interest rates are at 2%, but senior officials at the rate-setting European Central Bank are beginning to talk about the threat of inflation, prompting fears that interest rates may rise. The ECB's mandate is to fight rising prices by boosting interest rates - and that could further threaten Germany's hopes of recovery.\n",
    "score": 0
  }
]
```
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
