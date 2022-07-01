import re
import urllib.parse

import requests


class nagao:
    def __init__(self):
        self._to_oit_url = (
            "http://busnavi.keihanbus.jp/mobile/index.php/Route/TimeSheet?"
            "key_start=長尾&"
            "key_end=北山&"
            "start=長尾駅／京阪バス&"
            "end=北山中央／京阪バス&"
            "se=7e16ccfa1548c562bee6b6de0f2062ad"
        )
        self._to_nagao_url = ""
        self._decode_url = ""
        self.response = ""
        self.date = ""
        self.diagram = ""

    def url_encode(self):
        self._decode_url = urllib.parse.quote(
            self._to_oit_url, encoding="shift-jis", safe=":/=?&"
        )

    def get_content(self):
        self.response = requests.get(self._decode_url).text

    def get_date(self):
        self.date = re.search(r"\d\d時\d\d分現在", self.response).group(0)

    def get_diagram(self):
        self.diagram = re.search(r'<font color="red">\S\S</font>', self.response).group(
            0
        )
        print(self.diagram)


if __name__ == "__main__":
    bus = nagao()
    bus.url_encode()
    bus.get_content()
    bus.get_date()
    bus.get_diagram()
