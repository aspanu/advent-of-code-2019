import math

'''
You arrive at the Venus fuel depot only to discover it's protected by a password. The Elves had written the password on a sticky note, but someone threw it out.

However, they do remember a few key facts about the password:

It is a six-digit number.
The value is within the range given in your puzzle input.
Two adjacent digits are the same (like 22 in 122345).
Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
Other than the range rule, the following are true:

111111 meets these criteria (double 11, never decreases).
223450 does not meet these criteria (decreasing pair of digits 50).
123789 does not meet these criteria (no double).
How many different passwords within the range given in your puzzle input meet these criteria?
--> 56549

Your puzzle input is 108457-562041.
'''

# Generate potential 6 digit numbers by incrementing numbers, starting at max(111111, puzzle input min) (smallest possible value)
# End at puzzle min(999999, puzzle input max)
# Check to see if the password generated follows each rule
# Increment a counter if it does

def checkIfNumIsPossiblePassword(num: int) -> bool:
    str_version = str(num)
    prev_digit = int(str_version[0])
    has_double_digits = False
    for i in range(1, len(str_version)):
        if int(str_version[i]) < prev_digit:
            return False
        if int(str_version[i]) == prev_digit:
            has_double_digits = True
    
    return has_double_digits

# print(checkIfNumIsPossiblePassword(111111))
# print(checkIfNumIsPossiblePassword(223450))
# print(checkIfNumIsPossiblePassword(123789))

def findNumberOfPossiblePasswords(input_min: int, input_max: int) -> int:
    start_num = max(111111, input_min)
    end_num = min(999999, input_max)

    num_passwords = 0

    for num in range(start_num, end_num+1):
        if checkIfNumIsPossiblePassword(num):
            num_passwords += 1
    
    return num_passwords

print(findNumberOfPossiblePasswords(108457, 562041))