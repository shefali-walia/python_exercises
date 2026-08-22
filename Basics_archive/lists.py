mylist = ['banana', 'cherry', 'apple']
print(mylist)

mylist.append('lemon')
print(mylist)

mylist.insert(1, 'blueberry')
print(mylist)

item = mylist.pop()
print(item)
print(mylist)

# This assigns the return value (None) to item so output is none
# item = mylist.remove("cherry")
# print(item)

# This prints the return value of the method call
# print(mylist.remove("cherry"))  # Output: None

# so either just remove first then print modified list 
# or if u need the removed item use .pop to assign it to a variable

# mylist.clear() - to empty list

#  mylist.reverse()

mylist.sort()  # sorts in place (changes original list) in asc order
print(mylist)

# to not change original list and create a new sorted list use sorted 
newlist = sorted(mylist)
print(newlist)


nolist = [0]*5   # creates a list with 5 zeroes as elements
print(nolist)

mylist2 = [1,2,3,4,5]
new_list = mylist + mylist2
print(new_list)

# slicing
mylist = [1,2,3,4,5,6,7,8,9]

a = mylist[::2]
print(a)

# copying
list_org = ['banana', 'cherry', 'apple']
list_cpy = list_org   # modifying copy will also modify orginial list
# because using assignment operator = means both lists refer to same location in memory

list_cpy.append('lemon')
print(list_cpy)
print(list_org)

# to make actual copy use .copy method
list_cpy = list_org.copy()
list_cpy.append('watermelon')
print(list_cpy)
print(list_org)

# can also make actual copy by slicing
list_cpy = list_org[:]  # using just colon means from start to end
list_cpy.append('booze')
print(list_cpy)
print(list_org)

# list comprehension - create new list with existing list with one line
a = [1,2,3,4,5,6]
b = [i*i for i in a]  # create list of squares
print(a)
print(b)