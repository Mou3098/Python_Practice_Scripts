import re
import csv

def extract_bangladesh_numbers(text):
    # Use regular expression to extract Bangladesh mobile numbers
    pattern = re.compile(r'\b(?:\+88|88)?01[3-9]\d{8}\b')
    return re.findall(pattern, text)

def read_mobile_numbers_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return extract_bangladesh_numbers(content)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []

def write_to_csv(numbers, csv_file_path):
    fieldnames = ['phone']

    with open(csv_file_path, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for number in numbers:
            writer.writerow({'phone': number})

if __name__ == "__main__":
    input_file_path = 'E:/renamingfile/input_text.txt'
    output_csv_file_path = 'E:/renamingfile/output_numbers.csv'

    bangladesh_numbers = read_mobile_numbers_from_file(input_file_path)

    write_to_csv(bangladesh_numbers, output_csv_file_path)

    print(f"numbers written to {output_csv_file_path}")