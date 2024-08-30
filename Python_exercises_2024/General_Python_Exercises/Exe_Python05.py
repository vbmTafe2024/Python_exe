######################################################################
#
# 5.Exercise - Number Successor and Predecessor
#
# Python_exe
#
# File:     https://github.com/vbmTafe2024/Python_exe
# Author:   vbmTafe2024
# Version:  1.0
#
# Copyright:  © Copyright 2024, vbmTafe2024
#
# Description: This program helps you find your number's
# friends! Just enter a number, and it will tell you who comes before and after it.
######################################################################

#variables
number = int
successor = int
predecessor = int

#Program
number = int(input("Enter a Number:"))
print("The number is: {}".format(number))
print("The successor is:",number + 1)
print("The predecessor is:",number - 1)
