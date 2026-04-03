from content_based import recommend_product
from collaborative_based import recommend_for_user
from rating_based import get_top_rated_products

def hybrid_recommendation(
        item_name,
        user_id,
        top_results=5
):

    content_rec = recommend_product(
        item_name,
        top_results
    )

    collaborative_rec = recommend_for_user(
        user_id,
        top_results
    )

    rating_rec = get_top_rated_products(
        top_results
    )

    final_rec = list(
        set(
            content_rec +
            collaborative_rec +
            rating_rec
        )
    )

    return final_rec[:top_results]