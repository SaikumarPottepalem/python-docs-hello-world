# Python program to make a simple calculator Anjinkaya

# take inputs
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# choose operation
print("Operation: +, -, *, /")
select = input("Select operations: ")

# check operations and display result
# add (+) two numbers
if select == "+":
    print(num1, "+", num2, "=", num1+num2)
# subtract (-) two numbers
elif select == "-":
    print(num1, "-", num2, "=", num1-num2)
# multiply (*) two numbers
elif select == "*":
    print(num1, "*", num2, "=", num1*num2)
# divide (/) two numbers
elif select == "/":
    print(num1, "/", num2, "=", num1/num2)
else:
    print("Invalid input")
