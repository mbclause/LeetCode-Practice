"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a 
different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.


corner cases: array can't be empty, 
example two where the array is sorted in non increasing order

we definitely covered this algorithm in class, I can't remember it though. it's not dynamic programming, but I remember greedy
algorithms don't work. 

Brute force: for each x in prices (except for last element), loop through the remaining elements and store profit in array P,
return max(P)


def buySell(prices):
    let P be a new empty list

    for i in range(0, len(prices) - 1):
        for j in range(i + 1, len(prices)):
            P.add(prices[j] - prices[i])

    return max(P)

O(n^2) time
O(n) space
"""

def maxProfit(prices):
    P = []

    m = 0

    for i in range(0, len(prices) - 1):
        for j in range(i + 1, len(prices)):
            P.append(prices[j] - prices[i])

    if(len(P) > 0):
        m = max(P)

    if m < 0:
        m = 0

    return m


prices = [1, 2]

print(maxProfit(prices))



"""
improved algorithm: bottleneck is inner for loop, if greedy won't work, how do you find max profit without 
iterating through each possibility?

was it a randomized algorithm? you can't sort because the order matters

turns out the best algorithm uses dynamic programming principles

def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0
    
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    
    return max_profit
"""