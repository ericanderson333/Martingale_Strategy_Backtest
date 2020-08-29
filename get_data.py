import pandas as pd 
import robin_stocks as rh

#stock ticker to test
ticker = 'SPY'

#Enter account information in account.txt...
#Or just skip this process and enter user information below.
#get login information from text file
with open('account.txt', 'rt') as readin:
    username = readin.readline().replace('\n', '')
    password = readin.readline().replace('\n', '')

#login
rh.login(username=username, password=password)

#get stock data
_data = rh.get_stock_historicals(ticker, interval='day', span='5year')
df = pd.DataFrame(_data)
df.to_csv('{}_day_data.csv'.format(ticker))
