# Tuples: ordered, immutable, allows duplicate elements
# cannot be changed after creating, used for objects that belong together

mytuple = ('Max', 28, 'Boston')  # () are optional
print(mytuple)

# if we write single item in quotes or even in () it is not recognised at tuple, it is recognised at string
# so put a comma at the end to be recognised as tuple
# oor use tuple fnct. to create a tuple

mytuple = 'Max',
print(type(mytuple))

mytuple = tuple(['Max', 28, 'Boston']) # tuple from iterable list
print(mytuple)

item = mytuple[-2]
print(item)

# mytuple[0] = 'Tim'  # typeerror - tuple object does not support item assignment
# because immutable

for i in mytuple:
    print(i)

if 'Max' in mytuple:
    print('Yes')
else:
    print("No")

my_tuple = ('a', 'p', 'p', 'l', 'e')
print(len(my_tuple))
print(my_tuple.count('p'))
print(my_tuple.index('p')) # first instance index

my_list = list(my_tuple)
print(my_list)

my_tuple2 = tuple(my_list)
print(my_tuple2)

# slicing
a = (1,2,3,4,5,6,7,8,9,10)

b = a[2:5]  # last index exclusive
print(b)

b = a[::-1] # reverse tuple
print(b)

# splitting elements
mytuple = 'Max', 28, 'Boston'

name, age, city = mytuple
print(name)
print(age)
print(city)

tuple3 = (0,1,2,3,4)
i1, *i2, i3 = tuple3  # use * to group multiple elements
print(i1)
print(i2)  # list now
print(i3)

# list is larger than tuple memory wise even with same elements
# tuples can be more efficient and faster if immutable is okay