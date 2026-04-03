import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
df = pd.read_csv("clean_data.csv")

# Fill missing Tags
df["Tags"] = df["Tags"].fillna("")

# TF-IDF vectorizer
tfidf = TfidfVectorizer(stop_words="english")

tfidf_matrix = tfidf.fit_transform(df["Tags"])

# Similarity matrix
cosine_sim = cosine_similarity(tfidf_matrix)


def recommend_product(product_name):

    # If product not found
    if product_name not in df["Name"].values:

        return df.head(5)

    idx = df[df["Name"] == product_name].index[0]

    sim_scores = list(enumerate(cosine_sim[idx]))

    sim_scores = sorted(
        sim_scores,
        key=lambda x: x[1],
        reverse=True
    )

    sim_scores = sim_scores[1:6]

    product_indices = [i[0] for i in sim_scores]

    return df.iloc[product_indices]