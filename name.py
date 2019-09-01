

#------------- If name is less than 3 character long print it must 3 character -------------#

name = input("Enter your name : ")

if len(name) < 3:
    print("Name must be 3 chracters ")
elif len(name) > 50:
    print("Name can be maximum 50 Character ")
else:
    print(" Name Looks Good ! ")
