#!/usr/bin/env python3

import readline
from colorama import Fore, Back, Style

def calculate(arg):
    stack = list()
    for token in arg.split():
        if token == '+':
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = arg1 + arg2
            print(Fore.RED + token, end = ' ')
            stack.append(result)
        elif token == '-':
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = arg1 - arg2
            print(Fore.RED + token, end = ' ')
            stack.append(result)
        elif token == '*':
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = arg1 * arg2
            print(Fore.RED + token, end = ' ')
            stack.append(result)
        elif token == '^':
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = arg1 ** arg2
            print(Fore.RED + token, end = ' ')
            stack.append(result)
        elif token == '/':
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = arg1 // arg2
            print(Fore.RED + token, end = ' ') 
            stack.append(result)
        else:
            print(Style.RESET_ALL, end = '')
            print(int(token), end = ' ')
            stack.append(int(token))

        #print(stack)
    if len(stack) != 1:
        raise TypeError('malformed input')
    return stack.pop()

def main():
    while True:
       temp =  calculate(input("rpn calc>"))
       print(Style.RESET_ALL, end = '')
       print('=', end = ' ')
       print(Fore.GREEN, end = '')
       print(temp, end = '')
       print(Style.RESET_ALL)


if __name__ == '__main__': #Note: that's "underscore underscore n a m e..."
    main()
