import reflex as rx
import pandas as pd

from ai_recommendation_engine.state.cart_state import CartState


# Load dataset
df = pd.read_csv("clean_data.csv")

# FIX: Clean image column BEFORE use
df["ImageURL"] = df["ImageURL"].apply(
    lambda x: x.split("|")[0] if isinstance(x, str) else ""
)


class ProductState(rx.State):

    category: str = ""

    def set_category(self, category: str):
        self.category = category

    @rx.var
    def filtered_products(self) -> list[dict]:

        if self.category == "":
            return df.head(100).to_dict("records")

        category = self.category.lower()

        filtered = df[
            df["Category"]
            .str.lower()
            .str.contains(category, na=False)
        ]

        if filtered.empty:
            return df.head(100).to_dict("records")

        return filtered.head(100).to_dict("records")


def product_card(product):

    return rx.box(

        rx.vstack(

            rx.image(
                src=product["ImageURL"],
                width="110px",
                height="110px",
                object_fit="contain"
            ),

            rx.text(
                product["Name"],
                font_size="12px",
                text_align="center"
            ),

            rx.hstack(

                rx.button(
                    "❤️",
                    size="1",
                    on_click=lambda:
                        CartState.add_to_wishlist(
                            product["Name"],
                            product["ImageURL"]
                        )
                ),

                rx.button(
                    "🛒 Add",
                    size="1",
                    on_click=lambda:
                        CartState.add_to_cart(
                            product["Name"],
                            product["ImageURL"]
                        )
                ),

                rx.button(
                    "Buy",
                    size="1",
                    color_scheme="green",
                    on_click=rx.redirect("/payment")
                ),

                spacing="1"

            ),

            spacing="2",
            align="center"

        ),

        padding="8px",
        border_radius="10px",
        background_color="#1f1f1f",
        width="150px"

    )


def products():

    return rx.vstack(

        rx.heading(
            "Products",
            font_size="28px"
        ),

        rx.divider(),

        rx.grid(

            rx.foreach(
                ProductState.filtered_products,
                product_card
            ),

            columns="5",
            spacing="3"

        ),

        padding="20px"

    )