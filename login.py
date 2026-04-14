import reflex as rx


class LoginState(rx.State):

    user_id: str = ""
    password: str = ""

    is_logged_in: bool = False

    def login(self):

        if self.user_id != "" and self.password != "":
            self.is_logged_in = True
            return rx.redirect("/home")

        else:
            return rx.window_alert(
                "Invalid Login"
            )


def login():

    return rx.center(

        rx.vstack(

            rx.heading(
                "Login Page",
                font_size="32px"
            ),

            rx.input(
                placeholder="User ID",
                on_change=LoginState.set_user_id,
                width="250px"
            ),

            rx.input(
                placeholder="Password",
                type="password",
                on_change=LoginState.set_password,
                width="250px"
            ),

            rx.button(
                "Login",
                on_click=LoginState.login,
                color_scheme="blue"
            ),

            spacing="4"

        ),

        height="100vh"

    )