# Import Flask module
from flask import Flask, render_template, request

# Create an instance of Flask class
app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def home():
    # Render the form.html template
    return render_template('form.html')

# Define a route for the result page
@app.route('/result', methods=['POST'])
def result():
    # Get the values and operation from the form
    value1 = float(request.form['value1'])
    value2 = float(request.form['value2'])
    operation = request.form['operation']

    # Perform the calculation based on the operation
    if operation == '+':
        result = value1 + value2
    elif operation == '-':
        result = value1 - value2
    elif operation == '*':
        result = value1 * value2
    elif operation == '/':
        result = value1 / value2
    else:
        result = 'Invalid operation'

    # Render the result.html template with the result
    return render_template('result.html', result=result)

# Run the app in debug mode
if __name__ == '__main__':
    app.run(debug=True)
