#syntax error - must be fixed by you
#value error - when the input is of the wrong data type, like trying to convert a string to an integer

def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True: #so that it keeps asking for x until the user gives an integer 
        try:
            return int(input("What's x? "))  #can just use return instead of assigning to x and then returning x and just remove else 
        except ValueError:
            print("x is not an integer")  #or just pass to ignore the error and do nothing and continue asking for x
        #else:
            #return x 

main()

#can put many except blocks to catch different types of errors
#name error - when you try to use a variable that doesn't exist
#memory error - when you try to use more memory than is available