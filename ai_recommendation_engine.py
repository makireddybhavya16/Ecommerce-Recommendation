import reflex as rx

from .pages.home import home
from .pages.products import products
from .pages.recommendations import recommendations
from .pages.cart import cart
from .pages.login import login
from ai_recommendation_engine.pages.payment import payment
from ai_recommendation_engine.pages.success import success

from .pages.wishlist import wishlist
from .pages.orders import orders
from .pages.profile import profile


app = rx.App()

# Default page → LOGIN
app.add_page(login, route="/")

app.add_page(home, route="/home")
app.add_page(products, route="/products")
app.add_page(recommendations, route="/recommendations")
app.add_page(cart, route="/cart")
app.add_page(payment, route="/payment")
app.add_page(success, route="/success")

# NEW PAGES
app.add_page(wishlist, route="/wishlist")
app.add_page(orders, route="/orders")
app.add_page(profile, route="/profile")