#!/usr/bin/env python3
import sys

# ตรวจสอบว่ามีพารามิเตอร์หรือไม่
if len(sys.argv) > 1:
    print(f"parameters: {len(sys.argv) - 1}")  # แสดงจำนวนพารามิเตอร์
    for param in sys.argv[1:]:
        print(f"{param} {len(param)}")  # แสดงพารามิเตอร์และความยาวของพารามิเตอร์
else:
    print("none")  # ถ้าไม่มีพารามิเตอร์แสดง "none"
