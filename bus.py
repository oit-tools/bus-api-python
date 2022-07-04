import re

import requests
from bs4 import BeautifulSoup


class Bus:
    def __init__(self):
        self._result = dict()

    # 運行状況の詳細情報を取得
    def get_bus_info(self, rich_url, simple_url, type_list):
        headers = {"User-Agent": "Mozilla/5.0"}
        html = requests.get(rich_url, headers=headers).text
        soup = BeautifulSoup(html, "html.parser")

        try:
            self._result.update({"bus_service": True})
            # 曜日を取得
            self.get_day_of_week(simple_url)
            # バスののりば、おりばを取得
            self.get_bus_station(soup)
            # 運行状況等を取得
            self.get_bus_timetable(soup, type_list)

        except AttributeError:
            self._result.clear()
            self._result.update({"bus_service": False})

    # 曜日を取得
    def get_day_of_week(self, simple_url):
        html = requests.get(simple_url).text
        soup = BeautifulSoup(html, "html.parser")
        self._result.update({"dow": soup.find_all("font")[1].text})

    # バスののりば、おりばを取得
    def get_bus_station(self, soup):
        station = (
            (soup.find(class_="stationHead").text).replace(" ", "").replace("\n", "")
        )
        station = (re.sub(r"\(.*\)", "\n", station)).split("\n")
        station[0] = station[0].replace("停留所：", "")
        station[1] = station[1].replace("のりば：", "")
        self._result.update({"bus_terminal": station[1], "bus_stop": station[0]})

    # 運行状況等を取得
    def get_bus_timetable(self, soup, type_list):
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
            self.normalize_bus_info(value)
            # 接近情報未取得のものを除外
            if len(value) < 9:
                value.clear()
                continue
            # 系統が違うものを除外
            elif value[2] not in type_list:
                value.clear()
                continue
            else:
                timetable.append(dict(zip(key, value[:-3])))
                value.clear()

        self._result.update({"timetable": timetable})

    # 正規化
    def normalize_bus_info(self, value):
        value[1] = value[1].replace("到着予定", "")
        value[2] = value[2].replace("系統：", "").replace("[", "").replace("]", "")
        value[3] = value[3].replace("行先：", "").replace("行", "")
        value[4] = value[4].replace("定刻：", "")
        value[5] = value[5].replace("(", "").replace(")", "")
        value[6] = value[6].replace("経由：", "")

    # 出力
    def return_bus_info(self):
        return self._result
