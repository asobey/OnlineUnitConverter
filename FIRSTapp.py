# REFERENCE: https://www.youtube.com/watch?v=ia0rvIfxPFc

from flask import Flask, render_template, request

# Declare the App
app = Flask(__name__)


@app.route('/')  # Start the app route ('/')
def main():
    print('started')
    return render_template('app.html')


# Form Submission Route
@app.route('/send', methods=['POST'])
def send():
    if request.method == 'POST':
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operation = request.form['operation']

        if operation == 'add':
            result = num1 + num2
            return render_template('app.html', result=result)
        elif operation == 'subtract':
            result = num1 - num2
            return render_template('app.html', result=result)
        elif operation == 'multiply':
            result = num1 * num2
            return render_template('app.html', result=result)
        elif operation == 'divide':
            result = num1 / num2
            return render_template('app.html', result=result)
        else:
            return render_template('app.html')

