#!/usr/bin/env python3

# รับค่าตัวเลขจากผู้ใช้
number = float(input("Enter a number: "))

# ตรวจสอบว่าเป็นเลขลบ เลขบวก หรือศูนย์
if number < 0:
    print("This number is negative.")
elif number > 0:
    print("This number is positive.")
else:
    print("This number is both positive and negative.")
