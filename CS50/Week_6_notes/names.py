# names = []
# for _ in range(3):
#     names.append(input("What's your name? "))

# for name in sorted(names):
#     print(f"hello, {name}")

name = input("What's your name? ")

with open("names.txt", "a") as file:  # opens file/ creates if not existing, w for write, a for append, r for read (read is default so no need to mention) 
    file.write(f"{name}\n") # add the name and new line

# file.close() - close n save file - not needed when using "with"

