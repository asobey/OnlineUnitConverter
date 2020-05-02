#!python3

from flask import Flask, render_template, request
from simpleeval import simple_eval
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
            inch = simple_eval(request.form['inch'])
            mm = inch * 25.4
            to_mm = f'{inch * 25.4:.4g} mm'
            return render_template('app.html', to_mm=to_mm)
        if request.form['mm']:
            mm = simple_eval(request.form['mm'])
            to_inch = f'{mm / 25.4:.4g} in'
            return render_template('app.html', to_inch=to_inch)
        if request.form['lbf']:
            lbf = simple_eval(request.form['lbf'])
            to_kgf = f'{lbf / 2.20462:.4g} kgf'
            to_N = f'{lbf * 4.44822:.4g} N'
            return render_template('app.html', to_kgf=to_kgf, lbf_to_N=to_N)
        if request.form['kgf']:
            kgf = simple_eval(request.form['kgf'])
            to_lbf = f'{kgf * 2.20462:.4g} lbf'
            to_N = f'{kgf * 9.80665:.4g} N'
            return render_template('app.html', to_lbf=to_lbf, kgf_to_N=to_N)
        # PRESSURE
        if request.form['psi']:
            psi = simple_eval(request.form['psi'])
            to_Pa = f'{psi * 6894.76:.4g} Pa'
            to_MPa = f'{psi * 0.00689476:.4g} MPa'
            return render_template('app.html', to_Pa=to_Pa, to_MPa=to_MPa)
        if request.form['Pa']:
            Pa = simple_eval(request.form['Pa'])
            to_psi = f'{Pa / 6894.76:.4g} psi'
            to_ksi = f'{Pa / 6.89476:.4g} ksi'
            return render_template('app.html', to_psi=to_psi, to_ksi=to_ksi)
        # TEMPERATURE
        if request.form['F']:
            F = simple_eval(request.form['F'])
            to_C = f'{(F-32)*5/9:.4g}C'
            to_K = f'{(F-32)*5/9+273.15:.4g}K'
            return render_template('app.html', to_C=to_C, to_K=to_K)
        if request.form['C']:
            C = simple_eval(request.form['C'])
            to_F = f'{(C*9/5+32):.4g}F'
            C_to_K = f'{(C+273.15):.4g}K'
            return render_template('app.html', to_F=to_F, C_to_K=C_to_K)
        else:
            return render_template('app.html')

