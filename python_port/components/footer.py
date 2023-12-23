import reflex as rx
from python_port.components.form_footer import form_footer
import datetime
    
def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
        src="favicon.ico"
        ),
        rx.link(
            f"© {datetime.date.today().year} Daniel Garcia Dev.",
            href="https://danielgr.com",
            is_external=True
        ),
        rx.text(
            "♠ Diseñado con pasión y codificado con creatividad. ♠",
        ),
            # width="full",
            position="sticky",
            bg="#314299",
            color="#00BBF9",
            padding_x="16px",
            z_index="5",
    )