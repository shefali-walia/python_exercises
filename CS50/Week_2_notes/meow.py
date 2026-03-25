#program to print "meow" 
# using while loop to print "meow"
i = 0  
while i < 3:
    print("meow") 
    i += 1

# use ctrl + c to stop the program in case of accidental infinite loop

#using for loop to print "meow"
for i in range(3):
    print("meow")

# can use _ as a variable (instead of i) when we don't need to use the variable anywhere else in the code
for _ in range(3):  
    print("meow")

# using string multiplication 
print("meow\n"*3, end="")  # using end="" to avoid adding an extra newline at the end

