def calculate_price(price, tax_rate=18, discount=0):
    tax = price * tax_rate / 100
    final_price = price + tax - discount
    return final_price


# Only price
print("Price only:", calculate_price(1000))

# Price and custom tax rate
print("Price and tax:", calculate_price(1000, 10))

# All arguments
print("All arguments:", calculate_price(1000, 10, 100))

'''
Price only: 1180.0
Price and tax: 1100.0
All arguments: 1000.0
'''
