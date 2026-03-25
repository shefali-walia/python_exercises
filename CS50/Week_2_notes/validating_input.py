#infinite loop to keep asking for n until a non-negative number is entered
"""
while True: 
    n = int(input("What's n? "))
    if n < 0:
        continue  #continues asling for n if user keeps inputting negative no. 
    else:
        break  #breaks out of the most recently begun while loop if user inputs a non-negative no.
"""
# shorter loop:
while True: 
    n = int(input("What's n? "))
    if n > 0:
        break

# rest of the code:
for _ in range(n):
    print("meow")

"""same thing using functions: 
def main():
    number = get_number() # but get_number and meow not defined yet
    meow (3)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n  #can end while loop with return also if we want to return a value from the function (instead of break)
        
def meow(n):
    for _ in range(n):
        print("meow")
"""    