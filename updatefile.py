import os
import shutil

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print("File content:\n", content)
        return content
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        return None

def write_to_file(file_path, data):
    with open(file_path, 'w') as file:
        file.write(data)
    print(f"Data written to {file_path}")

def append_to_file(file_path, data):
    with open(file_path, 'a') as file:
        file.write(data)
    print("APPEND FILE\n")
    print(f"Data appended to {file_path}")

def delete_file(file_path):
    try:
        os.remove(file_path)
        print(f"File {file_path} deleted successfully.")
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")

def update_string_in_file(file_path, old_string, new_string):
    content = read_file(file_path)
    if content is not None:
        updated_content = content.replace(old_string, new_string)
        write_to_file(file_path, updated_content)
        print("UPDATED FILE\n")
        print(f"Updated '{old_string}' to '{new_string}' in {file_path}")

if __name__ == "__main__":
    # Replace with the actual path to a file on your desktop
    file_on_desktop = "E:/renamingfile/textfile.txt"

    # Read file
    read_file(file_on_desktop)

    # Update a word or string in the file
    update_string_in_file(file_on_desktop, "Hello", "Hi")

    # Read updated file
    read_file(file_on_desktop)

    append_to_file("E:/renamingfile/textfile.txt", "append_to_file")

    read_file(file_on_desktop)

    delete_file("E:/renamingfile/Excel.xlsx")
    read_file("E:/renamingfile/Excel.xlsx")

    write_to_file(file_on_desktop, "kotha bolbo na \n kotha na bolle ki hbe?")
    read_file(file_on_desktop)
