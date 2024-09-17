import pandas as pd
from datetime import datetime
import os

# Current working directory
current_directory = os.getcwd()

# Define input and output subdirectories
input_subdirectory = os.path.join(current_directory, 'CSV_File_handling_input')
output_subdirectory = os.path.join(current_directory, 'output_files')

# Create output subdirectory if it doesn't exist
if not os.path.exists(output_subdirectory):
    os.makedirs(output_subdirectory)

# File paths
input_file_path = os.path.join(input_subdirectory, 'employees.csv')
filtered_file_path = os.path.join(output_subdirectory, 'filtered_employees.csv')
avg_salary_file_path = os.path.join(output_subdirectory, 'average_salary_all.csv')
avg_salary_dept_file_path = os.path.join(output_subdirectory, 'average_salary_by_department.csv')
date_conversion_file_path = os.path.join(output_subdirectory, 'date_conversion_employees.csv')

print(input_file_path)
# Load CSV data
df = pd.read_csv(input_file_path)

# Filtering Rows
filtered_df = df[(df['Department'] == 'Engineering') | (df['Salary'] > 60000)]
filtered_df.to_csv(filtered_file_path, index=False)

# Compute Average Salaries
average_salary_all = df['Salary'].mean()
average_salary_by_dept = df.groupby('Department')['Salary'].mean()

# Save average salaries to CSV files
pd.DataFrame({'Average Salary': [average_salary_all]}).to_csv(avg_salary_file_path, index=False)
average_salary_by_dept.to_csv(avg_salary_dept_file_path, index=True)

# Date Conversion
df['JoiningDate'] = pd.to_datetime(df['JoiningDate'])  # Ensure 'JoiningDate' is in datetime format
df['YearsWithCompany'] = ((datetime.now() - df['JoiningDate']).dt.days / 365.25).round(2)  # Calculate years with company

# Save date conversion results to CSV file
df.to_csv(date_conversion_file_path, index=False)

print(f"Processed data saved successfully in {output_subdirectory}.")
