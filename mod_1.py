print("This is mod_1's name ->", __name__)


def amazing_sum(number1,number2):
    return int(number1) + int(number2)

def demo_amazing_sum():
    print("Welcome to the amazing sum DEMO!")
    number1 = int(input("What is your first number? "))
    number2 = int(input("What is your second number? "))
    print(amazing_sum(number1, number2))


if __name__ == '__main__':
    demo_amazing_sum()
    print("We are running this file directly")
else:
    print('This file was called/imported from somewhere')