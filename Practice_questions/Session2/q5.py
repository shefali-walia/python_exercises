num = 76542

while num !=0:
    last_digit = num%10
    print(last_digit, end = "")
    num = num//10

# Alternate
# num = 76542
# reverse_number = 0

# while num > 0:
#     digit = num % 10
#     reverse_number = (reverse_number * 10) + digit
#     num = num // 10
