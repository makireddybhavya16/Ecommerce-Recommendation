import pandas as pd
import numpy as np

def clean_data(file_path):
    df = pd.read_csv(file_path)

    df.dropna(subset=["User's ID", "ProdID", "Rating"], inplace=True)

    text_columns = ["Category", "Brand", "Description", "Tags"]
    df[text_columns] = df[text_columns].fillna("")

    df.reset_index(drop=True, inplace=True)

    df["User's ID"] = pd.to_numeric(df["User's ID"], errors='coerce')
    df["ProdID"] = pd.to_numeric(df["ProdID"], errors='coerce')

    df = df[(df["User's ID"] != 0) & (df["ProdID"] != 0)]

    df.reset_index(drop=True, inplace=True)

    return df
