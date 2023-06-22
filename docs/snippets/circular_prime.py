"""
@author: aidan
"""

def check_prime(num: int) -> bool:
    if (num <= 1):        
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True 

def rotate_prime(num: int) -> int:
    temp_x = len(str(num))
    temp = ((1 % temp_x) + temp_x) % temp_x 
    left_num = num // pow(10, temp_x - temp)
    num = num % pow(10, temp_x - temp)
    left_digit = len(str(left_num))
    num = num * pow(10, left_digit) + left_num 
    return num

def is_circularprime(num: int) -> bool:
    for i in range(0, len(str(num))):
        if(check_prime(num) == False):
            return False
        num = rotate_prime(num)
    return True
        
