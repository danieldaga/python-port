import reflex as rx
from python_port.components.link_button import link_button

def links() -> rx.Component:
    return rx.vstack(
        link_button("linkedIn"),
        link_button("github"),
        link_button("telefono"),
        link_button("discord"),
    )