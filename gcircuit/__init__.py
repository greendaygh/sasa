from flask import Flask, render_template, request

app = Flask(__name__)


# @app.route("/")
# def helloworld():
#     return "Hellow world!!"


@app.route("/hello")
def helloworld_from_html():
    return render_template('hello.html')

@app.route("/html_test")
def html_form_test():
    return render_template('html_test.html')

@app.route("/")
def circuit_design():
    return render_template('gcircuitmain.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
    
    if request.method == 'POST':
        name = request.form['name']
        ptype = request.form['type']
        seq = request.form['sequence']
        f = open("C:\kribb\sasa\db.txt", 'a')
        # random number generation (time)
        data = "%s %s %s\n" % (name, ptype, seq)
        f.write(data)
        f.close()

        with open("c:\kribb\sasa\db.txt") as f:
            result = f.read().splitlines()
        return render_template('gcircuitmain.html', result=result)
