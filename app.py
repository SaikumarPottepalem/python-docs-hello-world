from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    message = ""
    if request.method == 'POST':
        login_name = request.form.get('login_name')
        password = request.form.get('password')
        # Add your authentication logic here
        message = "Login successful!"  # This is just a placeholder

    return render_template('login.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
