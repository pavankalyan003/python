items = {
    "Laptop": 50000,
    "Mouse": 500,
    "Keyboard": 1500,
    "Monitor": 12000,
    "Headphones": 2000
}

sorted_items = sorted(
    items.items(),
    key=lambda x: x[1]
)

print("Items from cheapest to most expensive:")

for item, price in sorted_items:
    print(item, ":", price)


'''
Items from cheapest to most expensive:
Mouse : 500
Keyboard : 1500
Headphones : 2000
Monitor : 12000
Laptop : 50000
'''
