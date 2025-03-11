#!/usr/bin/env python3

while True:
    user_input = input("Enter something (type 'STOP' to exit): ")
    
    if user_input == "STOP":
        print("Program terminated.")
        break
    else:
        print(f"You entered: {user_input}")
