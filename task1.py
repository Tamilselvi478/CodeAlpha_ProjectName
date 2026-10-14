prices = {"AAPL": 180, "TSLA": 250, "GOOG": 150}

total = 0
n = int(input("Enter number of stocks: "))

for i in range(n):
    stock = input("Enter stock name: ").upper()
    qty = int(input("Enter quantity: "))

    if stock in prices:
        value = prices[stock] * qty
        total += value
        print(stock, "Investment:", value)
    else:
        print("Stock not found!")

print("Total Investment: $", total)

with open("portfolio.txt", "w") as f:
    f.write("Total Investment: $" + str(total))