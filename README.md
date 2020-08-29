# Random Walk Theory Stock Strategy (Martingale Strategy)
This program is a twist on the Martingale gambling strategy. As the price of a stock
drops below the previous/current average stock price, it will append +2
buys from the previous position. This program has a cap at 9 buys which represent
25 total positions at once. While in positions, once the price of the stock
jumps above the average price of stock positions, it will sell all current holdings.

## Packages
* Pandas
* NumPy
* robin_stocks api (or yfinance... Read below if so)

## Example Results
 *date* | *close_price* | *buy* | *sell* | *account_value* | *weighted_avg*
 |------|---------------|-------|--------|-----------------|--------------|
 2017-04-11 | 235.06 | 1 | 0 | 10490.63 | 235.06 |
 2017-04-12 | 234.03| 3 | 0 | 10489.61 | 234.28 |
 2017-04-13 | 232.51 | 5 | 0 | 10485.05 | 233.29 |
 2017-04-17 | 234.57 | 0 | 9 | 10503.59 | 0.0 |
 First note: This dataset was recieved from the robin_stocks api, if you use 
 different library to retrieve data, then in the backtesting function you will 
 have to change a couple of the column names. <br />
 Replace 'close_price' column to whatever your close/adjusted close prices are. <br />
 Also, replace the dropped columns to whatever columns you don't need as part of 
 your dataset. 
 
### Analysis on Example Results
* This series in the dataset is a common occurrence when it comes to profiting
from this algorithm. Analyzing the data there are multiple occasions of this happening
* As you can see, the program enters the trade at a price of 235.06.
 As the price decreases, it appends 2 more buys to the previous buy.
* As the program price averages the stock price. It will sell all
positions once the price jumps above the average price. 
* Notice the that there was a profit of +$12 despite selling 
the stock nearly $.50 below the initial buy.
* The buy column represents to how many shares were bought near close. The sell represents how many shares were 
sold that day near close (all positions)

## Contact
 Phone: (971) 708-4444<br />
 Email: ericsanderson333@gmail.com<br />
 Linkedin: https://www.linkedin.com/in/ericanderson333 <br />
 Please contact me and send me any questions/advice! Thanks!
 
