import pandas as pd
import matplotlib.pyplot as plt

"""Load the data from a CSV file."""
def load_data(csv_file):
  df = pd.read_csv(csv_file, header = 0)
  low_value = 40  # select a value to use for low
  high_value = 400  # select a value to use for high

  if (0):
      df.replace({"Low": low_value, "High": high_value}, inplace=True)  # notebook dev used pd 2.1.4
  else:  # to avoid the FutureWarning regarding Downcasting behavior in 'replace'

      def replace_alt(val, low_value, high_value):
          if val == "Low":
              return low_value
          elif val == "High":
              return high_value
          else:
              return val

      df['glucose_level'] = df.apply(lambda x: replace_alt(x['glucose_level'],
                                                                low_value, high_value), axis=1)
  
  return df

"""Plot glucose levels over time for a specific patient."""
def plot_glucose_trend(df, patient_id):
  patient_data = df[df['patient_id'] == patient_id]
  #Visualize every 20 data points
  patient_data = patient_data.iloc[::20]  

  min_glucose = int(patient_data['glucose_level'].min() // 10 * 10)  # Round down to nearest 10
  max_glucose = int(patient_data['glucose_level'].max() // 10 * 10) + 10  # Round up to nearest 10

  plt.figure(figsize=(12, 4))
  plt.title("Blood Glucose Levels Over Time", fontsize=16)
  plt.plot(patient_data['timestamp'], patient_data['glucose_level'], label=patient_id, color='blue')
  plt.xlabel("Time", fontsize=12)
  plt.ylabel("Blood Glucose (mg/dL)", fontsize=10)
  plt.xticks(patient_data['timestamp'][::10], rotation=45, fontsize=5)
  plt.yticks(range(min_glucose, max_glucose, 10), fontsize=5)  # Set y-axis ticks at increments of 10
  plt.legend()
  plt.tight_layout()
  plt.show()

"""Main function"""
if __name__ == "__main__":
  patient_id = "AIREADI-1001"
  # Path to the processed CSV file
  csv_file = "processed_glucose_data.csv"

  # Load data
  df = load_data(csv_file)
  print(df.head())

  plot_glucose_trend(df, patient_id)
