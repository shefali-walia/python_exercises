duplicates = [10, 20, 10, 30, 40, 40, 20, 50]

# Method to remove duplicates while preserving order
unique_list = list(dict.fromkeys(duplicates))

print(f"Unique List: {unique_list}")

# Unlike a standard set(), dict.fromkeys() preserves the order in which items first appeared 
# O(n) operation, making it significantly faster than using a loop to check if an item exists before adding it
# Converting a list to a set and back to a list is the quickest way to remove duplicates, though it might lose the original order. To keep the order, use dict.fromkeys()
# A set cannot contain duplicates