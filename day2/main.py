# #if-else conditional
a = int(input("enter your age"))
print("your age is:", a)

if(a>18):
    print("you can drive")
else:
    print("you cannot drive")   


# #elif conditional
num = int(input("enter any number"))
if(num<0):
    print("negative")
elif(num==0):
    print("zero")
else:
    print("positive")


# #nested if statement
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


# #match-case
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

    
#for loop
name = "naudiyal"
for i in name:
    print(i)

colors = ["red", "blue", "green", "yellow"]
for color in colors:
    print(color)
    for i in color:
        print(i)

for k in range(30):
    print(k)

for j in range(2, 14, 3):
    print(j)


#while loop
i=0
while(i<=3):
    print(i)
    i = i+1

i=int(input("enter any number"))
while(i<=65):
    i=int(input("enter any number"))
    print(i)
    i = i+1

count = 10
while (count >0):
    print(count)
    count = count - 1
else:
    print("condition is untrue")


#break statement
for i in range(12):
    if(i==10):
        break
    print("5 X ", i+1, "=", 5*(i+1))

print("done")


 

