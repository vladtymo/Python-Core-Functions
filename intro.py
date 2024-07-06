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

marks = [12, 10, 9.5, 11, 12, 12, 12, 12, 12]
prices = [120, 3400, 999, 120]

# TASK: create func that increment array items
def incrementItems(koef, list):
    for index in range(len(list)):
        list[index] += koef

# print("Original: ", marks)
# incrementItems(-2, marks)
# print("Changed: ", marks)

print("-=-" * 10)

print("Original: ", prices)
incrementItems(-2, prices)
print("Changed: ", prices)

# TASK: show horizontal line with length, symbol
def showLine(len, symbol):
    print(symbol * len)
 
showLine(10, '@')
showLine(7, '*')

# l = int(input("enter line length: "))
# s = input("enter line filler: ")
# showLine(l, s)

showLine(rnd.randint(5, 20), "#")

# ----- func with return operator
def getAverage(list):
    return round(sum(list) / len(list), 1) 

def isGenius(marks):
    # if getAverage(marks) >= 10:
    #     return True
    # else:
    #     return False
    return getAverage(marks) >= 10

avg = getAverage(marks)

print("Student average mark: ", avg)

if isGenius(marks):
    print("Student is genius!")
else:
    print("Student is normal!")
