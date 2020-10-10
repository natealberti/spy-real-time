# SPY real time prices via robinhood
import pandas as pd
import requests
import bs4
from bs4 import BeautifulSoup
import time
import datetime as dt

# in seconds
frequency = 3
timeframe = 12

def getSPYPrice(frequency, timeframe):
    prices = []
    print('retrieving live share prices . . .')
    for i in range (int(timeframe/frequency)):
        endpoint = 'https://robinhood.com/stocks/SPY'
        r = requests.get(endpoint)
        soup = bs4.BeautifulSoup(r.content, "html.parser")
        # live price
        prices.append(soup.find('div', {'class' : 'QzVHcLdwl2CEuEMpTUFaj'}).text)
        #print loading message
        print(str(round(((frequency*i) / timeframe)*100)) + "% complete")
        time.sleep(frequency)
    return prices

start_time = dt.datetime.now().time()
price_table = getSPYPrice(frequency, timeframe)
end_time = dt.datetime.now().time()
df = pd.DataFrame({'PRICE': price_table})
print(df)
df.to_csv('live_spy_prices.csv')
print("STARTED: " + str(start_time))
print("FINISHED: " + str(end_time))
