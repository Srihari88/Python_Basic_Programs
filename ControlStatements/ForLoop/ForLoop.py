""""
- Used to print the data n number of times based on conation.
- If you do need to iterate over a sequence of numbers,use the built-in function range().


syntax :
range() function :
range(10)
range(5, 10)
range(0, 10, 3)
range(-10, -100, -30)

Syntax:
for x in range(10):
for x in range(8,10):
for x in range(3,10,3):

for iterator_name in range(10): ...statements...
for iterator_name in range(start,end): ...statements...
for iterator_name in range(start,stop,increment): ...statements...

"""

for x in range(10):
    print("The values are...", x)

for x in range(5, 10):
    print("Second for loop are...", x)

for x in range(3, 10, 3):
    print("Third for loop...", x)

for x in range(-20, -10):
    print("Forth loop", x)

for x in range(-20, -10, 3):
    print("Fifth loop", x)

# for x in range(-100, -50, -15):
#     print("sixth loop", x)

for i in range(10, 0, -2):
    print(i)

for i in range(1, 5):
    print(i)
else:
    print('The for loop is over')

# case 1: if the exception raised in loop else block not executed.
for x in range(10):
    print("The values are: ", x)
    try:
        print(10 / 0)
    except:
        print("zero division error ")
    else:
        print(" End for loop")

else:
    print("else block")

# Write a program to print the sum of 1 to 100.
sum = 0
for i in range(1, 1000):
    sum = sum + i
print(sum)

# Write a program to print the even number from 1 to 100

for i in range(1, 100):
    if i % 2 == 0:
        print("Even Number", i)
    else:
        print("Odd Number", i)

# For loop with list data type

Fruits = ['apple', 'Goa', 'banana', 'Orange']

for fruit in Fruits:
    print(fruit, len(fruit))
