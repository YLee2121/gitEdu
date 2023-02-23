from .operator import adition, minus, multiply, divide

STOP = 'stop'
ADD = '+'
MINUS = '-'
MULTIPLY = '*'
DIVIDE = '/'

def main():

    while True:
        
        print('stop for exit')
        num1 = input('Enter first number: ')
        if num1 == STOP:
            break
        num2 = input('Enter second number: ')
        operator = input('Enter operator: ')

        if operator == ADD:
            print("ans is: ", adition(num1, num2))
        elif operator == MINUS:
            print("ans is: ", minus(num1, num2))
        elif operator == MULTIPLY:
            print("ans is: ", multiply(num1, num2))
        elif operator == DIVIDE:
            print("ans is: ", divide(num1, num2))

        