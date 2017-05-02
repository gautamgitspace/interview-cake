"""
	*******************************************************************************************
	Suppose we could access yesterday's stock prices as an array, where:
	- The indices are the time in minutes past trade opening time, which was 9:30am local time.
	- The values are the price in dollars of Apple stock at that time.

	For example, if the stock cost $500 at 10:30am, stock_prices_yesterday[60] = 500.
	Write an efficient function that takes stock_prices_yesterday and returns the
    best profit I could have made from 1 purchase and 1 sale of 1 Apple stock yesterday.
    *******************************************************************************************
"""

#Solved using brute force approach element by element comparison
#using two loops to compute min and max: O(n^2)

def best_profit(stock_prices_yesterday):
    max_profit = 0
    for outer in xrange(len(stock_prices_yesterday)):

        for inner in xrange(len(stock_prices_yesterday)):

            before = min(outer, inner)
            after   = max(outer, inner)

            before_price = stock_prices_yesterday[before]
            after_price   = stock_prices_yesterday[after]

            could_be_profit = after_price - before_price

            max_profit = max(max_profit, could_be_profit)

    return max_profit

stock_prices_yesterday = [10,20,30,5,35,3,2]
result = best_profit(stock_prices_yesterday)
print result
