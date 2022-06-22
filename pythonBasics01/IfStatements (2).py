# ask a user to enter their age. Check if they are over 18 or not

userAge = input("Please enter your age")
#check if the user is over 18
if int(userAge) >= 18:
    print("You are over 18")
else:
    print("You are under 18")


# Write a script to ask an end user for their exam result.
# The Script should display the corresponding Grade.
#  Fail: <50, Pass: 50-69, Merit: 70-89, Distinction: 90-100

examResult = int(input("Please enter your exam result"))

if examResult >= 50 and examResult <= 69:
    print("You passed")

elif examResult >= 70 and examResult <= 89:
    print("You achieved Merit")

elif examResult >= 90 and examResult <= 100:
    print("You achieved Distinction")

else:
    print("You Failed")