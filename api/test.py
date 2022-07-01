import json
import re

import requests
from bs4 import BeautifulSoup


class Bus:
    def __init__(self):
        self.url = "https://busnavi.keihanbus.jp/pc/busstatedtl?mode=4&fr=%E5%8C%97%E5%B1%B1%E4%B8%AD%E5%A4%AE&frsk=B&tosk=&dt=202206302320&dgmpl=%E5%8C%97%E5%B1%B1%E4%B8%AD%E5%A4%AE%E3%80%94%E4%BA%AC%E9%98%AA%E3%83%90%E3%82%B9%E3%80%95%3A2%3A1&p=0%2C14%2C15"
        self.res = ""

    def get_bus_info(self):
        headers = {"User-Agent": "Mozilla/5.0"}
        self.res = requests.get(self.url, headers=headers).text

    def scraping_bus_info(self):
        soup = BeautifulSoup(self.res, "html.parser")

        try:
            station = (
                (soup.find(class_="stationHead").text)
                .replace(" ", "")
                .replace("\n", "")
            )
            station = re.sub(r"\(.*\)", "\n", station)
            print(station)

            elem = soup.find_all(class_="fl bsdtl")
            status = list()
            status_list = list()

            for i in range(len(elem)):
                for j in elem[i].find_all("li"):
                    status.append((j.text).replace(" ", "").replace("\n", ""))
                status_list.append(status[:-3])
                status.clear()
            print(status_list)

        except AttributeError:
            print("現在バス接近情報がありません")

    def main():
        bus = Bus()
        bus.get_bus_info()
        bus.scraping_bus_info()


if __name__ == "__main__":
    Bus.main()
