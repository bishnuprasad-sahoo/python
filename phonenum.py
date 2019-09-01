

""" Wap to enter the digits and show them in character format using dictionary function """

phone = input("Enter Phone Number : ")

digits_mapping = {
    "0" : "zero",
    "1" : "one",
    "2" : "two",
    "3" : "three",
    "4" : "four",
    "5" : "five",
    "6" : "six",
    "7" : "seven",
    "8" : "eight",
    "9" : "nine"
}
output = ""
for number in phone:
    output += digits_mapping.get(number, "!") + " "
print(output)



