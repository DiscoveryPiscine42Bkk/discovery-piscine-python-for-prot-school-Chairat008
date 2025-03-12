#!/usr/bin/env python3
import sys

# ตรวจสอบว่ามีพารามิเตอร์เดียวหรือไม่
if len(sys.argv) == 2:
    print(sys.argv[1].lower())  # แสดงข้อความเป็นตัวพิมพ์เล็ก
else:
    print("none")  # ถ้าจำนวนพารามิเตอร์ไม่ใช่ 1 ให้แสดง "none"
