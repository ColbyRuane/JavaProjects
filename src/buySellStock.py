# 121. best time to buy and sell stock

# given an array 'prices' where prices[i] is the price of a given stock on the ith day
# maximize your profit by choosing a single day to buy one stock and choosing a 
# different day in the FUTURE to sell that stock

# return the maximum profit you can achieve from this transaction. if you cannot achieve any profit,
# return 0

# understand:
#   input: 'prices' array of integers
#   output: 'maximum profit' integer
# constraints:
#   'prices' array length of at least 1
#   prices[i] is a positive integer

# approach:
#   determine all pairs of integers in the array in which a profit can be made. if none, return 0
#   evaluate the pair of integers that provide the maximum profit
# edge-cases:
#   - array length of only one. cannot buy and sell in one day
#   - array of decreasing integers. impossible to profit

def bruteForce(prices: list[int]) -> int:
    length = len(prices)
    max = 0
    # less than 2 prices edge case
    if length <= 1:
        return 0

    descending = True
    for i in range(length):
        for j in range(length):
            # do not compare same index 
            # do not compare indices with negative profit
            # do not compare past days
            if i < j and prices[i] < prices[j]:
                difference = prices[j] - prices[i]
                if difference > max:
                    max = difference
        if descending: return 0
    return max
# Time Limit Exceeded!

def maxProfit1(prices: list[int]) -> int:
    # invalid list length edge case
    length = len(prices)
    if length <= 1:
        return 0
    
    # initialize global max count and pointers
    maxProfit = 0
    left, right = 0, 1

    # boundary condition for sliding window
    while right < length:
        # check if profit can be made
        if prices[left] < prices[right]:
            # check whether to update max profit
            maxProfit = max(maxProfit, prices[right] - prices[left])
        # profit cannot be made
        # cheaper day to buy stock, update left pointer
        else:
            left = right
        right += 1
    return maxProfit
# time-complexity = O(N) corresponding to complete list traversal
# space-complexity = O(1) corresponding to auxiliary data (pointers)

def maxProfit2(prices: list[int]) -> int:
    # auxiliary variables to store maximum profit and cheapest day to buy
    maxProfit = float('-inf')
    minPrice = float('inf')

    # invalid array edge case
    if len(prices) <= 1: return 0

    for price in prices:
        # update minimum price if possible
        if price < minPrice:
            minPrice = price
        
        # evaluate current maximum profit
        # (profit remains at 0 for decreasing prices)
        profit = price - minPrice
        maxProfit = max(profit, maxProfit)
    return maxProfit


# test-cases
prices = [7, 1, 5, 3, 6, 4]
print(f'max profit of {maxProfit2(prices)}')