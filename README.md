# Hex to ASCII Converter (CTF Utilities)

Utilities created for solving CTF challenges such as PW Crack 2 where encoded values (hex / 0x hex) must be converted to readable ASCII during password or flag analysis.

---

# Project Structure

```
hex-to-ascii/
├─ README.md
├─ python/
│  ├─ hex_to_ascii_plain.py
│  └─ hex_to_ascii_0x.py
└─ bash/
   ├─ hex_to_ascii_plain.sh
   └─ hex_to_ascii_0x.sh
```

---

# File: README.md

## Hex to ASCII Converter

Simple utilities to convert hexadecimal values to ASCII text.

### Features

* Python and Bash implementations
* Supports plain hex strings
* Supports `0x` prefixed hex values
* Useful for CTFs and password/flag decoding

---

## Usage

### Python — Plain Hex

```
python3 python/hex_to_ascii_plain.py
```

### Python — 0x Format

```
python3 python/hex_to_ascii_0x.py
```

### Bash — Plain Hex

```
bash bash/hex_to_ascii_plain.sh
```

### Bash — 0x Format

```
bash bash/hex_to_ascii_0x.sh
```

---

## One-Liners

### Python (Plain Hex)

```bash
python3 -c "print(bytes.fromhex(input().strip()).decode())"
```

### Python (0x Format)

```bash
python3 -c "import re;print(''.join(chr(int(x,16)) for x in re.findall(r'0x[0-9a-fA-F]+', input())))"
```

### Bash (Plain Hex)

```bash
echo "48656c6c6f" | xxd -r -p
```

### Bash (0x Format)

```bash
echo "0x48 0x65 0x6c 0x6c 0x6f" | sed 's/0x//g' | tr -d ' ' | xxd -r -p
```

---

## License

MIT License

---

# File: python/hex_to_ascii_plain.py

```python
#!/usr/bin/env python3

hex_string = input("Enter hex string: ").strip().replace(" ", "")

try:
    ascii_text = bytes.fromhex(hex_string).decode('ascii')
    print("ASCII:", ascii_text)
except ValueError:
    print("Invalid hex input")
```

---

# File: python/hex_to_ascii_0x.py

```python
#!/usr/bin/env python3
import re

hex_input = input("Enter hex values: 
---

# File: bash/hex_to_ascii_plain.sh

Make executable:

```
chmod +x bash/hex_to_ascii_plain.sh
```

---

# File: bash/hex_to_ascii_0x.sh

Make executable:

```
chmod +x bash/hex_to_ascii_0x.sh
```
