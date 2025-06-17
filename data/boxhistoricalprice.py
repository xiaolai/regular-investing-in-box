from datetime import date
# import requests
# from bs4 import BeautifulSoup
# from re import sub

# todaysdate = date.today().strftime('%Y-%m-%d')

# URL = 'https://coinmarketcap.com/currencies/bitcoin/markets/'
# page = requests.get(URL)
# soup = BeautifulSoup(page.content, 'html.parser')
# results = soup.find('span', class_='cmc-details-panel-price__price')
# for result in results:
#     btc_price = result
    
# URL = 'https://coinmarketcap.com/currencies/eos/markets/'
# page = requests.get(URL)
# soup = BeautifulSoup(page.content, 'html.parser')
# results = soup.find('span', class_='cmc-details-panel-price__price')
# for result in results:
#     eos_price = result

# URL = 'https://coinmarketcap.com/currencies/mixin/markets/'
# page = requests.get(URL)
# soup = BeautifulSoup(page.content, 'html.parser')
# results = soup.find('span', class_='cmc-details-panel-price__price')
# for result in results:
#     xin_price = result

from re import sub
import requests
import json

todaysdate = date.today().strftime('%Y-%m-%d')

BTCresponse = json.loads(requests.get("https://bigone.com/api/v3/asset_pairs/BTC-USDT/ticker", headers={'Connection':'close'}).text)
btc_price = '${:,.2f}'.format(float(BTCresponse['data']['close']))

EOSresponse = json.loads(requests.get("https://bigone.com/api/v3/asset_pairs/A-USDT/ticker", headers={'Connection':'close'}).text)
eos_price = '${:,.2f}'.format(float(EOSresponse['data']['close']))

XINresponse = json.loads(requests.get("https://bigone.com/api/v3/asset_pairs/XIN-USDT/ticker", headers={'Connection':'close'}).text)
xin_price = '${:,.2f}'.format(float(XINresponse['data']['close']))

ETHresponse = json.loads(requests.get("https://bigone.com/api/v3/asset_pairs/ETH-USDT/ticker", headers={'Connection':'close'}).text)
eth_price = '${:,.2f}'.format(float(ETHresponse['data']['close']))

DOTresponse = json.loads(requests.get("https://bigone.com/api/v3/asset_pairs/DOT-USDT/ticker", headers={'Connection':'close'}).text)
dot_price = '${:,.2f}'.format(float(DOTresponse['data']['close']))

MOBresponse = json.loads(requests.get("https://bigone.com/api/v3/asset_pairs/MOB-USDT/ticker", headers={'Connection':'close'}).text)
mob_price = '${:,.2f}'.format(float(MOBresponse['data']['close']))

UNIresponse = json.loads(requests.get("https://bigone.com/api/v3/asset_pairs/UNI-USDT/ticker", headers={'Connection':'close'}).text)
uni_price = '${:,.2f}'.format(float(UNIresponse['data']['close']))

SOLresponse = json.loads(requests.get("https://bigone.com/api/v3/asset_pairs/SOL-USDT/ticker", headers={'Connection':'close'}).text)
sol_price = '${:,.2f}'.format(float(SOLresponse['data']['close']))

box_price = '${:,.2f}'.format((float(sub(r'[^\d.]', '', btc_price)) * 1 + float(sub(r'[^\d.]', '', eos_price)) * 0 + float(sub(r'[^\d.]', '', xin_price)) * 8 + float(sub(r'[^\d.]', '', eth_price)) * 1 + float(sub(r'[^\d.]', '', dot_price)) * 0 + float(sub(r'[^\d.]', '', mob_price)) * 0 + float(sub(r'[^\d.]', '', uni_price)) * 100 + float(sub(r'[^\d.]', '', sol_price)) * 5)/10000) 

# f = open("box_price_history.txt", "a")
f = open("/root/regular-investing-in-box/data/box_price_history.txt", "a")
f.write(todaysdate + '\t' + btc_price + '\t' + eos_price + '\t' + xin_price + '\t' + eth_price + '\t' + dot_price + '\t' + mob_price + '\t' + uni_price + '\t' + sol_price + '\t' + box_price +'\r')
f.close()

# on MacOSX, in terminal:
# > crontab -e
# 0 8 * * * cd /root/regular-investing-in-box/data && /root/anaconda3/bin/python boxhistoricalprice.py && cd /root/regular-investing-in-box && git pull && git add . && git commit -a -m "box historical price auto-updated" && git push -u origin master 
# > about ctron time setting, see: https://crontab.guru/#59_23_*_*_*
