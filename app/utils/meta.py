import tomli

def get_app_version():
    """Reads the version from pyproject.toml."""
    with open("pyproject.toml", "rb") as f:  # Open the file in binary mode
        data = tomli.load(f)  # Parse the TOML file
        return data["project"]["version"]
