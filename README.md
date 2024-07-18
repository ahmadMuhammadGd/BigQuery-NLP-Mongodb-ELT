# BigQuery-NLP-Mongodb-ELT

## Introduction
![pipeline](./ReadMeAssets/pipeline.gif)

Analyzing a collection of articles from BigQuery's open datasets `BBC_news` using the Yake keywords extractor, this project focuses on the following steps:
1. **Extracting data from BigQuery**
2. **Loading data into MongoDB**
3. **Enhancing documents by adding extracted keywords using language models technology**

This project applies `SOLID` principles and class injections to ensure scalability and maintainability. 
> ## Streamlit Dashboard
>**Check out the streamlit dashboard code at**: https://github.com/ahmadMuhammadGd/Mongodb-Streamlit-Report
> ![streamlit dashboard](./ReadMeAssets/dashboard.gif)
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
    "$oid": "669992bab427cd84f1c680db"
  },
  "filename": "bbc/business/281.txt",
  "body": "Life insurer Axa Sun Life has lowered annual bonus payouts for up to 50,000 with-profits investors.\n\nRegular annual bonus rates on former Axa Equity & Law with-profits policies are to be cut from 2% to 1% for 2004. Axa blamed a poor stock market performance for the cut, adding that recent gains have not yet offset the market falls seen in 2001 and 2002. The cut will hit an estimated 3% of Axa's policyholders. The rest will know their fate in March.\n\nThe cuts on Axa's policies will mean a policyholder who had invested £50 a month into an endowment policy for the past 25 years would see a final maturity payout of £46,998. This equated to a annual investment growth rate of 8% Axa said. With-profits policies are designed to smooth out the peaks and troughs of stock market volatility. However, heavy stock market falls throughout 2001 and 2002 forced most firms to trim bonus rates on their policies. \"The stock market has grown over the past 18 months, however not enough to undo the damage that occurred during 2001 and 2002,\" Axa spokesman Mark Hamilton, Axa spokesman, told BBC News. Axa cut payouts for the same investors last January.\n",
  "title": "Axa Sun Life cuts bonus payments",
  "keywords": [
    {
      "kw": "Sun Life",
      "score": 0.007648533691608657
    },
    {
      "kw": "Life insurer",
      "score": 0.024272265880068356
    },
    {
      "kw": "Axa Sun",
      "score": 0.024500972347428197
    },
    {
      "kw": "Axa",
      "score": 0.03517384654956117
    },
    {
      "kw": "Life",
      "score": 0.050237791593689685
    },
    {
      "kw": "annual bonus",
      "score": 0.0638285585827784
    },
    {
      "kw": "Axa Equity",
      "score": 0.06904821186647411
    },
    {
      "kw": "Sun",
      "score": 0.07554549500129021
    },
    {
      "kw": "Law with-profits",
      "score": 0.07718050218782431
    },
    {
      "kw": "insurer Axa",
      "score": 0.08068561552682202
    },
    {
      "kw": "stock market",
      "score": 0.08688426484110995
    },
    {
      "kw": "lowered annual",
      "score": 0.09030430262142879
    },
    {
      "kw": "market",
      "score": 0.10012381852669737
    },
    {
      "kw": "bonus rates",
      "score": 0.10399520573237472
    },
    {
      "kw": "bonus",
      "score": 0.1074534507870518
    },
    {
      "kw": "with-profits policies",
      "score": 0.11037455339425017
    },
    {
      "kw": "cut",
      "score": 0.11246057554565242
    },
    {
      "kw": "annual",
      "score": 0.11705907577406108
    },
    {
      "kw": "with-profits",
      "score": 0.11705907577406108
    },
    {
      "kw": "policies",
      "score": 0.12873190701492288
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
