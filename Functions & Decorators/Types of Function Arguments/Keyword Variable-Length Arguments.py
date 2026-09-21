def build_profile(**details):
    print("----- PROFILE -----")

    for key, value in details.items():
        print(key, ":", value)


build_profile(
    name="Vijay",
    age=20,
    city="Hyderabad",
    hobby="Coding"
)

print()

build_profile(
    name="Ravi",
    branch="CSE",
    college="GMRIT"
)


'''
----- PROFILE -----
name : Vijay
age : 20
city : Hyderabad
hobby : Coding

----- PROFILE -----
name : Ravi
branch : CSE
college : GMRIT
'''
