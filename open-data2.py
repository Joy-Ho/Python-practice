#串接、擷取公開資料
import urllib.request as request
import json
src = "https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire"
with request.urlopen(src) as response:
    #data = response.read().decode("utf-8")
    data = json.load(response) # 已知src是json, 用json模組處理json資料格式
#print(data)

#取得公司名稱
clist = data["result"]["results"]
#print(clist)

#for company in clist:
    #print(company["公司名稱"])

with open("data.txt", "w", encoding = "utf-8") as file:
    for company in clist:
        file.write(company["公司名稱"] + "\n")
        