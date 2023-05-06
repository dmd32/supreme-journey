import requests
import os

ltuid = os.environ.get('LTUID')
ltoken = os.environ.get('LTOKEN')

genshinCheckinUrl = "https://hk4e-api-os.mihoyo.com/event/sol/sign?act_id=e202102251931481&lang=ru-ru"
starRailCheckinUrl = "https://sg-public-api.hoyolab.com/event/luna/os/sign?act_id=e202303301540311&lang=ru"

cookies = {'ltuid': ltuid, 'ltoken': ltoken}

genshinCheckin = requests.post(genshinCheckinUrl, cookies=cookies)
print(genshinCheckin.json())

starRailCheckin = requests.post(starRailCheckinUrl, cookies=cookies)
print(starRailCheckin.json())
