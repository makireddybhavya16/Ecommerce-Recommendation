import reflex as rx

from ai_recommendation_engine.pages.products import ProductState


def navbar():

    return rx.hstack(

        rx.text(
            "🛍️ AI Store",
            font_size="20px",
            font_weight="bold"
        ),

        rx.spacer(),

        rx.link("Home", href="/home"),

        rx.link("Products", href="/products"),

        rx.link("Recommendations", href="/recommendations"),

        rx.link("Wishlist ❤️", href="/wishlist"),

        rx.link("Cart 🛒", href="/cart"),

        rx.link("Profile 👤", href="/profile"),

        spacing="5",

        width="100%",
        padding="15px",
        border_bottom="1px solid gray"

    )


def category_card(title, image_url, category):

    return rx.box(

        rx.vstack(

            rx.image(
                src=image_url,
                width="150px",
                height="150px",
                border_radius="12px"
            ),

            rx.text(
                title,
                font_weight="bold",
                font_size="16px"
            ),

            align="center"

        ),

        cursor="pointer",

        on_click=lambda: [
            ProductState.set_category(category),
            rx.redirect("/products")
        ]

    )


def home():

    return rx.vstack(

        navbar(),

        rx.heading(
            "AI Enabled Recommendation Engine",
            font_size="32px"
        ),

        rx.text(
            "Welcome to Home Page",
            font_size="18px"
        ),

        rx.divider(),

        rx.heading(
            "Shop by Category",
            font_size="24px"
        ),

        rx.hstack(

            category_card(
                "Household",
                "https://images.unsplash.com/photo-1581578731548-c64695cc6952",
                "household"
            ),

            category_card(
                "Grooming",
                "https://images.unsplash.com/photo-1621605815971-fbc98d665033",
                "shave"
            ),

            category_card(
                "Fragrance",
                "https://images.unsplash.com/photo-1611930022073-b7a4ba5fcccd",
                "fragrance"
            ),

            category_card(
                "Hair Care",
                "https://images.unsplash.com/photo-1522337360788-8b13dee7a37e",
                "hair"
            ),

            category_card(
                "Makeup",
                "https://images.unsplash.com/photo-1512496015851-a90fb38ba796",
                "makeup"
            ),

            spacing="6"

        ),

        padding="20px"

    )