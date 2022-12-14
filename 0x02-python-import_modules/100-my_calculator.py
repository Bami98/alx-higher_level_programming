#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div 
    from sys import argv, exit
        
    if len(argv) - 1 != 3:
        print(f'Usage: ./{argv[0]} <a> <operator> <b>')
        exit(1)
    
    num1 = int(argv[1])
    op = argv[2]
    num2 = int(argv[3])
    
    
    if op == '+':
        print(f'{num1} + {num2} = {add(num1, num2)}')
    elif op == '-':
        print(f'{num1} - {num2} = {sub(num1, num2)}')
    elif op == '*':
        print(f'{num1} * {num2} = {mul(num1, num2)}')
    elif op == '/':
        print(f'{num1} / {num2} = {div(num1, num2)}')
    else:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)

