
nested = [[1, 2], [3, 4, 5], [6, 7]]

# to access the number 5
print(nested[1][2])   # constant time complexity because jumping directly to memory address

words = ["PHP", "Exercises", "Backend", "Python"]
longest = max(words, key = len)
print(longest)
# If two words have the same maximum length, Python’s max() will return the one that appeared first in the list.

sample_list = [10, 20, 30, 10, 40, 10, 50]
target = 10
freq = sample_list.count(target)   # O(n) TC
print(f"No. of times {target} occurs in sample_list is {freq}")

cleaned_list = [x for x in sample_list if x!= target]
print(cleaned_list)