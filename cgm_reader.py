import os
import pandas as pd
import json

# Define the root directory containing the dataset
root_dir = "Dataset/dataset/wearable_blood_glucose/continuous_glucose_monitoring/dexcom_g6"

# List to store DataFrames
dataframes = []

# Traverse through subdirectories and process JSON files
for subdir in os.listdir(root_dir):
    subdir_path = os.path.join(root_dir, subdir)
    if os.path.isdir(subdir_path):  # Ensure it's a directory
        json_file = os.path.join(subdir_path, f"{subdir}_DEX.json")
        if os.path.isfile(json_file):  # Check if the JSON file exists
            with open(json_file, 'r') as f:
                data = json.load(f)
            
            # Extract metadata
            patient_id = data['header']['patient_id']
            
            # Extract glucose readings
            cgm_data = data['body']['cgm']
            for entry in cgm_data:
                start_time = entry['effective_time_frame']['time_interval']['start_date_time']
                glucose_value = entry['blood_glucose']['value']
                # Append to a list
                dataframes.append({
                    'timestamp': start_time,
                    'glucose_level': glucose_value,
                    'patient_id': patient_id
                })

# Convert the list of dictionaries to a DataFrame
df = pd.DataFrame(dataframes)

# Convert the timestamp to a more readable format
df['timestamp'] = pd.to_datetime(df['timestamp'])  # Convert to datetime object
df['timestamp'] = df['timestamp'].dt.strftime('%Y-%m-%d %H:%M:%S')  # Format as 'YYYY-MM-DD HH:MM:SS'

# Save the processed data to a CSV file
output_csv = "processed_glucose_data.csv"
df.to_csv(output_csv, index=False)
