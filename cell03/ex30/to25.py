#!/usr/bin/env python3

# รับค่าตัวเลขจากผู้ใช้
num = int(input("Enter a number: "))

# ถ้าตัวเลขมากกว่า 25 ให้แสดง Error
if num > 25:
    print("Error\n")
else:
    # ใช้ loop แสดงตัวเลขตั้งแต่ num ถึง 25
    for i in range(num, 26):
        print(i)
