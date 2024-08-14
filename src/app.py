"""
app.py - A simple Flask application that returns 'Hello, world!' on the root URL.
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    """
    Returns a greeting string 'Hello, world!'.
    """
    return "Hello, world!"

if __name__ == "__main__":
    # Run the app on all IPs (0.0.0.0) and port 80
    app.run(host='0.0.0.0', port=80)
