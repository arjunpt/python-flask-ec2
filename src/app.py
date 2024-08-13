"""
app.py - A simple Flask application with an intentional security vulnerability.
"""

from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    """
    Returns a greeting string 'Hello, world!'.
    """
    return "Hello, world!"

@app.route("/vulnerable")
def vulnerable():
    """
    An intentionally vulnerable endpoint that executes arbitrary code.
    """
    user_input = request.args.get("input")
    # WARNING: The use of eval is insecure and should never be used with untrusted input.
    result = eval(user_input)
    return str(result)

if __name__ == "__main__":
    app.run()
