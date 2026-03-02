import pandas as pd
product_data = pd.read_csv("clean_data.csv")

def get_top_rated_products(top_results=5):
    sorted_products = product_data.sort_values(by="Rating", ascending=False)
    return sorted_products[["Name","Rating"]].head(top_results)

if __name__ == "__main__":
    print(get_top_rated_products())