#!/usr/bin/env python3
import sys

# ตรวจสอบว่ามีพารามิเตอร์ 2 ตัว
if len(sys.argv) == 3:
    try:
        # แปลงพารามิเตอร์ให้เป็นตัวเลข
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])
        
        # สร้างอาเรย์จาก range ของตัวเลขระหว่าง num1 และ num2
        number_range = list(range(num1, num2 + 1))
        
        # แสดงอาเรย์
        print(number_range)
    
    except ValueError:
        print("none")  # ถ้าไม่สามารถแปลงเป็นตัวเลขได้
else:
    print("none")  # ถ้ามีพารามิเตอร์ไม่ครบ
