# from flask import Flask
# app = Flask(__name__)

# @app.route("/")
# def hello():
#     return "Hello World!"

# if __name__ == "__main__":
#     app.run()

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        # this block is only entered when the form is submitted
        name = request.form.get('fname')  # Change 'name' to 'fname'
        return 'Form data received. Name: ' + name  # Modified return statement

if __name__ == '__main__':
    app.run(debug=True)


