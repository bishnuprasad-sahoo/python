

#---------- How to remove duplicate numbers from a list -------------#

numbers = [2, 2, 6, 9, 7, 1, 6, 1]
unique = []

for number in numbers:
    if number not in unique:
        unique.append(number)
print(unique)

