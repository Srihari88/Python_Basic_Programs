"""
- if the condition true if block executed.
- if the condition false else block executed.

Syntax:

if(condition):
    Statement(s)
else :
    statement(s)
"""

# Example-1

a = 10
if (a > 10):
    print("if body")
else:
    print("else body")

# Example-2: In python (1=true), (0=False)


if (1):
    print("Hello Sri")
else:
    print("Welcome Sri")

# Example-3
if (False):
    print("true body")
else:
    print("false body")

# Example-4: To find the entered year is leaf year or not?

year = int(input("Enter a year: "))

if (year % 4 == 0):
    print("Leaf year")
else:
    print("Not a leaf year")

# Write a program to enter numer is Even number

Number = int(input("Enter a Number: "))

if (Number % 2 == 0):
    print("Number is Even number")
else:
    print(" Odd Number ")
