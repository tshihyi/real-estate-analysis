# Real Estate Transaction Data Analysis
Crawler real estate transaction data with Python, and covert data to JSON with Spark. In additon, provide a simple API to query
transaction data.

## Workflow

<img src="https://github.com/tshihyi/real-estate-analysis/blob/main/image/work-flow.png" width="500">

**Web crawler with selenium and data cleansing with Pandas**
  - land_info.ipynb
    - 實價登錄交易資料source code

**Created RESTful API with FastAPI**
  - main.py
    - API source code
    - [API docs](https://tshihyi-api-docs.netlify.app/)(Swagger UI)

**Spark to JSON workflow**

<img src="https://github.com/tshihyi/real-estate-analysis/blob/main/image/spark-to-json.png" width="500">

**Generated specified JOSN with Spark**
  - [JSON files](https://drive.google.com/drive/folders/1EX6ZFLxrw-b1Zo3CEc418jfYUfVIXVvR?usp=sharing)
    - result-part1.json
    - result-part2.json
    
## Data Analysis Visualization
   ### Transaction amount statistics
   - 依縣市: 交易量第1縣市：_新北市_
   
     <img src="https://github.com/tshihyi/real-estate-analysis/blob/main/image/txn_amount_city.png" height= "250" width="300">
    
   - 依主要用途: 前4大主要用途：_住宅用,見其他登記事項,住商用,商業用_
  
     <img src="https://github.com/tshihyi/real-estate-analysis/blob/main/image/txn_reason.png" height= "270" width="550">
     
   - 依前4大交易用途於各縣市的交易統計
     
     <img src="https://github.com/tshihyi/real-estate-analysis/blob/main/image/city_top4_txn_reason_analysis.png">
 
   ### Observation transaction purpose in each city
   - 交易年度從2006至2019, 大部分的交易集中在2012至2019
   
     <img src="https://github.com/tshihyi/real-estate-analysis/blob/main/image/city_txn_reason_by_year.png" height= "250" width="370">
   
   ### Regression Analysis
   - 交易總價與面積呈現正相關
   
     <img src="https://github.com/tshihyi/real-estate-analysis/blob/main/image/price_area_regression_analysis.png" height= "250" width="300">
    
 

