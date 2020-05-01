from flask import Flask, render_template, request
# import logging

# logging.basicConfig(level=logging.DEBUG)

# Declare the App
app = Flask(__name__)


@app.route('/')  # Start the app route ('/')
def main():
    print('-----------------started-----------------')
    return render_template('app.html')


# Form Submission Route
@app.route('/send', methods=['POST'])
def send():
    if request.method == 'POST':
        # app.logger.info('INCH===============' + request.form['inch'])

        if request.form['inch']:
            inch = float(request.form['inch'])
            to_mm = f'{inch * 25.4} mm'
            return render_template('app.html', to_mm=to_mm)
        if request.form['mm']:
            mm = float(request.form['mm'])
            to_inch = f'{mm / 25.4} in'
            return render_template('app.html', to_inch=to_inch)
        if request.form['pound']:
            pound = float(request.form['pound'])
            result = f'{pound / 2.20462} mm'
            return render_template('app.html', result=result)
        if request.form['kg']:
            kg = float(request.form['kg'])
            result = f'{kg * 2.20462} mm'
            return render_template('app.html', result=result)
        else:
            return render_template('app.html')

