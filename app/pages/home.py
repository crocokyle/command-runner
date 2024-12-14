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
            # Dark Mode Toggle
            toggle = ui.switch('Dark/Light Mode', on_change=dark.toggle)

    # Table Data
    columns = [
        {'name': 'name', 'label': 'Name', 'field': 'name', 'sortable': True},
        {'name': 'path', 'label': 'Path', 'field': 'path', 'sortable': True},
        {'name': 'terminal', 'label': 'Terminal', 'field': 'terminal', 'sortable': True},
        {'name': 'venv', 'label': 'Virtual Environment', 'field': 'venv', 'sortable': True},
        {'name': 'popup', 'label': 'Popup', 'field': 'popup', 'sortable': True},
        {'name': 'log', 'label': 'Log', 'field': 'log', 'sortable': True},
    ]
    rows = [
        {
            'name': 'Build Integration',
            'path': 'C:\\Users\\Kyle\\code\\command-runner\\app\\main.py',
            'terminal': 'PowerShell',
            'venv': 'command-runner (Python 3.10)',
            'popup': 'true',
            'log': 'true'
        },
        {
            'name': 'Refresh Environment',
            'path': 'C:\\Users\\Kyle\\code\\command-runner\\app\\main.py',
            'terminal': 'PowerShell',
            'venv': 'command-runner (Python 3.10)',
            'popup': 'true',
            'log': 'false'
        },
        {
            'name': 'Build Integration',
            'path': 'C:\\Users\\Kyle\\code\\command-runner\\app\\main.py',
            'terminal': 'PowerShell',
            'venv': 'command-runner (Python 3.9)',
            'popup': 'false',
            'log': 'false'
        },
    ]

    # Add Table to the Page
    ui.table(columns=columns, rows=rows).classes('w-full max-w-none')
