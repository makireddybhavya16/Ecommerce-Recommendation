import reflex as rx

from ai_recommendation_engine.state.cart_state import CartState


# Single cart item UI
def cart_item(item, index):

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
                    CartState.remove_from_cart(index)
            ),

            spacing="4",
            align="center"

        ),

        padding="10px",
        border="1px solid #ddd",
        border_radius="10px"

    )


def cart():

    return rx.vstack(

        rx.heading(
            "🛒 Your Cart",
            size="7"
        ),

        rx.foreach(
            CartState.cart_items,
            lambda item, i:
                cart_item(item, i)
        ),

        rx.divider(),

        rx.text(
            f"Total Price: ₹{CartState.total_price}",
            font_weight="bold"
        ),

        rx.hstack(

            rx.button(
                "Clear Cart 🗑️",
                color_scheme="red",
                on_click=CartState.clear_cart
            ),

            rx.button(
                "Proceed to Payment 💳",
                color_scheme="green",
                on_click=rx.redirect("/payment")
            ),

            spacing="4"

        ),

        spacing="5",
        padding="20px"

    )