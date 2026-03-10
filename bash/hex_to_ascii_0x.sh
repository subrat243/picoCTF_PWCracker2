#!/bin/bash
read -p "Enter hex values: " input
clean=$(echo "$input" | sed 's/0x//g' | tr -d ' ')
echo "$clean" | xxd -r -p
