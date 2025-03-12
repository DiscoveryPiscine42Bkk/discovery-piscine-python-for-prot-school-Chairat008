#!/usr/bin/env python3
import sys

# ตรวจสอบว่ามีพารามิเตอร์ 1 ตัวหรือไม่
if len(sys.argv) == 2:
    # รับค่าพารามิเตอร์ที่ 1
    string = sys.argv[1]
    
    # ค้นหาตัวอักษร "z" ในสตริง
    if 'z' in string:
        # แสดง "z" สำหรับทุกครั้งที่พบ "z" ในสตริง
        for char in string:
            if char == 'z':
                print('z')
    else:
        print("none")  # ถ้าไม่มี "z" ให้แสดง "none"
else:
    print("none")  # ถ้าจำนวนพารามิเตอร์ไม่ใช่ 1 ให้แสดง "none"
