import requests
import pandas as pd

# API URL
url = "https://jsonplaceholder.typicode.com/users"

# Send GET request
response = requests.get(url)

# Check status code
print("Status Code:", response.status_code)

# Convert response to JSON
data = response.json()

# Convert JSON data into DataFrame
df = pd.DataFrame(data)

# Display the data
print("\nAPI Data:")
print(df)

# Display basic information
print("\nNumber of Records:", len(df))
print("Number of Columns:", len(df.columns))

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Save data as CSV
df.to_csv("api_users.csv", index=False)

print("\nCSV file created successfully!")

#Perform basic analysis
print("\nfirst 5 records:")
print(df.head())

print("\nDataset information:")
print(df.info())

