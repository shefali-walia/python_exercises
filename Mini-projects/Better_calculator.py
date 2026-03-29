a = float(input ("Enter a number: "))
b = float(input ("Enter another number: "))
op = input ("Enter an operator: ")

if op == "+":
    result = a + b
elif op == "-":
    result = a - b
elif op == "*":
    result = a * b
elif op == "/" and b!= "0":
    result = a / b
elif op == "/" and b =="0":
    result = "Division by zero is not defined."
else:
    result = "Invalid operator"

print(result)

