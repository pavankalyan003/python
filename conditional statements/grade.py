#Write a program that takes a student's marks and prints the grade using if-elif-else (A:90,
#B: 75–89, C: 60–74, D: 40–59, F: below 40)
marks = float(input("Enter student's marks: "))

if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 40:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)

#Enter student's marks: 92
#Grade: A
