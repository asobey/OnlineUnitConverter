#!python3

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
        sig_figs = 5
        if request.form['Significant_Figures']:
            sig_figs = float(request.form['Significant_Figures'])
        if request.form['inch']:
            inch = float(request.form['inch'])
            mm = inch * 25.4
            to_mm = f'{inch * 25.4:.sig_figs} mm'
            return render_template('app.html', to_mm=to_mm)
        if request.form['mm']:
            mm = float(request.form['mm'])
            to_inch = f'{mm / 25.4:.sig_figs} in'
            return render_template('app.html', to_inch=to_inch)
        if request.form['lbf']:
            lbf = float(request.form['lbf'])
            to_kgf = f'{lbf / 2.20462:.5} kgf'
            to_N = f'{lbf * 4.44822:.5} N'
            return render_template('app.html', to_kgf=to_kgf, lbf_to_N=to_N)
        if request.form['kgf']:
            kgf = float(request.form['kgf'])
            to_lbf = f'{kgf * 2.20462:.5} lbf'
            to_N = f'{kgf * 9.80665:.5} N'
            return render_template('app.html', to_lbf=to_lbf, kgf_to_N=to_N)
        else:
            return render_template('app.html')

