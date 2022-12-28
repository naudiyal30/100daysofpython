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
