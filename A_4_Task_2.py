def write_and_append_file():
    filename = "output.txt"

    text_to_write = input("Enter text to write to the file: ")
    with open(filename, "w") as file:
        file.write(text_to_write + "\n")
    print(f"Data successfully written to {filename}.\n")

    text_to_append = input("Enter additional text to append: ")
    with open(filename, "a") as file:
        file.write(text_to_append + "\n")
    print("Data successfully appended.\n")

    print(f"Final content of {filename}:")
    with open(filename, "r") as file:
        print(file.read())


write_and_append_file()
