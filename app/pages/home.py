from nicegui import ui


def home_ui():
    ui.label('Welcome to the Home Page!').classes('text-h4')

    with ui.row():
        ui.button('About', on_click=lambda: ui.open('/about'))
