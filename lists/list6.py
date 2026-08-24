#Given a list of 10 numbers, print the first 3 elements, the last 3 elements, and every alternate element using slicing.
numbers=[1,2,3,4,5,6,7,8,9,10]
print("first 3 elements:",numbers[:3])
print("last 3 elements:",numbers[-3:])
print("alternate elements:",numbers[::2])



#output:
#first 3 elements: [1, 2, 3]
#last 3 elements: [8, 9, 10]
#alternate elements: [1, 3, 5, 7, 9]
