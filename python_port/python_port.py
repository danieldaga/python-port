import reflex as rx

class State(rx.State):
    pass

def index() -> rx.Component:
    return rx.button_group(
        rx.button("Button 1", color="red"),
        rx.button("Button 2", color="blue"),
        rx.button("Button 3", color="green"),
    )

app = rx.App()
app.add_page(index)
app.compile()