######################################################################
#
# 6.Exercise - Number Meter Converter
#
# Python_exe
#
# File:     https://github.com/vbmTafe2024/Python_exe
# Author:   vbmTafe2024
# Version:  1.0
#
# Copyright:  © Copyright 2024, vbmTafe2024
#
# This program helps you convert measurements from meters to centimeters and millimeters.
# Just enter the number of meters, and it will show you the equivalent values in centimeters and millimeters.
######################################################################

meters =float(input("Enter a quantity of metres: "))
print("The metres are:{}M.".format(meters))
print("Converting it to centimeters:{}CM".format(meters *100))
print("Converting it to millimeters:{}MM".format(meters *1000))
