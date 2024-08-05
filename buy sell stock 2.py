"""
so the difference is that you can buy and sell stock multiple times as you advance through prices. the normal algorithm won't work here, unless we do multiple passes through the array? I think we could do the normal algorithm once, then delete everything before the day we sold at? No because there could be a more optimal combo we could do. Brute force seems riduculously slow

corner cases: array sorted in non increasing order

array can't be empty, prices are non negative


could this be a dynamic programming problem? I think it is, it's very similar to the rod cutting problem, we need to come up with a recurrence, make the problem 1 smaller

does this problem have overlapping sub problems? I'm not sure, ok it does. this is a value problem

how do you make the problem one size smaller? 

buy on day i, sell on day k, buy on day k+1, sell on day j

recurrence relation:
r_i,j = max profit for buying on day i and selling on day j, where i <= j
base case, i = j so r_i,j = 0

r_i,j =max_i <= k <= j (r_i,k + r_k+1,j + p[k] - p[i] + p[j] - p[k+1])
"""


"""
turns out there's a way simpler approach using a greedy heuristic

def maxProfit(prices):
    max_profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            max_profit += prices[i] - prices[i - 1]
    return max_profit
"""