import reflex as rx

class FormErrorState(rx.State):
    name: str

    @rx.var
    def is_error(self) -> bool:
        return len(self.name) <= 3

def form_footer() -> rx.Component:
    return rx.form_control(
            rx.input(
                placeholder="name",
                on_blur=FormErrorState.set_name,
            ),
            rx.cond(
                FormErrorState.is_error,
                rx.form_error_message(
                    "Name should be more than four characters"
                ),
                rx.form_helper_text("Enter name"),
            ),
            is_invalid=FormErrorState.is_error,
            is_required=True,
        ),