from hybrid_model import hybrid_recommendation

if __name__ == "__main__":

    print("\nAI Recommendation Engine\n")

    item_name = input(
        "Enter product name: "
    )

    user_id = int(
        input(
            "Enter user ID: "
        )
    )

    recommendations = hybrid_recommendation(
        item_name,
        user_id
    )

    print("\nRecommended Products:\n")

    for product in recommendations:
        print(product)