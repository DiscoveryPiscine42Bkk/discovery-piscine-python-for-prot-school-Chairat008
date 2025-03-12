#!/usr/bin/env python3
import sys

# ตรวจสอบว่ามีพารามิเตอร์ถูกส่งเข้ามาหรือไม่
if len(sys.argv) > 1:
    print(sys.argv[1])  # แสดงพารามิเตอร์แรก
else:
    print("none")  # ถ้าไม่มีพารามิเตอร์ให้แสดง "none"
