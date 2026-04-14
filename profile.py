import reflex as rx

from ai_recommendation_engine.pages.login import LoginState
from ai_recommendation_engine.state.cart_state import CartState


def profile():

    return rx.center(

        rx.vstack(

            # Title
            rx.heading(
                "My Profile 👤",
                font_size="32px"
            ),

            rx.divider(),

            # Profile Card
            rx.box(

                rx.vstack(

                    # Profile Image
                    rx.image(
                        src="https://cdn-icons-png.flaticon.com/512/3135/3135715.png",
                        width="100px",
                        height="100px",
                        border_radius="50%"
                    ),

                    # USER DETAILS (Dynamic)
                    rx.text(
                        f"Name: {LoginState.user_id}",
                        font_size="18px"
                    ),

                    rx.text(
                        f"Email: {LoginState.user_id}",
                        font_size="16px"
                    ),

                    rx.divider(),

                    # ACCOUNT SUMMARY
                    rx.hstack(

                        # CART
                        rx.box(

                            rx.vstack(

                                rx.text(
                                    "🛒 Cart Items",
                                    font_weight="bold"
                                ),

                                rx.text(
                                    CartState.cart_count
                                )

                            ),

                            padding="12px",
                            border_radius="10px",
                            background_color="#1f1f1f",
                            width="120px",
                            align="center"

                        ),

                        # WISHLIST
                        rx.box(

                            rx.vstack(

                                rx.text(
                                    "❤️ Wishlist",
                                    font_weight="bold"
                                ),

                                rx.text(
                                    CartState.wishlist_count
                                )

                            ),

                            padding="12px",
                            border_radius="10px",
                            background_color="#1f1f1f",
                            width="120px",
                            align="center"

                        ),

                        # ORDERS
                        rx.box(

                            rx.vstack(

                                rx.text(
                                    "📦 Orders",
                                    font_weight="bold"
                                ),

                                rx.text(
                                    "0"
                                )

                            ),

                            padding="12px",
                            border_radius="10px",
                            background_color="#1f1f1f",
                            width="120px",
                            align="center"

                        ),

                        spacing="5"

                    ),

                    rx.divider(),

                    # LOGOUT BUTTON
                    rx.link(

                        rx.button(
                            "Logout",
                            color_scheme="red",
                            size="3"
                        ),

                        href="/"

                    ),

                    spacing="4",
                    align="center"

                ),

                padding="30px",
                border_radius="15px",
                background_color="#121212",
                width="350px"

            ),

            spacing="5",
            align="center"

        ),

        height="100vh"

    )