#functions
def calculateGmean(a, b):
    mean = (a*b)/(a+b)
    print(mean)   

def isGreater(a, b):
   if(a>b):
        print("first is greater")
   else:
        print("second is greater and equal") 

def isLesser(a,b):
    pass

a=6
b=8
isGreater(a,b)
calculateGmean(a, b)
c=40
d=12
isGreater(c,d)
calculateGmean(c, d)


#function arguments
def average(a,b):
    print("the average is ", (a+b)/2)
average(4,6)

def name(fname="jatin", mname="sharma", lname="naudiyal"):
    print("hello", fname, mname, lname)
name("shreya") 

def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum +i
    print("average is: ", sum /len(numbers))
average(5,6)

def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum +i
    return sum /len(numbers)
c = average(52,62)
print(c)
