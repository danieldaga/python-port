import reflex as rx
from python_port.components.link_button import link_button

def links() -> rx.Component:
    return rx.vstack(
        link_button("LinkedIn", "https://www.linkedin.com/in/daniel-garc%C3%ADa-rodr%C3%ADguez-71548948/"),
        link_button("Github", "https://github.com/danieldaga"),
        link_button("Whatsapp", "https://wa.me/605627423"),
        link_button("Email", "mailto:dagarodriguez93@gmail.com"),
        link_button("Discord", ""),
    )