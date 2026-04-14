import reflex as rx
import pandas as pd

from ai_recommendation_engine.state.cart_state import CartState


# Load dataset
df = pd.read_csv("clean_data.csv")

# Clean images
df["ImageURL"] = df["ImageURL"].apply(
    lambda x: x.split("|")[0] if isinstance(x, str) else ""
)


class RecommendationState(rx.State):

    search_text: str = ""

    recommendations: list[dict] = []

    def set_search_text(self, value: str):
        self.search_text = value


    def get_recommendations(self):

        if self.search_text.strip() == "":
            self.recommendations = (
                df.head(6)
                .to_dict("records")
            )
            return

        keyword = self.search_text.lower()

        filtered = df[
            df["Name"]
            .str.lower()
            .str.contains(keyword, na=False)
        ]

        if filtered.empty:

            filtered = df[
                df["Category"]
                .str.lower()
                .str.contains(keyword, na=False)
            ]

        if filtered.empty:
            filtered = df.head(6)

        self.recommendations = (
            filtered.head(6)
            .to_dict("records")
        )


def product_card(product):

    return rx.box(

        rx.vstack(

            rx.image(
                src=product["ImageURL"],
                width="120px",
                height="120px",
                object_fit="contain"
            ),

            rx.text(
                product["Name"],
                font_size="12px",
                text_align="center"
            ),

            rx.text(
                "₹299",
                color="limegreen",
                font_weight="bold"
            ),

            rx.button(
                "Add to Cart",

                on_click=lambda:
                    CartState.add_to_cart(
                        product["Name"],
                        product["ImageURL"]
                    )
            ),

            spacing="2",
            align="center"

        ),

        padding="10px",
        border_radius="12px",
        background_color="#1f1f1f",
        width="180px"

    )


def recommendations():

    return rx.vstack(

        rx.heading(
            "Recommendations",
            font_size="28px"
        ),

        rx.hstack(

            rx.link(
                rx.button(
                    "View Cart 🛒",
                    color_scheme="green"
                ),
                href="/cart"
            ),

            rx.text(
                f"Cart Items: {CartState.cart_count}"
            ),

            spacing="4"

        ),

        rx.input(

            placeholder="Enter product name",

            on_change=
                RecommendationState.set_search_text

        ),

        rx.button(

            "Get Recommendations",

            on_click=
                RecommendationState.get_recommendations

        ),

        rx.divider(),

        rx.grid(

            rx.foreach(
                RecommendationState.recommendations,
                product_card
            ),

            columns="3",
            spacing="6"

        ),

        padding="20px"

    )