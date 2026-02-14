from preprocess_data import clean_data

df = clean_data("clean_data.csv")

print("Data loaded successfully!")
print(df.head())
