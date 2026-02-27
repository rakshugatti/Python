"""
 Product Price Lookup
"""

def binary_search(prices, target_price):
    left = 0
    right = len(prices) - 1

    while left <= right:
        mid = (left + right) // 2

        if prices[mid] == target_price:
            return mid
        elif prices[mid] < target_price:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# Sorted product prices
product_prices = [100, 200, 300, 400, 500, 600]

search_price = 400

result = binary_search(product_prices, search_price)

if result != -1:
    print("Product price found at index:", result)
else:
    print("Product price not found")