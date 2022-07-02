my_list = []

my_list.append(1)
my_list.append(2)
my_list.append(3)
print(my_list[0])
print(my_list[1])
print(my_list[2])

for x in my_list:
    print(x)

# Accessing an index which does not exist generates an exception (an error)
# my_list = [1, 2, 3]
# print(my_list[10])
