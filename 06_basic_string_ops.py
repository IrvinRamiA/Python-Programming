# String length
astring = "Hello World!"
print("Single quotes are ' '")
print(len(astring))

# Find index of a letter
print(astring.index("o"))

# Count occurrences of letters
print(astring.count("l"))

# String slices
print(astring[3:7])
print(astring[3:7:2])
print(astring[3:7:1])
print(astring[::-1])

# Uppercase and lowercase
print(astring.upper())
print(astring.lower())

# Starts with and ends with
print(astring.startswith("Hello"))
print(astring.endswith("asdfasdfasdf"))

afewwords = astring.split(" ")
print(afewwords)
