import reflex as rx
from python_port.styles.styles import Size as Size

def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
            "Daniel García Developer",
            ),
            position="sticky",
            bg="#314299",
            color="#00BBF9",
            padding_x=Size.DEFAULT.value,
            padding_y=Size.SMALL.value,
            z_index="5",
            top="0"
        )