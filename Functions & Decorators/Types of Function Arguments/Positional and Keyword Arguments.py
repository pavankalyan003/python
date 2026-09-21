def student_info(name, roll_no, branch):
    print("Name:", name)
    print("Roll No:", roll_no)
    print("Branch:", branch)


# Positional arguments
print("Using Positional Arguments:")
student_info("kalyan", 101, "CSE")

# Keyword arguments
print("\nUsing Keyword Arguments:")
student_info(branch="CSE", name="kalyan", roll_no=101)


'''
Using Positional Arguments:
Name: kalyan
Roll No: 101
Branch: CSE

Using Keyword Arguments:
Name: kalyan
Roll No: 101
Branch: CSE
'''
