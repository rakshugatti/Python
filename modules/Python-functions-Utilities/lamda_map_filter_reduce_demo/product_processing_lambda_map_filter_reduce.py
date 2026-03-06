from functools import reduce

products = []

# Number of products
n = int(input("Enter number of products: "))

# Taking n inputs
for i in range(n):
    name = input("Enter product name: ")
    price = float(input("Enter product price in USD: "))
    products.append((name, price))

print("\nProduct List:")
print(products)


# (a) Lambda: Sort products by price
sorted_products = sorted(products, key=lambda x: x[1])
print("\nProducts sorted by price:")
print(sorted_products)


# (b) map(): Convert USD to INR (1 USD = 83 INR)
prices_usd = [price for name, price in products]

prices_inr = list(map(lambda p: p * 83, prices_usd))
print("\nPrices converted to INR using map():")
print(prices_inr)


# (c) filter(): Products cheaper than $100
affordable_products = list(filter(lambda x: x[1] < 100, products))
print("\nAffordable products (price < $100):")
print(affordable_products)


# (d) reduce(): Total value of all products
total_price = reduce(lambda x, y: x + y, prices_usd)
print("\nTotal value of all products using reduce():")
print(total_price)


# (e) List Comprehension Equivalents

prices_inr_lc = [price * 83 for name, price in products]

affordable_lc = [product for product in products if product[1] < 100]

print("\nUsing List Comprehension:")
print("Prices in INR:", prices_inr_lc)
print("Affordable products:", affordable_lc)