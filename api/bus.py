import api.scraping


def oit_to_nagao():
    rich_url = "https://busnavi.keihanbus.jp/pc/busstatedtl?mode=4&fr=%E5%8C%97%E5%B1%B1%E4%B8%AD%E5%A4%AE&frsk=B&tosk=&dt=202207041358&dgmpl=%E5%8C%97%E5%B1%B1%E4%B8%AD%E5%A4%AE%E3%80%94%E4%BA%AC%E9%98%AA%E3%83%90%E3%82%B9%E3%80%95%3A2%3A1&p=0%2C14%2C15"
    simple_url = "http://busnavi.keihanbus.jp/mobile/index.php/Route/TimeSheet?key_start=%96k%8ER%92%86%89%9B&key_end=%92%B7%94%F6&start=%96k%8ER%92%86%89%9B%81%5E%8B%9E%8D%E3%83o%83X&end=%92%B7%94%F6%89w%81%5E%8B%9E%8D%E3%83o%83X&se=a295301252a9917b4a22f89da9478e10"
    type_list = ["直通", "29"]

    return get_info(rich_url, simple_url, type_list)


def nagao_to_oit():
    rich_url = "https://busnavi.keihanbus.jp/pc/busstatedtl?mode=4&fr=%E9%95%B7%E5%B0%BE%E9%A7%85&frsk=B&tosk=&dt=202207041618&dgmpl=%E9%95%B7%E5%B0%BE%E9%A7%85%E3%80%94%E4%BA%AC%E9%98%AA%E3%83%90%E3%82%B9%E3%80%95%3A1%3A1&p=0%2C14%2C15"
    simple_url = "http://busnavi.keihanbus.jp/mobile/index.php/Route/TimeSheet?key_start=%96k%8ER&start=%96k%8ER%92%86%89%9B%81%5E%8B%9E%8D%E3%83o%83X&type=1&se=df681b2a928c0fb0b52ecf89bab8c611"
    type_list = ["直通", "27", "29", "37"]

    return get_info(rich_url, simple_url, type_list)


def oit_to_kuzuha():
    rich_url = "https://busnavi.keihanbus.jp/pc/busstatedtl?mode=4&fr=%E5%8C%97%E5%B1%B1%E4%B8%AD%E5%A4%AE&frsk=B&tosk=&dt=202207041627&dgmpl=%E5%8C%97%E5%B1%B1%E4%B8%AD%E5%A4%AE%E3%80%94%E4%BA%AC%E9%98%AA%E3%83%90%E3%82%B9%E3%80%95%3A1%3A1&p=0%2C14%2C15"
    simple_url = "http://busnavi.keihanbus.jp/mobile/index.php/Route/TimeSheet?key_start=%96k%8ER&start=%96k%8ER%92%86%89%9B%81%5E%8B%9E%8D%E3%83o%83X&type=1&se=df681b2a928c0fb0b52ecf89bab8c611"
    type_list = ["1", "2", "2A"]

    return get_info(rich_url, simple_url, type_list)


def kuzuha_to_oit():
    rich_url = "https://busnavi.keihanbus.jp/pc/busstatedtl?mode=4&fr=%E6%A8%9F%E8%91%89%E9%A7%85&frsk=B&tosk=&dt=202207041656&dgmpl=%E6%A8%9F%E8%91%89%E9%A7%85%E3%80%94%E4%BA%AC%E9%98%AA%E3%83%90%E3%82%B9%E3%80%95%3A4%3A1&p=0%2C14%2C15"
    simple_url = "http://busnavi.keihanbus.jp/mobile/index.php/Route/TimeSheet?key_start=%8F%BE%97t&start=%8F%BE%97t%89w%81%5E%8B%9E%8D%E3%83o%83X&type=1&se=aaa253f7a16306ccf16522f86e5a808b"
    type_list = ["直通", "大2", "大2A"]

    return get_info(rich_url, simple_url, type_list)


def oit_to_hirakata():
    rich_url = ""
    simple_url = ""
    type_list = [""]

    return get_info(rich_url, simple_url, type_list)


def hirakata_to_oit():
    rich_url = ""
    simple_url = ""
    type_list = [""]

    return get_info(rich_url, simple_url, type_list)


def get_info(rich_url, simple_url, type_list):
    bus = api.scraping.Bus
    return bus.main(rich_url, simple_url, type_list)
