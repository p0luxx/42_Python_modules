#!/usr/bin/python3

def secure_archive(name: str, action: int = 0, content: str = "") -> tuple:
    try:
        if name and action == 0:
            with open(name, 'r') as e:
                info = e.read()
                print("Using 'secure_archive' to read from a regular file:")
                res = (True, f"{info}")
                return res
        elif name and action == 1:
            with open(name, 'w') as e:
                print("Using 'secure_archive' to write "
                      "previous content to a new file:")
                e.write(content)
                res = (True, "Content successfully written to file")
                return res
    except FileNotFoundError as e:
        print("Using 'secure_archive' to read from a nonexistent file:")
        res = (False, f"{e}")
        return res
    except PermissionError as e:
        print("Using 'secure_archive' to read from an inaccessible file:")
        res = (False, f"{e}")
        return res
    else:
        return (False, "Invalid action")


if __name__ == "__main__":
    print("=== Cyber Archives Security ===\n")
    nonexist = secure_archive("/not/existing/file", 0, "")
    print(nonexist, "\n")
    inaccesible = secure_archive("stop.txt", 0, "")
    print(inaccesible, "\n")
    regular_file = secure_archive("test.txt", 0, "")
    print(regular_file, "\n")
    content = "Hello world"
    new_file = secure_archive("other.txt", 1, content)
    print(new_file, "\n")
