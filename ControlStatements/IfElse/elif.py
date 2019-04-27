"""
- The keyword ‘elif’ is short for ‘else if’
- An if ... elif ... elif ... sequence is a substitute for the switch or case statements found in other
languages


Syntax:
if expression:
    statement(s)
elif expression:
    statement(s)
elif expression:
    statement(s)
else:
    statement(s)

"""

# Example:

Number = 20

Guess = int(input("Guess a number"))

if Guess == Number:
    print("Congratulations..!!! You guessed correctly")
elif Guess > Number:
    print("Big number you entered")
else:
    print("Small number you entered")

# Example-2
x = int(input("Please enter an integer: "))
if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")

# Example-3

x = int(input("Please enter an integer: "))
if x < 0:
    print("x is negative")
elif x % 2:
    print("x is positive and odd")
else:
    print("x is even and non-negative")
    print("process is done")
