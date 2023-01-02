#DocStrings
def square(n):
     '''Takes in a number n, returns the square of n'''
     print(n**2)
square(5)
print(square.__doc__)


#Recursion
def factorial(n):
     if(n==0 or n==1):
          return 1
     else:
          return n * factorial(n-1)
print(factorial(5))

def fibonacci(num):
  if (num ==0):
    return 0
  elif num ==1:
    return 1
  else:
   return fibonacci(num-1) +  fibonacci(num-2)
print(fibonacci(7))


#Sets
s = {2, 4, 2, 6}
print(s)

info = {"Carla", 19, False, 5.9, 19}
print(info)

jatin = set()
print(type(jatin))

for value in info:
  print(value)


#Sets methods
s1 = {1,2,5,6}
s2 = {3,6,7}
print(s1.union(s2))
print(s1.intersection(s2))
s1.update(s2)
print(s1, s2)


#Dictionaries
dic = {
  "Jatin": "Human",
  "Spoon": "Object"
}
print(dic["Jatin"])

dic1 = {
  567: "Jatin",
  876: "Ram",
  665: "Shyam",
  234: "Karan"
}
print(dic1[234])

info = {'Name': 'Jatin', 'Age': 25, 'Eligible':True}
print(info)
print(info['Name'])         #throws an error when name is not exist
print(info.get('Eligible'))     #throws an null value when name is not exist

print(info.keys())
print(info.values())

for key in info.keys():
  print(f"The value corresponding to the key {key} is {info[key]}")


#Dictionaries Methods
ep1 = {122: 45, 123: 89, 567: 69, 670: 76}
ep2 = {222: 67, 566: 90}
ep1.update(ep2)
print(ep1)
empty={}
print(empty)
ep1.pop(122)
ep1.popitem()
print(ep1)