import pandas as pd
import os

# Path to the folder with Excel files
folder_path = "/Users/laskhyawardhansingh/Desktop/developer/amazon webscrapping"

# Create an empty DataFrame to store all data
merged_data = pd.DataFrame()

# Loop through each file in the folder
for file in os.listdir(folder_path):
    if file.endswith('.xlsx'):  # Only process .xlsx files
        file_path = os.path.join(folder_path, file)
        df = pd.read_excel(file_path)  # Read Excel file
        merged_data = pd.concat([merged_data, df], ignore_index=True)

# Save the merged data into a new file
merged_data.to_excel("/developer/amazon webscrapping/data/merged_output.xlsx", index=False)

print("Merge completed successfully!")
#this code is very important      
