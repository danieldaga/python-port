import reflex as rx
from python_port.components.navbar import navbar
from python_port.views.header.header import header
from python_port.views.links.links import links

class State(rx.State):
    pass

def index() -> rx.Component:
     return rx.vstack(
          navbar(),
          header(),
          links(),
        
          )


app = rx.App()
app.add_page(index)
app.compile()