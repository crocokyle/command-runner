from nicegui import ui
from app.pages.home import home_ui


# Define Routes
@ui.page('/')
def home():
    home_ui()


# Run App
if __name__ in {"__main__", "__mp_main__"}:
    ui.run(title='My NiceGUI Project', port=8080)
