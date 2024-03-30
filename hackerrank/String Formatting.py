"""
Given an integer, , print the following values for each integer  from  to :

Decimal
Octal
Hexadecimal (capitalized)
Binary
Function Description

Complete the print_formatted function in the editor below.

print_formatted has the following parameters:

int number: the maximum value to print
Prints

The four values must be printed on a single line in the order specified above for each  from  to . Each value should be space-padded to match the width of the binary value of  and the values should be separated by a single space.

Input Format

A single integer denoting .

"""


def print_formatted(number):
    #print(number)
    # your code goes here
    width = len(bin(number)[2:])
    #print(width)
    for i in range(1, 1 + number):
        #print(i)
        oct1 = oct(i)[2:]
        #print(type(oct1))
        hex1 = hex(i)[2:].upper()
        bin1 = bin(i)[2:]
        #number= str(number)
        print(str(i).rjust(width), oct1.rjust(width), hex1.rjust(width), bin1.rjust(width))
