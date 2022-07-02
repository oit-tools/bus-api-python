import json
import re

import requests
from bs4 import BeautifulSoup


class Bus:
    def __init__(self):
        self._rich_url = "https://busnavi.keihanbus.jp/pc/busstatedtl?mode=4&fr=%E5%8C%97%E5%B1%B1%E4%B8%AD%E5%A4%AE&frsk=B&tosk=&dt=202206302320&dgmpl=%E5%8C%97%E5%B1%B1%E4%B8%AD%E5%A4%AE%E3%80%94%E4%BA%AC%E9%98%AA%E3%83%90%E3%82%B9%E3%80%95%3A2%3A1&p=0%2C14%2C15"
        self._simple_url = "http://busnavi.keihanbus.jp/mobile/index.php/Route/TimeSheet?key_start=%96k%8ER&start=%96k%8ER%92%86%89%9B%81%5E%8B%9E%8D%E3%83o%83X&type=1&se=df681b2a928c0fb0b52ecf89bab8c611"
        self._result = dict()

    # 曜日を取得
    def get_day_of_week(self):
        html = requests.get(self._simple_url).text
        soup = BeautifulSoup(html, "html.parser")
        self._result.update({"dow": soup.find_all("font")[1].text})

    # 運行状況の詳細情報を取得
    def get_bus_info(self):
        headers = {"User-Agent": "Mozilla/5.0"}
        html = requests.get(self._rich_url, headers=headers).text
        soup = BeautifulSoup(html, "html.parser")

        try:
            # バスののりば、おりばを取得
            self.get_bus_station(soup)
            # 運行状況等を取得
            self.get_bus_timetable(soup)

        except AttributeError:
            print("現在バス接近情報がありません")

    def get_bus_station(self, soup):
        station = (
            (soup.find(class_="stationHead").text).replace(" ", "").replace("\n", "")
        )
        station = (re.sub(r"\(.*\)", "\n", station)).split("\n")
        self._result.update({"bus_terminal": station[1], "bus_stop": station[0]})

    def get_bus_timetable(self, soup):
        elem = soup.find_all(class_="fl bsdtl")
        key = [
            "arrive",
            "expectation",
            "type",
            "destination",
            "fixed_time",
            "status",
            "via",
        ]
        value = list()
        timetable = list()

        for i in range(len(elem)):
            for j in elem[i].find_all("li"):
                value.append((j.text).replace(" ", "").replace("\n", ""))
            timetable.append(dict(zip(key, value[:-3])))
            value.clear()
        self._result.update({"timetable": timetable})

    # jsonにして出力
    def return_bus_info(self):
        return json.dumps(self._result, ensure_ascii=False, indent=4)

    def main():
        bus = Bus()
        bus.get_day_of_week()
        bus.get_bus_info()

        result = bus.return_bus_info()
        print(result)


if __name__ == "__main__":
    Bus.main()
