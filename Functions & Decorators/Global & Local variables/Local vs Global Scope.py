
count = 0


def show_local():
    count = 10
    print("Local count:", count)

show_local()

print("Global count:", count)

'''
Local count: 10
Global count: 0
'''
