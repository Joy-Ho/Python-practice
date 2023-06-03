# 網路連線
import urllib.request as request
src = "https://www.ntu.edu.tw/"
with request.urlopen(src) as response:
    data = response.read().decode("utf-8") # data 是原始碼(前端HTML, CSS, JS), utf可顯示出中文字，不會是亂碼
print(data)
