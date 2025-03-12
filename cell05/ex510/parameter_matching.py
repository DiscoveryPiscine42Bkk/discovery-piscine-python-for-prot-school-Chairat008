#!/usr/bin/env python3
import sys

# ตรวจสอบว่ามีพารามิเตอร์ 1 ตัวหรือไม่
if len(sys.argv) == 2:
    # ถ้ามีพารามิเตอร์
    user_word = input("Enter a word: ")  # ขอให้ผู้ใช้ป้อนคำ
    if user_word == sys.argv[1]:
        print("Good job!")  # ถ้าคำที่ป้อนตรงกับพารามิเตอร์แสดง "Good job!"
    else:
        print("Nope, sorry...")  # ถ้าคำไม่ตรงแสดง "Nope, sorry..."
else:
    print("none")  # ถ้าจำนวนพารามิเตอร์ไม่ใช่ 1 ให้แสดง "none"
