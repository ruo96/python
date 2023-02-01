import urllib.request

url = "https://www.baidu.com"
#网页连接
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
}
#定义headers，模拟浏览器访问
req = urllib.request.Request(url,headers)
#模拟浏览器发送，访问网页
response = urllib.request.urlopen(req)
#获取页面信息
print(response.read().decode("utf-8"))