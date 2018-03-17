stocks = {
    'GOOG': 434,
    'AAPL': 325,
    'FB': 54,
    'AMZN': 623,
    'F': 32,
    'MSFT': 549
}

print(min(stocks)) # prints AAPL, prints the minimum key

# (434, 'GOOG') (325, 'AAPL') -- kind of what we want with zip
min_price = min(zip(stocks.values(), stocks.keys()))

# min value now prints (32, 'F')
print(min_price)
