## Simeon Patton
## 


def calc(a, b):
    sum = a + b
    f"The sum of {a} + {b} is {sum}."
    ##print(sum)

    difference = a - b
    print(difference)

    multiplication = a * b
    print(multiplication)

    divide = a / b
    print(divide)

    FinalValues = [sum, difference, multiplication, divide]
    print(FinalValues)

    SumOfList = FinalValues[0] + FinalValues[1] + FinalValues[2] + FinalValues[3]
    print(SumOfList)

def a_input():
    a = input("Please enter a number 'a': ")
    a = int(a)
    print("")
    return int(a)

def b_input():
    b = input("Please enter a number 'b': ")
    print("")
    b = int(b)
    return int(b)


a = a_input()
b = b_input()
calc(a,b)
print("")