import pandas as pd
import numpy as np
from get_data import ticker


def walk_theory_backtest(test_df):
    #make copy of global csv file
    df = test_df.copy() 

    #columns to append to list
    buy = [] #number of buys on that day
    sell = [] #number of sells on that day (will sell total amount of current position listed below)
    acc_val = [] #account value
    weighted_avg = [] #weighted averages 
    
    #flags during backtesting
    curr_position = 0 #amount of shares we are holding (25 shares)
    '''for current buys:
    max amount of times to buy in sequence will be 5 times (1,2,3,4,5)
    each time we buy, we append two shares to previous buy.
    Ex: [first buy: 1 share (1 total share)]
        [second buy: 3 shares (4 total shares)]
        [third buy: 5 shares (9 total shares)]
        [fourth buy: 7 shares (16 total shares)]
        [fifth buy (max): 9 shares (25 total shares)]'''
    curr_buys = 0 
    max_buys = 9 #max amount curr_buys can equate to

    #loops through each row
    for i in range(len(df)):
        #this case just for first date, append the shmoneyyy
        if not acc_val:
            acc_val.append(10000)
            #append 0 for every element that we dont muck with
            buy.append(0)
            sell.append(0)
            weighted_avg.append(0)
            continue        
        #initial first day buy order
        if df['close_price'][i] < df['close_price'][i-1] and curr_buys == 0:
             curr_position = 1
             curr_buys = 1
             buy.append(curr_buys)
             sell.append(0)
             weighted_avg.append(df['close_price'][i])
             acc_val.append(acc_val[i-1])
        #any buy orders after the first day
        elif df['close_price'][i] < df['close_price'][i-1] and curr_buys != max_buys and curr_buys > 0 and df['close_price'][i] < weighted_avg[i-1]:
            #hold current buys when calculating account value
            hold_curr_buys = curr_buys
            #hold current position when calculating weighted average
            prev_curr_position = curr_position
            curr_buys += 2
            curr_position += curr_buys
            buy.append(curr_buys)
            sell.append(0)
            #calculate weighted average
            avg_to_add = (prev_curr_position * weighted_avg[i-1] + (curr_buys * df['close_price'][i]))/curr_position
            weighted_avg.append(avg_to_add)
            #calculate account value
            val_to_add = (df['close_price'][i] - df['close_price'][i-1]) * (hold_curr_buys)
            val_to_add = val_to_add + acc_val[i-1]
            acc_val.append(val_to_add)
        #sell (always sell all current positions at a time)
        elif df['close_price'][i] > df['close_price'][i-1] and df['close_price'][i] > weighted_avg[i-1]:
            buy.append(0)
            sell.append(curr_position)
            #calculate account value
            val_to_add = (df['close_price'][i] - df['close_price'][i-1]) * (curr_position)
            val_to_add = val_to_add + acc_val[i-1]
            acc_val.append(val_to_add)
            #enter 0 for weighted value since we sold position
            weighted_avg.append(0)
            #restart current buys and positions 
            curr_buys = 0
            curr_position = 0
        #hold (either hold when in buy position or hold because stock is growing and we cannot sell any shares out of position)
        else:
            #curr_buys and positions are the same
            buy.append(0)
            sell.append(0)
            #calculate account value
            val_to_add = (df['close_price'][i] - df['close_price'][i-1]) * (curr_position)
            val_to_add = val_to_add + acc_val[i-1]
            acc_val.append(val_to_add)
            #append same weighted average
            weighted_avg.append(weighted_avg[i-1])

    #add values to dataframe
    df['buy'] = buy
    df['sell'] = sell
    df['account_value'] = acc_val
    df['weighted_avg'] = weighted_avg
    df.to_csv('backtested_{}.csv'.format(ticker))
    
if __name__ == "__main__":
    df = pd.read_csv('{}_day_data.csv'.format(ticker))
    df = df.drop(columns=['Unnamed: 0', 'symbol', 'session', 'interpolated'], axis=1)
    walk_theory_backtest(df)
