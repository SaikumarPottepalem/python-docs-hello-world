# Import Flask module
from flask import Flask

# Create an instance of Flask class
app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def hello():
    # Return the message "Hello World!"
    return "Hello World!"

# Run the app in debug mode
if __name__ == '__main__':
    app.run(debug=True)
