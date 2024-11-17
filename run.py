# run.py (entry point to run the Flask app)
from src.app import create_app  # Import the create_app function from src.app

# Create the Flask app using the factory function
app = create_app()

# Run the app if this is the main module
if __name__ == "__main__":
    app.run(debug=True)  # Runs the app in debug mode
