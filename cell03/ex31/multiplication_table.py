#!/usr/bin/env python3

# รับค่าตัวเลขจากผู้ใช้
num = int(input("Enter a number: "))

# แสดงสูตรคูณของเลขที่ผู้ใช้ป้อน (ตั้งแต่ 1 ถึง 12)
print(f"Multiplication table for {num}:")
for i in range(1, 13):
    print(f"{num} x {i} = {num * i}")
