from nicegui import ui
from app.utils import get_app_version

def home_ui():
    dark = ui.dark_mode()
    dark.enable()

    with ui.header().classes('items-center justify-between bg-blue-500 text-white'):
        # Left side: Logo/Brand
        ui.label(f'Command Runner v{get_app_version()}').classes('text-h5 font-bold')

        # Right side: Navigation and Dark Mode toggle
        with ui.row().classes('gap-4'):
            ui.link('Home', '/').classes('text-white text-lg')
            ui.link('About', '/about').classes('text-white text-lg')

            # Dark Mode Toggle
            toggle = ui.switch('Dark/Light Mode', on_change=dark.toggle)

    # Main content for the homepage
