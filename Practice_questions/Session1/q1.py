a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a*b <= 1000:
    ans = a*b
else:
    ans = a+b
print(ans)