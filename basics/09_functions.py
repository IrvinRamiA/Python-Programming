def my_function():
    print("Hello from my_function")


def my_function_with_args(user_name, greeting):
    print("Hello, %s, from my_function, I wish you %s" % (user_name, greeting))


def sum_two_numbers(a, b):
    return a + b


my_function()
my_function_with_args("John Doe", "a great year!")
x = sum_two_numbers(1, 3)
print(x)
