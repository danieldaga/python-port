import reflex as rx

def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
            "Daniel García Developer",
            height="40px"
            ),
            position="sticky",
            bg="blue",
            padding_x="16px",
            z_index="5",
        )