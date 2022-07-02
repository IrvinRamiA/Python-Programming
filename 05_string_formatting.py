# Python can use C-style formatting to create new, formatted strings
name = "John"
print("Hello, %s" % name)

# To use two or more argument specifiers, use a tuple
name = "Charles"
age = 23
print("%s is %d years old" % (name, age))

# Any object which is not a string can be formatted using the %s operator as well
my_list = [1, 2, 3]
print("A list: %s" % my_list)

"""
Basic argument specifiers:
%s - String (or any object with a string representation, like numbers)
%d - Integers
%f - Floating point numbers
%.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot
%x/%X - Integers in hex representation (lowercase/uppercase)
"""
