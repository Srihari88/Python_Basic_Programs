"""Data types in Python
********Numbers******
 Int / float / complex: type
 Describes the numeric value & decimal value
 These are immutable modifications are not allowed.

******Boolean********
 bool: type
 represent True / Falsevalues.
 0 = False & 1 = True
 Logical operators and or not return value is Boolean
******Strings********
 str: type
 Represent group of characters
 Declared with in single or double or triple quotes
 It is immutable modifications are not allowed.
****Lists************
- list: type
- group of heterogeneous objects in sequence.
- This is mutable modifications are allowed
- Declared with in the square brackets[]
*****Tuples***********
 tuple: type
 group of heterogeneous objects in sequence
 this is immutable modifications are not allowed.
 Declared within the parenthesis()
 Sets
 set: type
 group of heterogeneous objects in unordered
 this is mutable modifications are allowed
 declared within brasses {}
 Dictionaries
 dict: type
 it stores the data in key value pairs format.
 Keys must be unique & value
 It is mutable modifications are allowed.
 Declared within the curly brasses
{key: value}

"""

print(bool(1))
print((bool(0)))
print(bool(False))
print(bool(True))

T, F = True, False
print("T: ", T, " F:", F)

print(T and F)
print(T or F)
print(T and T)
print(F or F)
print(F and T)
