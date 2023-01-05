#Finally Keyword
try:
    l = [1,3,5,6,7,8]
    i = int(input("Entert the index: "))
    print(l[i])
except:
    print("Some error occured ")
finally:
    print("I am always executed")

def func1():
    try:
        l = [1,3,5,6,7,8]
        i = int(input("Entert the index: "))
        print(l[i])
        return 1
    except:
        print("Some error occured ")
        return 0
    finally:
        print("I am always executed")
x = func1()
print(x)


#Custom Errors
a = int(input("Enter any value between 5 and 9: "))

if (a<5 or a>9):
    raise ValueError("Value should be between 5 and 9")

