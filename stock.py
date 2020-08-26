
import tushare as ts
import json
pro = ts.pro_api("b45b68431dc2ada16c0695f43cb2deff1d597401600f82d892209180")

#查询当前所有正常上市交易的股票列表

data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,is_hs')
print(data)

column_list = []
for row in data:
    column_list.append(row)

jsonlist = []
for index in range(data[column_list[0]].size):
    dict = {}
    for row in data:
        dict[row] = data[row][index]
    jsonlist.append(dict)

jsonData = json.dumps(jsonlist,ensure_ascii=False)
fileObject = open('stockDict.json','w',encoding='utf-8')
fileObject.write(jsonData)
fileObject.close()