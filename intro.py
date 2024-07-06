import random as rnd, math

# create function
def showMessage():
    # interact with user
    login = input("enter your login: ")
    print("Hello dear: ", login, "!")

# function with parameters
def showNumbers(koef, start, end):
    for n in range(start, end):
        if n % koef == 0:
            print(n)
    print("-" * 30)

showNumbers(9, 0, 100)
showNumbers(10, 100, 200)
showNumbers(22, 200, 300)
showNumbers(50, 0, 100)

# call function
#showMessage()

print(math.pow(2, 16))

# 2 bytes = 16 bits
# 4 bytes = 32 bits

marks = [12, 10, 9.5, 7, 11, 12]
prices = [120, 3400, 999, 120]

# TASK: create func that increment array items
def incrementItems(koef, list):
    for index in range(len(list)):
        list[index] += koef

print("Original: ", marks)
incrementItems(-2, marks)
print("Changed: ", marks)

print("-=-" * 10)

print("Original: ", prices)
incrementItems(-2, prices)
print("Changed: ", prices)
