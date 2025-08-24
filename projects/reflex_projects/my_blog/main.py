


def new_page():
    return rx.box(
        navbar(),
        rx.vstack(
            rx.heading("New Page", size="xl"),
            rx.text("This is a new page."),
            padding="2em",
        ),
        footer(),
    )

# Add to routes
app.add_page(new_page, route="/new-page")