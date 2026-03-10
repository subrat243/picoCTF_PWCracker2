#!/bin/bash
read -p "Enter hex string: " hex
echo "$hex" | xxd -r -p
