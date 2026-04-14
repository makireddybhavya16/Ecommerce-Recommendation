import reflex as rx

from ai_recommendation_engine.state.cart_state import CartState


# Single wishlist item
def wishlist_item(item, index):

    return rx.box(

        rx.hstack(

            rx.image(
                src=item["image"],
                width="60px",
                height="60px"
            ),

            rx.text(
                item["name"]
            ),

            rx.button(
                "Remove ❌",
                color_scheme="red",
                on_click=lambda:
                    CartState.remove_from_wishlist(index)
            ),

            spacing="4",
            align="center"

        ),

        padding="10px",
        border="1px solid #ddd",
        border_radius="10px"

    )


def wishlist():

    return rx.vstack(

        rx.heading(
            "My Wishlist ❤️",
            size="7"
        ),

        rx.cond(

            # If wishlist has items
            CartState.wishlist_items.length() > 0,

            rx.vstack(

                rx.foreach(
                    CartState.wishlist_items,
                    lambda item, i:
                        wishlist_item(item, i)
                )

            ),

            # If empty
            rx.vstack(

                rx.text(
                    "Your saved products will appear here."
                ),

                rx.button(
                    "Go to Products",
                    on_click=rx.redirect("/products")
                )

            )

        ),

        padding="20px",
        spacing="5"

    )