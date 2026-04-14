import reflex as rx

def orders():

    return rx.center(
        rx.vstack(

            rx.heading(
                "My Orders 📦",
                size="7"
            ),

            rx.text(
                "You have no orders yet."
            ),

            rx.button(
                "Start Shopping",
                color_scheme="green",
                on_click=rx.redirect("/home")
            ),

            spacing="4",
            align="center"

        ),
        min_height="80vh"
    )