#!/usr/bin/env python3
import sys

# ตรวจสอบว่ามีพารามิเตอร์ 2 ตัวหรือไม่
if len(sys.argv) == 3:
    keyword = sys.argv[1]
    text = sys.argv[2]
    
    count = text.count(keyword)  # นับจำนวนครั้งที่ keyword ปรากฏใน text
    
    if count > 0:
        print(count)
    else:
        print("none")  # ถ้าไม่มี keyword อยู่ใน text ให้แสดง "none"
else:
    print("none")  # ถ้าจำนวนพารามิเตอร์ไม่ใช่ 2 ให้แสดง "none"
