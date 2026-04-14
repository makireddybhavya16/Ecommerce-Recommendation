import reflex as rx

def payment():

    return rx.vstack(

        rx.heading("Payment Page"),

        rx.text(
            "Click below to make payment"
        ),

        rx.button(
            "Pay with Razorpay",
            on_click=lambda: rx.window_open(
                "https://rzp.io/l/testpayment"
            )
        )
    )