grade = lambda marks: "Pass" if marks >= 40 else "Fail"


marks = [35, 45, 67, 28, 90, 39]

for m in marks:
    print(m, ":", grade(m))

'''
35 : Fail
45 : Pass
67 : Pass
28 : Fail
90 : Pass
39 : Fail
'''
