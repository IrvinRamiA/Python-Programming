phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
print(phonebook)

# Another notation
phonebook = {
    "John": 938477566,
    "Jack": 938377264,
    "Jill": 947662781
}
print(phonebook)

# Iterating over dictionaries
phonebook = {"John": 938477566, "Jack": 938377264, "Jill": 947662781}
for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))

# Removing a value
phonebook = {
    "John": 938477566,
    "Jack": 938377264,
    "Jill": 947662781
}
del phonebook["John"]
print(phonebook)

# or
phonebook = {
    "John": 938477566,
    "Jack": 938377264,
    "Jill": 947662781
}
phonebook.pop("John")
print(phonebook)
