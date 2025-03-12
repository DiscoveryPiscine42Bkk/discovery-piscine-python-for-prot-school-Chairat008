#!/usr/bin/env python3
import sys

# นับจำนวนพารามิเตอร์ที่ส่งเข้ามา (ไม่รวมชื่อไฟล์)
num_args = len(sys.argv) - 1

# แสดงผลลัพธ์
print("Number of parameters passed:", num_args)
