from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from playsound import playsound
import tkinter as tk
import sys


def islem(a):
    try:
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        browser = webdriver.Chrome(executable_path="/usr/bin/chromedriver", options=chrome_options)
        while True:
            browser.get(a)
            aa = browser.title
            if len(aa) < 35:
                print("\33[35m", "Price >>", aa)
                if aa[0:5] == sys.argv[4]:
                    print('\33[34m', "Buy >>", aa[0:5])
                    playsound("a.mp3")
                    sleep(20)
                    browser.close()
                    browser.quit()
                elif aa[0:5] == sys.argv[6]:
                    print("\33[31m", "Sell >>", aa[0:5])
                    playsound("a.mp3")
                    sleep(20)
                    browser.close()
                    browser.quit()

    except:
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")


secim = """ 
                 >>>WELCOME TO COINS TOOL<<<
\nAbout: This tool allows you to track the coin price,
alerts you when coin reaches the desired buy or sale price.
                                        CODED BY TMRSWRR
Parameters:

--coin ==> Choose which coin you want to track
    Coin list:  BTC ETH DASH LTC XRP ADA EOS DOT DOGE 
--buy  ==> Set purchase price
       ex:1,550
--sell ==> Set sale price
       ex:1,580
--help     

example:\n\tpython3 coins.py --coin ETH --buy 1,500 --sell 1,550
        python3 coins.py coin --help
 """


           
if sys.argv[2] in ['BTC', ]:
    a = "https://www.binance.com/tr/trade/BTC_USDT"
    islem(a)
elif sys.argv[2] in ['ETH']:
    a = "https://www.binance.com/tr/trade/ETH_USDT"
    islem(a)
elif sys.argv[2] in ['DASH']:
    a = "https://www.binance.com/en/trade/DASH_USDT"
    islem(a)
elif sys.argv[2] in ['LTC']:
    a = "https://www.binance.com/tr/trade/LTC_USDT"
    islem(a)
elif sys.argv[2] in ['XRP']:
    a = "https://www.binance.com/tr/trade/XRP_USDT"
    islem(a)
elif sys.argv[2] in ['ADA']:
    a = "https://www.binance.com/tr/trade/ADA_USDT"
    islem(a)
elif sys.argv[2] in ['EOS']:
    a = "https://www.binance.com/tr/trade/EOS_USDT"
    islem(a)
elif sys.argv[2] in ['DOT']:
    a = "https://www.binance.com/tr/trade/DOT_USDT"
    islem(a)
elif sys.argv[2] in ['DOGE']:
    a = "https://www.binance.com/en/trade/DOGE_USDT"
    islem(a)
elif sys.argv[2] in ['-h', '--help']:
    print('\33[95m',secim)
    


else:
    print("wrong parameters...")
