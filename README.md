Welcome to My Webpage, it is a rudimentary form page/Flask application

The HTML and CSS are rather straightforward but I will give a breakdown of what I leveraged in Flask's library to create this sample webpage:

-from flask import Flask, request is importing the Flask module and the request object.

-app = Flask(__name__) is creating a new web application object with the name app.

-@app.route('/submit_form', methods=['POST']) is a decorator that Flask provides to assign URLs in our app to functions easily. The '/submit_form' URL is where your form data will be sent when the form is submitted.

def submit_form(): is a new function that will be called when the form is submitted.
if request.method == 'POST': is a conditional statement that checks if the HTTP method is POST. If it is, it means that the form has been submitted.

- name = request.form.get('name') is getting the data from the form input with the name 'name'.

- return 'Form data received. Name: ' + name is returning a string that includes the name from the form.

- if __name__ == '__main__': app.run(debug=True) is using a conditional statement to ask Python to run the Flask web server if the script is being run directly. The debug=True argument enables debug mode for your Flask application.