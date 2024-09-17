import pandas as pd
from datetime import datetime
import os

# path of csv files(Input & Output)
directory = "D:/m/python/CSV_File_handling/"
if not os.path.exists(directory):
    os.makedirs(directory)  # Create the directory if it doesn't exist

# File paths
input_file_path = os.path.join(directory, "employees.csv")
filtered_file_path = os.path.join(directory, "filtered_employees.csv")
avg_salary_file_path = os.path.join(directory, "average_salary_all.csv")
avg_salary_dept_file_path = os.path.join(directory, "average_salary_by_department.csv")
date_conversion_file_path = os.path.join(directory, "date_conversion_employees.csv")

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

print(f"Processed data saved successfully in {directory}.")
