#!/usr/bin/env python3

def happy_new_year():
    count_down = 10
    while count_down > 0:
        print(f"{count_down} ")
        count_down -= 1
    print("Happy New Year!\n")

def square_integers(int_list):
    int_list = [ squint * squint for squint in int_list]
    return int_list

def fizzbuzz():
    i = 1
    while i <= 100:
        if i % 3 == 0 and i % 5 != 0:
            print("Fizz")
        elif i % 3 != 0 and i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        else:
            print(f"{i}")
        i += 1


fizzbuzz()
