import requests



h1 = {
    "Accept": '*/*',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'en-US,en;q=0.9',
'Access-Control-Request-Headers': 'content-type',
'Access-Control-Request-Method': 'POST',
'Connection': 'keep-alive',
'Host': 'zeapi.yandex.net',
'Origin': 'https://yandex.ru',
'Referer': 'https://yandex.ru/',
'Sec-Fetch-Dest': 'empty',
'Sec-Fetch-Mode': 'cors',
'Sec-Fetch-Site': 'cross-site',
'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
}


h2 = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Content-Length': '42',
        'Content-Type': 'application/json',
        'Host': 'zeapi.yandex.net',
        'Origin': 'https://yandex.ru',
        'Referer': 'https://yandex.ru/',
        'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}


def main():
    d = {'query': "Итмо ", 'intro': 0, 'filter': 1}
    s = requests.Session()
    s.options('https://zeapi.yandex.net/lab/api/yalm/text3', headers=h1) 
    r = s.post(
        'https://zeapi.yandex.net/lab/api/yalm/text3', data=json.dumps(d), headers=h2)
    print(r.text)
