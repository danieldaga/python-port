import reflex as rx
from python_port.components.navbar import navbar
from python_port.views.header.header import header
from python_port.views.links.links import links
from python_port.components.footer import footer
import python_port.styles.styles as styles

class State(rx.State):
    pass

def index() -> rx.Component:
     return rx.box(
                navbar(),
                rx.center(
                    rx.vstack(
                            header(),
                            links(),
                            max_width=styles.MAX_WIDTH,
                            widht="100%",
                            margin_y=styles.Size.DEFAULT.value
                            )
                ),
                footer()
     )



app = rx.App(
     style=styles.BASE_STYLE
)
app.add_page(index)
app.compile()