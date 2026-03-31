#syntax error - must be fixed by you
#value error 

def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            return int(input("What's x? "))  #can just use return instead of assigning to x and then returning x and just remove else 
        except ValueError:
            print("x is not an integer")  #or just pass to ignore the error and do nothing and continue asking for x
        #else:
            #return x 

main()

  
#name error - when you try to use a variable that doesn't exist
