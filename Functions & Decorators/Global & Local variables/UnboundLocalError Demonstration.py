'''
counter = 10

def change_counter():
    counter = counter + 1
    print(counter)

change_counter()

UnboundLocalError: cannot access local variable 'counter' where it is not associated with a value
'''

counter = 10

def change_counter():
    global counter
    counter = counter + 1
    print(counter)

change_counter()

'''
11
'''
