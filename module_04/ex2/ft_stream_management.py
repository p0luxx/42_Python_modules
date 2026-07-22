#!/usr/bin/python3
import sys
import typing


def create_new_file(file_name: str, content: str) -> None:
    try:
        new_file: typing.IO
        new_file = open(file_name, 'w')
        new_file.write(content)
        new_file.close()
    except PermissionError as e:
        print(f"[STDERR] Error opening file '{file_name}': {e}", file=sys.stderr)
        print("Data not saved.")


def transform_data(content: str) -> str:
    buff = ""
    for i in range(0, len(content)):
        if content[i] == "\n":
            buff += "#"
            buff += "\n"
        else:
            buff += content[i]
        if i == (len(content) - 1) and content[i] != "\n":
            buff += "#"
    return buff


def normalize_input(string: str) -> str:
    buff = ""
    for i in range(0, len(string)):
        if string[i] == "\n":
            pass
        else:
            buff += string[i]
    return buff

    
def ft_archive_creation(file_name: str) -> None:
    try:
        file: typing.IO
        file = open(file_name, 'r')
        content = file.read()
        print("---\n", file=sys.stdout)
        print(content)
        print("---", file=sys.stdout)
        file.close()
        print(f"File '{file_name}' closed.\n", file=sys.stdout)
        print("Transform data:", file=sys.stdout)
        print("---\n", file=sys.stdout)
        transformed_data = transform_data(content)
        print(transformed_data, file=sys.stdout)
        print("---", file=sys.stdout)
        print("Enter new file name (or empty): ", end="")
        new_file_name = normalize_input(sys.stdin.readline())
        if new_file_name == "":
            print("Not saving data.", file=sys.stdout)
        else:
            print(f"Saving data to '{new_file_name}'", file=sys.stdout)
            create_new_file(new_file_name, transformed_data)
    except FileNotFoundError as e:
        print(f"[STDERR] Error opening file '{sys.argv[1]}': {e}", file=sys.stderr)
    except PermissionError as e:
        print(f"[STDERR] Error opening file '{sys.argv[1]}': {e}", file=sys.stderr)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
    else:
        print("=== Cyber Archives Recovery & Preservation ===")
        ft_archive_creation(sys.argv[1])
