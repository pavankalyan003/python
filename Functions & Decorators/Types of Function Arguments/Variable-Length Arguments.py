def total_marks(*marks):
    total = sum(marks)
    average = total / len(marks)
    return total, average


# 3 marks
total, average = total_marks(80, 70, 90)
print("3 Marks:")
print("Total:", total)
print("Average:", average)

# 5 marks
total, average = total_marks(80, 70, 90, 85, 75)
print("\n5 Marks:")
print("Total:", total)
print("Average:", average)

# 1 mark
total, average = total_marks(95)
print("\n1 Mark:")
print("Total:", total)
print("Average:", average)



'''
3 Marks:
Total: 240
Average: 80.0

5 Marks:
Total: 400
Average: 80.0

1 Mark:
Total: 95
Average: 95.0
'''
