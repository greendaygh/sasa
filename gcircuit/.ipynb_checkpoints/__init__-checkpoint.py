from flask import Flask, render_template, request
import os 

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

UPLOAD_FOLDER = "/images/"

# model function
def dP_dt(P, t, a, b, c, d):
    return [(a- b*P[0]), (c*P[0] - d*P[1])]

app = Flask(__name__,
           static_url_path='', 
           static_folder='static',
           template_folder='templates')

# load config from this file
app.config.from_object(__name__) 

@app.route('/')
def index():
    params=[50,50,50,50]
    return render_template('modeling.html', image_file='', params=params)


@app.route('/result',methods = ['POST', 'GET'])
def modeling():
    if request.method == 'POST':
        a = int(request.form['a'])
        b = int(request.form['b'])
        c = int(request.form['c'])
        d = int(request.form['d'])

        ts = np.linspace(0, 3, 100)
        P0 = [1.5, 1.0]
        params = (a, b, c, d)
        Ps = odeint(dP_dt, P0, ts, args=params)
        pro = Ps[:,0]
        rna = Ps[:,1]

        plt.figure()
        plt.plot(ts, pro, "-", label="Protein")
        plt.plot(ts, rna, "-", label="mRNA")
        plt.xlabel("Time")
        plt.ylabel("Value")
        plt.legend();

        fig=plt.gcf()
        fig.savefig('gcircuit/static/images/myfile.png',dpi=fig.dpi)
        full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'myfile.png')
        return render_template('modeling.html', image_file=full_filename, params=params)

