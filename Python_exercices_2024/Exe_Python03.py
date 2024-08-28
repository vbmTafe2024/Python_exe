######################################################################
#
# 3.Exercise - Sum of two numbers
#
# Python_exe
#
# File:     https://github.com/vbmTafe2024/Python_exe
# Author:   vbmTafe2024
# Version:  1.0
#
# Copyright:  © Copyright 2024, vbmTafe2024
#
# Description: This Python code calculates the sum of two numbers entered by the user.
# It asks for the first number, then the second, and adds them together.
# Finally, it prints the result in a formatted message.
#
######################################################################
#variable
total = 0

# Asking the user to add the numbers
first_number = float(input("Please write your first number: "))
second_number = float(input("Please write your second number: "))

# Making the addition
total = first_number + second_number
print("The total between {0} + {1} = {2}".format(first_number, second_number, total))
