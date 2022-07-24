from fastapi import FastAPI
from typing import Union
import uvicorn
import sqlite3

app = FastAPI()


@app.get("/items/")
async def read_item(
    floors: Union[int, None] = None,
    district: Union[str, None] = None,
    building_type: Union[str, None] = None
):

    sql_str = "SELECT * FROM land_txn_log WHERE 1 = 1 "

    item = {}
    if floors:
        item.update({"floors": floors})
        sql_str += ' AND floor_Num = :floors '
    if district:
        item.update({"district": district})
        sql_str += ' AND `鄉鎮市區` = :district '
    if building_type:
        item.update({"building_type": building_type+"%"})
        sql_str += ' AND `建物型態` like :building_type '

    connection = sqlite3.connect('land.db')
    cursor = connection.cursor()
    cursor.execute(sql_str + " limit 10;", item)
    data = cursor.fetchall()
    connection.close()

    return list(map(lambda item: {
        "city": item[0],
        "鄉鎮市區": item[1],
        "交易標的": item[2],
        "土地位置建物門牌": item[3],
        "土地移轉總面積平方公尺": item[4],
        "都市土地使用分區": item[5],
        "非都市土地使用分區": item[6],
        "非都市土地使用編定": item[7],
        "交易年月日": item[8],
        "交易筆棟數": item[9],
        "移轉層次": item[10],
        "總樓層數": item[11],
        "建物型態": item[12],
        "主要用途": item[13],
        "主要建材": item[14],
        "建築完成年月": item[15],
        "建物移轉總面積平方公尺": item[16],
        "建物現況格局-房": item[17],
        "建物現況格局-廳": item[18],
        "建物現況格局-衛": item[19],
        "建物現況格局-隔間": item[20],
        "有無管理組織": item[21],
        "總價元": item[22],
        "單價元平方公尺": item[23],
        "車位類別": item[24],
        "車位移轉總面積(平方公尺)": item[25],
        "車位總價元": item[26],
        "備註": item[27],
        "編號": item[28],
        "主建物面積": item[29],
        "附屬建物面積": item[30],
        "陽台面積": item[31],
        "電梯": item[32],
        "移轉編號": item[33]
    }, data))

uvicorn.run(app, host="0.0.0.0", port=8080)
