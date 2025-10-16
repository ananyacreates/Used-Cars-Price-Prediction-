import pandas as pd

# Load each CSV file into a DataFrame
city_master = pd.read_csv('City_Master.csv')
car_sales_transactions = pd.read_csv('Car_sales_transactions.csv')
postal_code_master = pd.read_csv('Postal_Code_Master.csv')
region_master = pd.read_csv('Region_Master.csv')
region_state_mapping = pd.read_csv('Region_State_Mapping.csv')
sales_status = pd.read_csv('Sales_Status.csv')
state_master = pd.read_csv('State_Master.csv')

# Check data types for debugging
print("car_sales_transactions State_Code dtype:", car_sales_transactions['State_Code'].dtype)
print("region_state_mapping State_Code dtype:", region_state_mapping['State_Code'].dtype)

# Ensure 'State_Code' is of the same type in both DataFrames
car_sales_transactions['State_Code'] = car_sales_transactions['State_Code'].astype(str)
region_state_mapping['State_Code'] = region_state_mapping['State_Code'].astype(str)

# Merge dataframes based on common columns
merged_data = car_sales_transactions.merge(city_master, on='City_Code', how='left', suffixes=('', '_city'))
print("Columns after merging with city_master:", merged_data.columns)

merged_data = merged_data.merge(postal_code_master, on='Postal_Code', how='left', suffixes=('', '_postal'))
print("Columns after merging with postal_code_master:", merged_data.columns)

merged_data = merged_data.merge(region_state_mapping, on='State_Code', how='left', suffixes=('', '_region_state'))
print("Columns after merging with region_state_mapping:", merged_data.columns)

merged_data = merged_data.merge(region_master, on='Region_Code', how='left', suffixes=('', '_region'))
print("Columns after merging with region_master:", merged_data.columns)

merged_data = merged_data.merge(state_master, on='State_Code', how='left', suffixes=('', '_state'))
print("Columns after merging with state_master:", merged_data.columns)

merged_data = merged_data.merge(sales_status, on='Sales_ID', how='left', suffixes=('', '_sales'))
print("Columns after merging with sales_status:", merged_data.columns)

# Save the merged data to a new CSV file
merged_data.to_csv('Merged_Car_Sales_Data.csv', index=False)
print("Merged data saved successfully")

# Print the first few rows of the merged data
print(merged_data.head())

# Print the shape of the merged data
print("Shape of merged data:", merged_data.shape)