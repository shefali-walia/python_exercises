
list1 = [10, 20, 30, 40, 50]

for i in range(len(list1)-1, -1,-1):
    print(list1[i], end =" ")

print()
# Alternate method
for num in reversed(list1):
    print(num, end = " ")