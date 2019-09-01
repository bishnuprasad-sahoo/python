######### How to calculate GCD of two number #################

def ComputeGCD(x,y):
    if(y==0):
        return x
    else:
        return ComputeGCD(y,x%y)

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print(ComputeGCD(num1,num2))
