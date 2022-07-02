class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class")


my_object_x = MyClass()
my_object_y = MyClass()

my_object_x.variable = "yackity"

print(my_object_x.variable)
print(my_object_y.variable)

my_object_x.function()
my_object_y.function()


class NumberHolder:
    # init() function
    def __init__(self, number):
        self.number = number

    def return_number(self):
        return self.number


"""
The __init__() function is a special function that is called when the class is being initialized. It's used for asigning
in a class.
"""
var = NumberHolder(7)
print(var.return_number())
