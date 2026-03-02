import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
user_product_data = pd.read_csv("user_item_matrix.csv", index_col=0)
similarity_scores = cosine_similarity(user_product_data)

similarity_table = pd.DataFrame(
    similarity_scores,
    index=user_product_data.index,
    columns=user_product_data.index
)
def recommend_for_user(target_user, top_results=5):
    similar_users = similarity_table[target_user].sort_values(ascending=False)
    similar_users = similar_users.drop(target_user)
    most_similar_user = similar_users.index[0]
    products_rated = user_product_data.loc[most_similar_user]
    recommended_products = products_rated[products_rated > 0].sort_values(ascending=False)
    return recommended_products.head(top_results)
if __name__ == "__main__":
    print(recommend_for_user(user_product_data.index[0]))