#!/usr/bin/env python3

# รับตัวเลขจากผู้ใช้
num = input("Enter a number: ")

# เช็คว่าเป็นเลขทศนิยมไหม
try:
    float_num = float(num)  # พยายามแปลงเป็นทศนิยม
    if '.' in num:  # เช็คว่าเป็นทศนิยม (ตรวจสอบการมีจุดทศนิยมในสตริง)
        print("This is a decimal number.")
    else:
        print("This is not a decimal number.")
except ValueError:
    print("Invalid input! Please enter a valid number.")
