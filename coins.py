import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from playsound import playsound
import sys
import os

secim = """ 
            >>> WELCOME TO COINS TOOL <<<
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
--exit ==> Press to "e" for exit

example:\n\tpython3 coins.py --coin ETH --buy 1,660 --sell 1,700
        python3 coins.py coin --help
 """

def islem(a):
    try:
        print('\33[34m'+secim[:45],'\33[31m'+secim[45:215],"\33[33m"+secim[215:458],"\33[36m"+secim[458:560])
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        browser = webdriver.Chrome(executable_path="/usr/bin/chromedriver", options=chrome_options)
        os.system("clear")
        while True:
            browser.get(a)
            aa = browser.title
            if len(aa) < 35:
                print('\33[33m' + "Time :", "\33[37m" + time.strftime('%c'), "\33[35m" + "Price :", '\33[32m' + aa[0:7])
                if aa[0:5] == sys.argv[4]:
                    print('\33[32m' + "Buy :", '\33[31m' +"Price :"+aa[0:7])
                    playsound("a.mp3")
                    aaa = input("Press exit 'e' or contiue 'c' :")
                    if aaa == "e":
                        browser.quit()
                        browser.close()
                    elif aaa == "c":
                        continue
                    else:
                        print("Wrong Value..!")
                elif aa[0:5] == sys.argv[6]:
                    print("\33[32m" + "Sell :", '\33[31m' +"Price :"+ aa[0:7])
                    playsound("a.mp3")
                    aaa = input("Press exit 'e' or contiue 'c' :")
                    if aaa == "e":
                        browser.quit()
                        browser.close()
                    elif aaa == "c":
                        continue
                    else:
                        print("Wrong Value..!")




    except:
        pass




try:
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
        print('\33[34m'+secim[:45],'\33[31m'+secim[45:215],"\33[33m"+secim[215:458],"\33[36m"+secim[458:560])
except:
    pass
