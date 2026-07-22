import sys
import typing


def create_new_file(file_name: str, content: str) -> None:
    new_file: typing.IO
    new_file = open(file_name, 'w')
    new_file.write(content)
    new_file.close()


def transform_data(content: str) -> str:
    buffer = ""
    for i in range(0, len(content)):
        if content[i] == "\n":
            buffer += '#'
            buffer += "\n"
        else:
            buffer += content[i]
        if i == (len(content) - 1) and content[i] != "\n":
            buffer += '#'
    return buffer


def ft_archive_creation(file_name: str) -> None:
    print(f"Accessing file '{file_name}'")
    try:
        file: typing.IO
        file = open(file_name, 'r')
        content = file.read()
        print("---\n")
        print(content)
        print("---")
        file.close()
        print(f"File '{file_name}' closed.\n")
        print("Transform data:")
        print("---\n")
        transformed_data = transform_data(content)
        print(transformed_data)
        print("---")
        new_file_name = input("Enter new file name (or empty): ")
        if new_file_name == "":
            print("Not saving data.")
        else:
            print(f"Saving data to '{new_file_name}'")
            create_new_file(new_file_name, transformed_data)
            print(f"Data saved in file '{new_file_name}'.")
    except FileNotFoundError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")
    except PermissionError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
    else:
        print("=== Cyber Archives Recovery & Preservation ===")
        ft_archive_creation(sys.argv[1])
