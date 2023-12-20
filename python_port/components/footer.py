import reflex as rx
from python_port.components.form_footer import form_footer
    
def footer() -> rx.Component:
    return rx.hstack(
        form_footer(),
        rx.text(
            "footer con datos"
        )
    )