#!/usr/bin/env python3

def happy_new_year():
    number = 10

    while number >= 0:
        if number != 0:
            print(number)
        else:
            print("Happy New Year!")
            return "Happy New Year!"

        number -= 1


happy_new_year()
# 10
# 9
# ...
# 2
# 1
# Happy New Year!

def square_integers(int_list):
    # code goes here!


    int_list = [int * int for int in int_list]
    print(int_list)
    return int_list
    pass


square_integers([1, 2, 3, 4, 5])
# [1, 4, 9, 16, 25]

def fizzbuzz():
    # code goes here!
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
    pass




fizzbuzz()
# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# ...
# 14
# FizzBuzz
# 16
# ...
# 98
# Fizz
# Buzz
