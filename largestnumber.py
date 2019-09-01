#------------- Find the largest number in a String/Array ---------------#

numbers = [10, 60, 5, 2, 90, 35]
max = numbers[0]

for number in numbers:
    if number > max:
        max = number
print(max)
