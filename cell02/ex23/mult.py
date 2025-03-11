#!/usr/bin/env python3

# รับค่าตัวเลขสองตัวจากผู้ใช้
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# คำนวณผลคูณ
result = num1 * num2

# ตรวจสอบว่าเป็นบวก ลบ หรือศูนย์
if result > 0:
    print("The result is positive.")
elif result < 0:
    print("The result is negative.")
else:
    print("The result is zero.")

# แสดงผลลัพธ์ของการคูณ
print("Multiplication result:", result)
