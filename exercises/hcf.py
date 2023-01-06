#To find HCF of two numbers

num1 = int(input("Enter first number\n"))
num2 = int(input("Enter second number\n"))

if num1>num2:
    mn = num1
else:
    mn = num2

for i in range(1, mn+1):
    if num1%i==0 and num2%i==0:
        hcf = i

print(f"The HCF/GCD of these two numbers is {hcf}")