#lists
a = [3, 5, 7, "jatin", True, 45, 66, 87, 78,99]
print(a)
print(len(a))
print(type(a))

print(a[-3])
print(a[len(a)-3])
print(a[5-3])
print(a[2])

if 7 in a:
    print("yes")
else:
    print("no")

if "tin" in "Jatin":
    print("yess")

print(a)
print(a[1: -1])
print(a[1:8:2])

#list comprehension
lst = [i*i for i in range(20)]
print(lst)

lst = [i*i for i in range(20) if i%2==0]
print(lst)


#list methods
a = [1,6,36,6,787,4,34,3,54,56,51,31,21,323]
print(a)
a.append(45)
print(a)
a.sort()
print(a)
a.sort(reverse=True)
print(a)
a.reverse()
print(a)
print(a.index(4))
print(a.count(6))

b = a.copy()
b[0]=0
print(a)

a.insert(1,900)
print(a)

m = [677,899,222]
k = a + m
print(k)
a.extend(m)
print(a)



#tuples
tup = (1,4,7,54,23,2,45,888,65,4,32,3)
print(type(tup), tup)

countries = ("spain", "india", "italy", "england", "germany")
temp= list(countries)
temp.append("russia")      #add item
temp.pop(3)                #remove item
temp[2]="finland"          #change item
countries=tuple(temp)
print(countries)


#f-string
letter="hey my name is {1} and i am from {0}"
country="india"
name="jatin"
print(letter.format(country, name))

print(f"hey my name is {name} and i am from {country}")

price = 47.9927332
txt = f"for only {price:.2f} dollars"
print(txt)