import reflex as rx
from python_port.components.link_button import link_button
from python_port.components.title import title

def links() -> rx.Component:
    return rx.vstack(
        title("Redes Sociales"),
        link_button(
            "LinkedIn", 
            "Conocemé en LinkdIn", 
            "https://www.linkedin.com/in/daniel-garc%C3%ADa-rodr%C3%ADguez-71548948/"
            ),
        link_button(
            "Discord", 
            "", 
            ""
            ),
        title("Repositorios"),
        link_button(
            "Github", 
            "Visita mis repositorios", 
            "https://github.com/danieldaga"
            ),
        title("Contactame"),
        link_button(
            "Whatsapp", 
            "Envíame un Whatsapp", 
            "https://wa.me/605627423"
            ),
        link_button(
            "Email", 
            "Hablemos por Email", 
            "mailto:dagarodriguez93@gmail.com"
            ),
        width="100%"
    )