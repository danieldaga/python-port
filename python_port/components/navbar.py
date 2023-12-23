import reflex as rx

def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
            "Daniel García Developer",
            height="40px",
            ),
            # width="full",
            position="sticky",
            bg="#314299",
            color="#00BBF9",
            padding_x="16px",
            z_index="5",
        )