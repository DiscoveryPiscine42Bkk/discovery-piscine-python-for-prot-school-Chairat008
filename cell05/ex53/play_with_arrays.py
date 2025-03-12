#!/usr/bin/env python3

# กำหนดอาเรย์ของตัวเลข
original_array = [2, 8, 9, 48, 8, 22, -12, 2]

# สร้างอาเรย์ใหม่โดยเพิ่มค่า 2 ให้กับทุกตัวในอาเรย์เดิม
new_array = [num + 2 for num in original_array]

# กำจัดค่าที่ซ้ำโดยไม่ใช้ set() (รักษาลำดับเดิมไว้)
unique_new_array = []
for num in new_array:
    if num not in unique_new_array:
        unique_new_array.append(num)

# แสดงผลลัพธ์
print("Original array:", original_array)
print("New array without duplicates:", unique_new_array)
