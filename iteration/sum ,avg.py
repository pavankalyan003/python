#Write a program to find the sum and average of digits of a given number using a while loop.
number = 12345
original_number = abs(number)
temp = original_number
total_sum = 0
count = 0

while temp > 0:
    digit = temp % 10
    total_sum += digit
    count += 1
    temp //= 10

average = total_sum / count if count > 0 else 0

print(f"Number: {original_number}")
print(f"Sum of digits: {total_sum}")
print(f"Average of digits: {average}")
