"""
- A string is a list of characters in order enclosed by single quote or double quote.
- Python string is immutable modifications are not allowed once it is created.
- String index starts from 0, trying to access character out of index range will generate IndexError.
- In python it is not possible to add any two different data types, possible to add only same data
type data.

"""

s = 'Hello'

print(len(s))

# String follows forward and backward indexing
# Forward Indexing
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])

# Backward Indexing
print(s[-0])
print(s[-1])
print(s[-2])
print(s[-3])
print(s[-4])

# String slicing
print(s[1:4])
print(s[1:3])
print(s[1:2])
print(s[1:5])

print(s.find('Z'))
print(s.rfind('H'))
print(s.index('H'))
print(s.join("Sri"))
print(s.lower())
print(s.upper())
print(s.title())
print(s.strip())
print(s.replace('H', 'S'))
sri = "Hello Champs.!! what's going on"
print(s.split('H'))
print(sri.split('what'))
print(sri.splitlines())
