import random

NUMBER_COUNT = 2

print("Nicholas Wilson")

sum = 0
for x in range(NUMBER_COUNT):
    x = random.randint(0,101)
    sum += x
    print(x)


print("Sum = ", sum)
print("Average = ", sum/NUMBER_COUNT)
