import requests

url = "https://busnavi.keihanbus.jp/pc/busstatedtl?mode=4&fr=%E5%8C%97%E5%B1%B1%E4%B8%AD%E5%A4%AE&frsk=B&tosk=&dt=202206302320&dgmpl=%E5%8C%97%E5%B1%B1%E4%B8%AD%E5%A4%AE%E3%80%94%E4%BA%AC%E9%98%AA%E3%83%90%E3%82%B9%E3%80%95%3A2%3A1&p=0%2C14%2C15"

header = {"User-Agent": "Mozilla/5.0"}

res = requests.get(url, headers=header).text

with open("bus.html", "w", encoding="utf-8") as f:
    f.write(res)
