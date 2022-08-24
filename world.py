my_list = ["1", "2", "3", "4", "5", "a", "b", "c", "d"]
my_list.sort(reverse=True)
print(my_list)
print(type(my_list))


my_list = ["1", "2", "3", "4", "5", "a", "b", "c", "d"]
my_list.sort(reverse=True)
print(len(my_list))

#list[]
#tuple()
#sets{}

#changing from tuple to list
#y = ("apple", "banana", "cherry")
#d = list(y)
#d[1] = "kiwi"
#y = tuple(d)
#print(d)

x = ("fish", "rice", "flower")

y = ("mango", 2, "orange", 5, 30.3)
print(y)

my_tuple = (28, 83, 93, 37, 23)


thisset = {"fish", "fish", "orange"}
tropical = {"yam", "ham"}
thisset.add("Banana")
thisset.update(tropical)
print(thisset)


myset = {"rice", "jam"}
yourset = {"abacha"}
set3 = myset.union(yourset)
print(set3)


aset = {"rice", "jam"}
Aset = {"rice"}

aset.difference_update(Aset)
print(aset)

f = {"hello", "mello", "indaboski"}
g = {"hello", "kite" "bello"}

z = f.difference(g)
print(z)

def my_function():
   print("hello world")
   
my_function()

#using function parameters

def my_func(fname):
    print(fname + " Summer class")
    
my_func("Seelva")




def my_func(x):
    return 5 * x
print(my_func(3))
print(my_func(10))

cars  = ["Bmw", "Mitshibushi", "Tesla"]
cars[1] = "Hummer"
cars.append("Mooncar")
print(cars)

