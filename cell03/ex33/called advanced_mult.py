#!/usr/bin/env python3

# วนลูปตัวเลข 1-12 เพื่อสร้างสูตรคูณ
for num in range(1, 13):
    print(f"Multiplication table for {num}:")
    for i in range(1, 13):
        print(f"{num} x {i} = {num * i}")
    print("-" * 20)  # เส้นคั่นระหว่างตาราง
