#!/usr/bin/env python3

hex_string = input("Enter hex string: ").strip().replace(" ", "")

try:
    ascii_text = bytes.fromhex(hex_string).decode('ascii')
    print("ASCII:", ascii_text)
except ValueError:
    print("Invalid hex input")
