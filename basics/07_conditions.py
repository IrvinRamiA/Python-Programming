x = 2
print(x == 2)
print(x == 3)
print(x < 2)

# Boolean operators
name = "John"
age = 23

if name == "John" and age == 23:
    print("Your name is John and you are also 23 years old")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick")

# In operators
if name in ["John", "Rick"]:
    print("Your name is either John or Rick")

# If-else-if
statement = False
another_statement = True

if statement is True:
    pass
elif another_statement is True:
    pass
else:
    pass

# Is operator
"""
Unline the double equals operator "==", the "is" operator does not match the values of the variables, but the instances
themselves
"""
x = [1,2,3]
y = [1,2,3]
z = True
print(x == y)
print(x is y)
print(z is True)

# Not operator
print(not False)
print((not False) == False)
