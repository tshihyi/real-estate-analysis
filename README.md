# Real Estate Transaction Data Analysis
Crawler real estate transaction data with Python, and covert data to JSON with Spark. In additon, provide a simple API to query
transaction data.

**Workflow**

<img src="https://github.com/tshihyi/real-estate-analysis/blob/main/image/work-flow.png" width="500">

**Web crawler with selenium and data cleansing with Pandas**
  - land_info.ipynb
    - 實價登錄交易資料source code

**Created RESTful API with FastAPI**
  - main.py
    - API source code
    - [API docs](https://simple-api.tshihyi.repl.co/docs#/default/read_item_items__get)(Swagger UI)

**Spark to JSON workflow**

<img src="https://github.com/tshihyi/real-estate-analysis/blob/main/image/spark-to-json.png" width="500">

**Generated specified JOSN with Spark**
  - [JSON files](https://drive.google.com/drive/folders/1EX6ZFLxrw-b1Zo3CEc418jfYUfVIXVvR?usp=sharing)
    - result-part1.json
    - result-part2.json
