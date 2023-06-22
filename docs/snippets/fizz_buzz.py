# -*- coding: utf-8 -*-
"""
@author: aidan
"""

def fizz_buzzv1(n: int)-> list():
    fizz_list = []
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            fizz_list.append("FizzBuzz")
        elif i % 5 == 0:
            fizz_list.append("Buzz")
        elif i % 3 == 0:
            fizz_list.append("Fizz")
        else:
            fizz_list.append(" ")
    return fizz_list

def fizz_buzzv2(k: int)-> [str]:
    fizz_list = ["Buzz","Fizz","FizzBuzz", " "]
    lst = []
    for i in range(1,k+1):
        if i%3 == 0 and i%5==0: lst.append(fizz_list[2])
        elif i%5==0: lst.append(fizz_list[0])
        elif i%3==0: lst.append(fizz_list[1])
        else: lst.append(fizz_list[3])
    return lst

def fizz_buzzv3(z: int):
    buffer = []
    for i in range (1,z+1):
        buffer.append(i)
    fizz_list = map(characteristic_digit, buffer)
    return list(fizz_list)
        
def characteristic_digit(z: int):
    if z % 3 == 0 and z % 5 == 0:
        return "FizzBuzz"
    elif z % 5 == 0:
        return "Buzz"
    elif z % 3 == 0:
        return "Fizz"
    else:
        return " "