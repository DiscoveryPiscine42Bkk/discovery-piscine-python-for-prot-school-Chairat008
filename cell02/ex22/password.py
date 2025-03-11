#!/usr/bin/env python3

# กำหนดรหัสผ่านที่ถูกต้อง
password = "ChairatLnwza"

# รับรหัสผ่านจากผู้ใช้
user_input = input("Enter the password: ")

# ตรวจสอบว่ารหัสถูกต้องหรือไม่
if user_input == password:
    print("ACCESS GRANTED")
else:
    print("ACCESS DENIED")
