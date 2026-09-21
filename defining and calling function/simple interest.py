def simple_interest(principal, rate, time):

    si = (principal * rate * time) / 100
    return si

p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))

result = simple_interest(p, r, t)

print("Simple Interest:", result)


'''
Enter principal: 10000
Enter rate: 2
Enter time: 12
Simple Interest: 2400.0
'''
