#!/usr/bin/python3

import sys
import typing


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
    else:
        file_name = sys.argv[1]
        try:
            print("=== Cyber Archives Recovery ===")
            print(f"Accessing file '{sys.argv[1]}'")
            file: typing.IO
            file = open(file_name, 'r')
            file_content = file.read()
            print("---\n")
            print(file_content)
            print("---")
            file.close()
            print(f"File '{sys.argv[1]}' closed")
        except FileNotFoundError as e:
            print(f"Error opening file '{sys.argv[1]}': {e}")
        except PermissionError as e:
            print(f"Error opening file '{sys.argv[1]}': {e}")
