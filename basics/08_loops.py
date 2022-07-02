# For loop
primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)

# 0 - 4
for x in range(5):
    print(x)

# 3-5
for x in range(3, 6):
    print(x)

# 3, 5, 7
for x in range(3, 8, 2):
    print(x)

# While loop
count = 0
while count < 5:
    print(count)
    count += 1

# Break and continue statements
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

# Else clause for loops
count = 0
while(count < 5):
    print(count)
    count += 1
else:
    print("count value reached %d" % (count))

for i in range(1, 10):
    if(i % 5 == 0):
        break
    print(i)
else:
    print("This is not printed because for loop is terminated because of break but not due to fail in condition")
