#!/usr/bin/env python3
from flask import Flask

# Initialize Flask app
app = Flask(__name__)

# Existing models array (provided)
existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']


@app.route('/')
def index():
    """Default route - returns welcome message."""
    return "Welcome to Flatiron Cars"


@app.route('/<model>')
def get_model(model):
    """
    Dynamic route for car models.
    
    Args:
        model: String - car model name from URL
        
    Returns:
        String message indicating if model exists or not
    """
    if model in existing_models:
        return f"Flatiron {model} is in our fleet!"
    else:
        return f"No models called {model} exists in our catalog"


if __name__ == '__main__':
    # Run the Flask app in debug mode
    app.run(debug=True, port=5000)