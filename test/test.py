from src.app import app

def test_index():
    # Create a test client using the Flask application configured for testing
    with app.test_client() as client:
        # Send a GET request to the index route
        response = client.get("/")
        # Check that the response is "Hello, world!"
        assert response.data == b"Hello, world!"
        # Check that the status code is 200
        assert response.status_code == 200
