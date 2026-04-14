import reflex as rx


def payment():

    return rx.center(

        rx.vstack(

            rx.heading(
                "Razorpay Payment Gateway (Demo)",
                size="6"
            ),

            rx.text(
                "Total Amount: ₹902"
            ),

            rx.box(

                rx.text(
                    "Processing secure mock payment..."
                ),

                rx.button(
                    "Simulate Payment Success",
                    color_scheme="green",
                    on_click=rx.redirect("/success")
                ),

                padding="20px",
                border="1px solid #ddd",
                border_radius="10px"

            ),

            spacing="4"

        ),

        min_height="80vh"
    )