import reflex as rx


def success():

    return rx.vstack(

        rx.heading(
            "Order Successful 🎉",
            size="7"
        ),

        rx.text(
            "Your order has been placed successfully."
        ),

        rx.button(
            "Continue Shopping",
            href="/"
        ),

        spacing="4",
        padding="20px"
    )