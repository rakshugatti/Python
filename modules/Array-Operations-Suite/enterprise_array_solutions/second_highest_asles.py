"""
 Sales Analytics - Second Highest Revenue
"""

def second_largest(sales):
    largest = -999999999
    second = -999999999

    for amount in sales:
        if amount > largest:
            second = largest
            largest = amount
        elif amount > second and amount != largest:
            second = amount

    if second == -999999999:
        return None

    return second


monthly_sales = [50000, 75000, 62000, 90000, 90000, 85000]

result = second_largest(monthly_sales)

if result is not None:
    print("Second Highest Sales:", result)
else:
    print("Not enough data")