#!/usr/bin/env python3
import sys

# ตรวจสอบว่ามีพารามิเตอร์อย่างน้อย 2 ตัวหรือไม่
if len(sys.argv) >= 3:
    print(" ".join(sys.argv[1:][::-1]))  # เรียงลำดับพารามิเตอร์ย้อนกลับและแสดงผล
else:
    print("none")  # ถ้าพารามิเตอร์น้อยกว่า 2 ให้แสดง "none"
