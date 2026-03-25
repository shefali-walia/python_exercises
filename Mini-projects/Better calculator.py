
a = input ("Enter a number: ")
b = input ("Enter another number: ")
op = input ("Enter an operator: ")

if op == "+":
    result = float(a) + float(b)
elif op == "-":
    result = float(a) - float(b)
elif op == "*":
    result = float(a)*float(b)
elif op == "/" and b!= "0":
    result = float(a)/float(b)
elif op == "/" and b =="0":
    result = "Division by zero is not defined."
else:
    result = "Invalid operator"

print(result)

# could have just used float once while defining the variable like a = float(input(...)) and then after if statement just print (a+b) like that no need of a result variable