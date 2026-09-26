numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Cubes using map()
cubes = list(map(lambda x: x ** 3, numbers))

# Numbers divisible by 3 using filter()
divisible = list(filter(lambda x: x % 3 == 0, numbers))

print("Original numbers:", numbers)
print("Cubes:", cubes)
print("Numbers divisible by 3:", divisible)


'''
Original numbers: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Cubes: [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
Numbers divisible by 3: [3, 6, 9]
'''
