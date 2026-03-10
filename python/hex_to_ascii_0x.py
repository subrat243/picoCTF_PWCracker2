#!/usr/bin/env python3
import re

hex_input = input("Enter hex values: ")
hex_values = re.findall(r'0x[0-9a-fA-F]+', hex_input)

try:
    ascii_text = ''.join(chr(int(h, 16)) for h in hex_values)
    print("ASCII:", ascii_text)
except ValueError:
    print("Invalid hex input")

