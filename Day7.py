# Best time to buy and sell stock
def max_profit(prices):
    min_price = float('inf')
    max_profit = 0
    
    for price in prices:
        if price < min_price:
            min_price = price
        else:
            profit = price - min_price
            if profit > max_profit:
                max_profit = profit
    
    return max_profit

# Input from user
prices = list(map(int, input("Enter stock prices: ").split()))

result = max_profit(prices)

print("Maximum Profit:", result)