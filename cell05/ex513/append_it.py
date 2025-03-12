#!/usr/bin/env python3
import sys

# ตรวจสอบว่ามีพารามิเตอร์หรือไม่
if len(sys.argv) > 1:
    for param in sys.argv[1:]:
        # ตรวจสอบว่าพารามิเตอร์มีคำว่า "ism" ต่อท้ายหรือไม่
        if not param.endswith("ism"):
            print(param + "ism")  # ถ้าไม่มี "ism" ต่อท้าย แสดงพารามิเตอร์พร้อม "ism"
else:
    print("none")  # ถ้าไม่มีพารามิเตอร์ แสดง "none"
