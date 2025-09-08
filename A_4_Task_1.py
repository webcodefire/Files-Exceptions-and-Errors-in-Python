def read_file(filename):
    try:
        with open(filename, "r") as file:
            print("Reading file content:\n")
            for i, line in enumerate(file, start=1):
                print(f"Line {i}: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")


read_file("sample.txt")
