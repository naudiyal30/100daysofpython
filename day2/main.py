#if-else conditional
a = int(input("enter your age"))
print("your age is:", a)

if(a>18):
    print("you can drive")
else:
    print("you cannot drive")   


#elif conditional
num = int(input("enter any number"))
if(num<0):
    print("negative")
elif(num==0):
    print("zero")
else:
    print("positive")


#nested if statement
num = 3
if (num<0):
    print("negative")
elif (num>0):
    if(num<=10):
        print("between 1-10")
    elif (num>10 and num<=20):
        print("between 11-20")
    else:
        print("greater than 20")
else:
    print("zero")


#match-case
x = int(input("Enter the value of x: "))
# x is the variable to match
match x:
    # if x is 0
    case 0:
        print("x is zero")
    # case with if-condition
    case 4:
        print("case is 4")

    case _ if x!=90:
        print(x, "is not 90")
    case _ if x!=80:
        print(x, "is not 80")
    case _:
        print(x)

