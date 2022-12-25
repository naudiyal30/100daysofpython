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

