#Escape sequence character
print("how to win\nand influence \"people\"")


#More on Print statement
print("jatin", 89, 98, sep="~", end="naudiyal\n")
print("crazy guy")


#Variables
a = 56787      #integer
print(a)
b = "jatin"     #string
print(b)
c = True    #boolean type
print(c)
d = None   #none type
print(d)


print("type of a, b, c, d is", type(a), type(b), type(c), type(d))      #To print data types


list1 = [9, 3.4, [-5, 8], ["apple", "banana"]]      #list
print(list1)

tuple1 = (("parrot", "sparrow"), ("lion", "tiger"))        #tuple
print(tuple1)

dict1 = {"name":"jatin", "age":24, "canVote":True}      #dictonary
print(dict1)


#Operators
print(15+8)
print(15-8)
print(15*8)
print(15/8)
print(15//8)
print(15%8)
print(15**3)

#TypeCasting
a = "1"
b = "2"
print(int(a) + int(b))

str = "15"
num = 7
str_num = int(str)
sum = num + str_num
print("sum is", sum)

#Implicit  typecasting
c = 1.99
d = 9
print(c + d)


#User Input
# a = input("enter you name: ")
# print("my name is:", a)

# x = input("enter first number: ")
# y = input("enter second number: ")
# print (x + y)
# print (int(x) + int(y))


#Strings
name = "jatin"
friend = "rohan"
anotherFriend = "shreya"

apple = 'he said, "I want to eat an apple."'

str  = '''hi everyone,
have a nice day
Thankyou'''

print("hello " + name + friend)
print(apple)
print(str)

print(name[0])


print("lets use a for loop")
for character in name:
    print(character)


#String Slicing
names = "jatin,rohan,shreya"
print(names[0:8])
print(len(names))
fruit = "Mango"
mangoLen = len(fruit)
print(mangoLen)
print(fruit[0:4])
print(fruit[1:4])
print(fruit[:5])
print(fruit[0:-3])

#strings are immutable
a = "!!!!Jatin!!!!!!!!"
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("Jatin", "Shreya"))

blogHeading = "introduction tO jS"
print(blogHeading.capitalize())

str2 = "welcome to the console"
print(str2.center(50))
print(a.count('Jatin'))

str3 = "Welcome to the console"
print(str3.endswith("to", 4, 10))

str4 = "Hi my name is jatin and he is cooler than me"
print(str4.find("is"))
print(str3.isalnum())
