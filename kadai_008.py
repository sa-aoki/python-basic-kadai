import random

var = random.randint(0,30)

print(var)


if var % 3 == 0 and var % 5 != 0 :
    print("Fizz")

elif var % 5 == 0 and var % 3 != 0:
    print("Bazz")

elif var % 3 == 0 and var % 5 == 0:
    print("FizzBazz")

else: 
    print(var)

    