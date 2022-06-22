# Creating and using functions within Python
# Create a function to display your name on the console

def printMyName(name1):
    print(name1)

# Call the function printMyName
printMyName("Sarah Narayamy")
printMyName("Paula Oehme")
printMyName("Gabrielle Patricia")
printMyName("Luis Schneider")

# Create a function that takes 3 arguments.
# The first two arguments are integer numbers
# The third argument is a mathematical operator
# The mathematical operation should be performed on the first
# two arguments


def mathematicalOperation(number1, number2, operator):
    if operator == '+':
        print("The result is:", number1+number2)

    elif operator == '-':
        print("The result is:", number1-number2)

    elif operator == '*':
        print("The result is:", number1*number2)

    elif operator == '/':
        print("The result is:", number1/number2)


mathematicalOperation(9, 5, '-')

