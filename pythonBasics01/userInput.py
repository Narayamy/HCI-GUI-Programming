# Reading in input from the end user

#userInput = ''

userInput1 = input("Please enter a value between 1 and 10")
print("You entered:", userInput1)
userInput2 = input("Please enter a value between 1 and 10")
print("You entered:", userInput2)

print("userInput1 plus userInput2 equals:", int(userInput1)+int(userInput2))

# Write a Python Script that continually asks the end user to enter a String.
# The user input is printed, and the while loop terminates when the user enters QUIT

userInput = ''

while userInput != 'quit':
    userInput = input("Please enter a string")
    print(userInput)