import pandas as pd


# Load dataset
data = pd.read_csv("Housing_Dataset.csv")

print("First 5 Rows:")
print(data.head())

print("\nLast 5 Rows:")
print(data.tail())

print("\nData Types:")
print(data.dtypes)

print("\nStatistical Summary:")
print(data.describe())

print("\nColumns:")
print(data.columns)

print("\nDataset Shape:")
print(data.shape)

print("\nMissing Values:")
print(data.isnull().sum())

# Select useful columns
usefull = ['Suburb', 'Rooms', 'Type', 'Price',
           'Method', 'SellerG', 'Car', 'Bedroom2', 'Bathroom',
           'Landsize', 'Distance', 'BuildingArea',
           'CouncilArea', 'Regionname', 'Propertycount']

newData = data[usefull]

print("\nSelected Data Shape:")
print(newData.shape)

print("\nMissing Values After Column Selection:")
print(newData.isnull().sum())

# Fill specific columns with 0
cols = ['Car', 'Bathroom', 'Bedroom2', 'Propertycount', 'Distance']
newData[cols] = newData[cols].fillna(0)

# Replace missing values with median
newData['BuildingArea'] = newData['BuildingArea'].fillna(newData['BuildingArea'].median())
newData['Landsize'] = newData['Landsize'].fillna(newData['Landsize'].median())

print("\nMissing Values After Filling:")
print(newData.isnull().sum())

# Drop remaining missing values
newData.dropna(inplace=True)

print("\nFinal Missing Values:")
print(newData.isnull().sum())

# Convert categorical variables into dummy variables
newData = pd.get_dummies(newData, drop_first=True)

print("\nFinal Dataset Shape After Encoding:")
print(newData.shape)

# Save cleaned dataset
newData.to_csv("Cleaned_Housing_Dataset.csv", index=False)

print("\nCleaned dataset saved as 'Cleaned_Housing_Dataset.csv'")
