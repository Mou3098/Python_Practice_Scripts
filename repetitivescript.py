import os
import glob
import pandas as pd
import json

def rename_one_file(src,dst):
    try:
        print("renamed the specific file name")
        os.rename(src,dst)
    except OSError as e:
        print(f"Error: {e}")
    # another method using pathlib
    # from pathlib import Path
    # old_file = Path('path/to/old_filename.ext')
    # new_file = Path('path/to/new_filename.ext')
    #
    # old_file.rename(new_file)


def rename_same_type_files_global():
    # Find all files with names start with "d" and ending with ".jpg"
    files = glob.glob('d*.jpg')

    # Loop through each file and rename them
    for file in files:
        # Split the file name at the '_' character
        parts = file.split('_')

        # Create a new file name using the parts and the desired prefix
        new_name = f'new_{parts[1]}'

        # Rename the file using os.rename()
        os.rename(file, new_name)
        print(f"Renamed: {file} to {new_name}")
    print("renamed same_type_files_global")

def rename_files_definite_directory(directory_path, prefix):
    # Get the list of files in the directory
    files = os.listdir(directory_path)

    # Iterate through each file and rename it with the specified prefix
    for file_name in files:
        old_path = os.path.join(directory_path, file_name)

        # Extract the file extension
        file_name, file_extension = os.path.splitext(file_name)

        # Construct the new file name with the prefix
        new_file_name = f"{prefix}{file_name}{file_extension}"

        new_path = os.path.join(directory_path, new_file_name)

        # Rename the file
        os.rename(old_path, new_path)

        print(f"Renamed: {file_name} to {new_file_name}")
    print("renamed same_type_files_global")

def process_data_in_directory(directory_path):
    word_count = {}

    try:
        # Iterate through all files in the specified directory
        for file_name in os.listdir(directory_path):
            # Check if the file is a text file
            if file_name.endswith(".txt"):
                file_path = os.path.join(directory_path, file_name)

                # Open the file for reading
                with open(file_path, 'r') as file:
                    # Read the content of the file
                    data = file.read()

                    # Tokenize the words (assuming words are separated by whitespace)
                    words = data.split()

                    # Count occurrences of each word across all files
                    for word in words:
                        # Remove punctuation and convert to lowercase for better counting
                        clean_word = word.lower()
                        word_count[clean_word] = word_count.get(clean_word, 0) + 1

    except FileNotFoundError:
        print(f"Error: Directory {directory_path} not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

    for word, count in word_count.items():
        print(f"{word}: {count}")



def process_and_write_to_excel(input_file, output_excel):
    try:
        # Read input string from file
        with open(input_file, 'r') as file:
            input_string = file.read()

        # Process the input string
        processed_string, character_count = process_string(input_string)

        # Create a DataFrame for the results
        data = {'Character': list(processed_string), 'Count': [character_count[char] for char in processed_string]}
        df = pd.DataFrame(data)

        # Write to Excel file
        df.to_excel(output_excel, index=False)
        print(f"Data written to {output_excel}")

    except FileNotFoundError:
        print(f"Error: File {input_file} not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
#part of  process_and_write_to_excel
def process_string(input_string):
    # Remove spaces and special characters
    cleaned_string = ''.join(char for char in input_string if char.isalnum())

    # Remove duplicate characters
    unique_characters = ''.join(sorted(set(cleaned_string), key=cleaned_string.index))

    # Count characters
    character_count = {char: cleaned_string.count(char) for char in unique_characters}

    return unique_characters, character_count



def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"File not found at {file_path}")
        return None
    except json.JSONDecodeError:
        print(f"Error decoding JSON from {file_path}")
        return None

def write_file(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

def update_file_info(file_path, key, new_value):
    data = read_file(file_path)

    if data is not None:
        if key in data:
            data[key] = new_value
            write_file(file_path, data)
            print(f"Updated {key} to {new_value} in {file_path}")
        else:
            print(f"{key} not found in {file_path}")

# Example usage:
local_file_path = 'path/to/your/local/file.json'
update_key = 'version'
new_version = '2.0'

update_file_info(local_file_path, update_key, new_version)


if __name__ == "__main__":
    # Specify the directory path and prefix
    # directory_path = "E:/renamingfile"
    # prefix = ""

    # Call the function to rename files

    # rename_one_file("E:/renamingfile/textfile.txt","E:/renamingfile/renamed_text.txt")
    # rename_files_definite_directory("E:/renamingfile", "mm")
    # rename_same_type_files_global()

    #process_data_in_directory("E:/renamingfile")
    process_and_write_to_excel("E:/renamingfile/textfile.txt", "E:/renamingfile/Excel.xlsx")
