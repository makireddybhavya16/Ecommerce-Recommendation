import pandas as pd
from content_based import recommend_product

data = pd.read_csv("clean_data.csv")

def evaluate_content_based_metrics(
        item_name,
        top_n=5
):

    item_row = data[
        data["Name"] == item_name
    ].iloc[0]

    category = item_row["Category"]
    brand = item_row["Brand"]

    relevant_items = set(
        data[
            (data["Category"] == category) &
            (data["Brand"] == brand)
        ]["Name"]
    )

    recommended_items = set(
        recommend_product(
            item_name,
            top_n
        )
    )

    true_positive = len(
        recommended_items.intersection(
            relevant_items
        )
    )

    precision = true_positive / top_n

    recall = true_positive / len(
        relevant_items
    )

    if precision + recall == 0:
        f1 = 0
    else:
        f1 = (
            2 * precision * recall
        ) / (precision + recall)

    print("Precision:", precision)
    print("Recall:", recall)
    print("F1 Score:", f1)


if __name__ == "__main__":

    evaluate_content_based_metrics(
        data.iloc[0]["Name"]
    )