import reflex as rx

def header() -> rx.Component:
    return rx.vstack(
        rx.avatar(
            name="Daniel García",
            size="xl",
            bg="blue",
        ),
        rx.text("@danieldaga"),
        rx.text("Hola! Mi nombre es Daniel Garcia."),
        rx.text("Soy desarrollador Full Stack con experiencia en TypeScript, React (Next.js), Tailwind, HTML5, CSS3, y JavaScript ES6. Experiencia en la integración con APIs, así como en el desarrollo y despliegue de aplicaciones utilizando Firebase, Supabase, y Node.js. Profundo conocimiento de control de versiones con GitHub y metodologías Agile para la gestión eficiente de proyectos. Además, poseo habilidades en Python y el marco de desarrollo Express para la creación de aplicaciones web robustas y escalables."),
    )