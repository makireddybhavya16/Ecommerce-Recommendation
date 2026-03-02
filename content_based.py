import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

products = pd.read_csv("clean_data.csv")
products["Tags"] = products["Tags"].fillna("")

vectorizer = TfidfVectorizer(stop_words="english")
tag_vectors = vectorizer.fit_transform(products["Tags"])

similarity_matrix = cosine_similarity(tag_vectors, tag_vectors)

def recommend_product(search_name, top_results=5):
    matched_index = products[products["Name"].str.contains(search_name, case=False)].index
    
    if len(matched_index) == 0:
        return "Product not found"
    
    product_index = matched_index[0]
    similarity_scores = list(enumerate(similarity_matrix[product_index]))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    similarity_scores = similarity_scores[1:top_results+1]
    recommended_indices = [item[0] for item in similarity_scores]
    return products.iloc[recommended_indices][["Name","Brand"]]

if __name__ == "__main__":
    print(recommend_product("lipstick"))