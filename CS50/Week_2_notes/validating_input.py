#infinite loop to keep asking for n until a non-negative number is entered
while True: 
    n = int(input("What's n? "))
    if n < 0:
        continue  #continues asling for n if user keeps inputting negative no. 
    else:
        break  #breaks out of the most recently begun while loop if user inputs a non-negative no.

# # shorter way:
# while True: 
#     n = int(input("What's n? "))
#     if n > 0:
#         break

# rest of the code:
for _ in range(n):
    print("meow")
