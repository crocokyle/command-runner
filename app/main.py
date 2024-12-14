from flask import Flask

app = Flask(__name__)

# Define Routes
@app.route('/')
def home():
    return "Blonk"

# Run App
if __name__ in {"__main__", "__mp_main__"}:
    app.run(port=8080, debug=True)