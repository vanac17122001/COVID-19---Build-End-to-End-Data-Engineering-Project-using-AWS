import pandas as pd

# Load the JSON file into a pandas dataframe
df = pd.read_json("usa-hospital-beds.json")

# Convert the dataframe to a CSV file
df.to_csv("usa_hospital_beds.csv", index=False)