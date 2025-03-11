#!/usr/bin/env python3

# รับตัวเลขสองตัวจากผู้ใช้
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# คำนวณผลลัพธ์ของการบวก, ลบ, คูณ และ หาร
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

# ตรวจสอบการหาร (ป้องกันหารด้วยศูนย์)
if num2 != 0:
    division = num1 / num2
else:
    division = "undefined (division by zero)"

# แสดงผลลัพธ์
print(f"Addition: {num1} + {num2} = {addition}")
print(f"Subtraction: {num1} - {num2} = {subtraction}")
print(f"Multiplication: {num1} * {num2} = {multiplication}")
print(f"Division: {num1} / {num2} = {division}")
