import reflex as rx

def header() -> rx.Component:
    return rx.vstack(
        rx.avatar(
            name="Daniel García",
            size="xl",
            bg="blue",
        ),
        rx.text("@danieldaga"),
        rx.text("lorem"),
    )