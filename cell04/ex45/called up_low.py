#!/usr/bin/env python3

# รับข้อความจากผู้ใช้
user_input = input("Enter a string: ")

# สลับตัวอักษรพิมพ์ใหญ่เป็นพิมพ์เล็กและพิมพ์เล็กเป็นพิมพ์ใหญ่
swapped_case = user_input.swapcase()

# แสดงผลลัพธ์
print(f"The string with swapped case is: {swapped_case}")
