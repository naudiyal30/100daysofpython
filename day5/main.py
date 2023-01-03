#for loop with else statement
for i in range(5):
    print(i)
else:
    print("Sorry no i")


for i in range(6):
    print(i)
    if i==4:
        break
else:
    print("Sorry no i")


i = 0
while i<7:
    print(i)
    i = i+ 1
    if i==4:
        break
else:
    print("Sorry no i")


#Exceptional Handling
a =input("Enter the number: ")
print(f"Multiplication table of {a} is:")

try:
    for i in range (1, 11):
        print(f"{int(a)} X {i} = {int(a)*i}")

except:
    print("Invalid Input!")

print("Some imp lines of codes")
print("End of program")


try:
    num=int(input("Enter an integer: \n"))
    a =[6, 3]
    print(a[num])

except ValueError:
    print("Number entered is not an integer")

except IndexError:
    print("Index Error")