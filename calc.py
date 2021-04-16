## Simeon Patton
## 


def calc(a, b):
    sum = a + b
    print(sum)

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

a_input = input("Please enter a number 'a': ")
a_input = int(a_input)
print("")
b_input = input("Please enter a number 'b': ")
print("")
b_input = int(b_input)