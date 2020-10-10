#function for calculate two numbers
def calculator():
    num1 = float(input("Enter first number: ")) #user input the first number
    op = input("Enter Operator: ") #user input the operator that are +,-,* or /
    num2 = float(input("Enter second number: ")) #user input the second number
    #if else statment for what kind of operator user choosed
    if op == "+":
        return num1+num2
    elif op == "-":
        return num1-num2
    elif op == "*":
        return num1*num2
    elif op == "/":
        return num1/num2
    else:
        return "Invalid Operator!"
#call function that print the result
print(calculator()) 