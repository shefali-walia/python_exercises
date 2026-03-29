WORDS = {"PAIR": 4, "HAIR": 4, "CHAIR": 5, "GRAPHIC": 7}

def main():
    print("Welcome to spelling bee!")
    print("Your letters are: A I P C R H G")

    while len(WORDS) > 0:
        print(f"{len(WORDS)} words left!")
        guess = input("Guess a word: ")

        if guess == "GRAPHIC":
            WORDS.clear() #clear removes all key-value pairs from the dictionary, so the length of WORDS becomes 0 and the while loop ends
            print("You've won!")
        if guess in WORDS.keys():
            points = WORDS.pop(guess) #pop gives the key-value for guess and then removes it from the dictionary
            print(f"Good Job! You scored {points} points.")
    
    print("That's the game!")
main()


# def main():
#     print("Welcome to spelling bee!")
#     for word, points in WORDS.items(): #its like saying keys, values in WORDS
#         prinnt(f"{word} is worth {points} points.")

