import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import sys
from time import sleep

secim = """\033[1;33m
  ╭━━━━┳━━━┳━━━┳━━━┳━━━┳━━━╮
  ┃╭╮╭╮┃╭━╮┃╭━╮┣╮╭╮┃╭━━┫╭━╮┃
  ╰╯┃┃╰┫╰━╯┃┃╱┃┃┃┃┃┃╰━━┫╰━╯┃
  ╱╱┃┃╱┃╭╮╭┫╰━╯┃┃┃┃┃╭━━┫╭╮╭╯
  ╱╱┃┃╱┃┃┃╰┫╭━╮┣╯╰╯┃╰━━┫┃┃╰╮
  ╱╱╰╯╱╰╯╰━┻╯╱╰┻━━━┻━━━┻╯╰━╯
         \033[1;32mCODED BY TMRSWRR
                   This tool allows 
          you to track the 
                   coin price,alerts 
          you when the coin 
                   reaches the desired 
          buy or sale price.
        
\033[1;33mParameters:

\033[1;32m--coin ==> \033[0mChoose which coin you want to track
    Coin list:  \033[1;32mBTC ETH DASH LTC XRP ADA EOS DOT DOGE\033[0m
\033[1;32m--buy  ==> \033[0mSet purchase price
       ex: \033[1;32m1,550\033[0m
\033[1;32m--sell ==> \033[0mSet sale price
       ex: \033[1;32m1,580\033[0m
\033[1;32m--help\033[0m
\033[1;32m--exit ==> \033[0mPress 'e' for exit

\033[1;32m
example:\n\t\033[0mpython3 coins.py --coin ETH --buy 1,660 --sell 1,700
        python3 coins.py --coin ETH --help
"""

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

def islem(a):
    try:
        print('\33[34m'+secim[:45],'\33[31m'+secim[45:215],"\33[33m"+secim[215:458],"\33[36m"+secim[458:560])

        chrome_service = Service("/usr/bin/chromedriver")
        browser = webdriver.Chrome(service=chrome_service, options=chrome_options)

        while True:
            browser.get(a)
            sleep(5)
            aa = browser.title
            print(aa)

    except Exception as e:
        print(f"An error occurred: {e}")

try:
    if sys.argv[2] in ['BTC', ]:
        a = "https://www.binance.com/en/trade/BTC_USDT"
        islem(a)
    elif sys.argv[2] in ['ETH']:
        a = "https://www.binance.com/en/trade/ETH_USDT"
        islem(a)
    elif sys.argv[2] in ['DASH']:
        a = "https://www.binance.com/en/trade/DASH_USDT"
        islem(a)
    elif sys.argv[2] in ['LTC']:
        a = "https://www.binance.com/en/trade/LTC_USDT"
        islem(a)
    elif sys.argv[2] in ['XRP']:
        a = "https://www.binance.com/en/trade/XRP_USDT"
        islem(a)
    elif sys.argv[2] in ['ADA']:
        a = "https://www.binance.com/en/trade/ADA_USDT"
        islem(a)
    elif sys.argv[2] in ['EOS']:
        a = "https://www.binance.com/en/trade/EOS_USDT"
        islem(a)
    elif sys.argv[2] in ['DOT']:
        a = "https://www.binance.com/en/trade/DOT_USDT"
        islem(a)
    elif sys.argv[2] in ['DOGE']:
        a = "https://www.binance.com/en/trade/DOGE_USDT"
        islem(a)
    elif sys.argv[2] in ['-h', '--help']:
        print('\33[34m'+secim[:45],'\33[31m'+secim[45:215],"\33[33m"+secim[215:458],"\33[36m"+secim[458:560])
except IndexError:
    print("Please provide a valid command-line argument.")
except Exception as e:
    print(f"An error occurred: {e}")
