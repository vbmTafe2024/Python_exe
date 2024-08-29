######################################################################
#
# 4.Exercise - Friendly Data Analyzer
#
# Python_exe
#
# File:     https://github.com/vbmTafe2024/Python_exe
# Author:   vbmTafe2024
# Version:  1.0
#
# Copyright:  © Copyright 2024, vbmTafe2024
#
# Description: This program is here to help you understand your data!
# Just enter something, and it will tell you what kind of information it is.
#
######################################################################

#Variables
information = input

# Asking to show the type of the variable and to show its "information/characteristics"
information = input("Please enter something: ")
print("The type is: ",type(information))
print("Is it Alphabetic? :", information.isalpha())
print("Is it Lower Case? : ", information.islower())
print("Is it a number? : ", information.isalnum())
print("Is it a decimal number? : ", information.isdecimal())
print("Is it Printable? : ", information.isprintable())
print("Is it upper letter?: ", information.isupper())
