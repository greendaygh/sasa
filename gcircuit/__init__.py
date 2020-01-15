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
        circuitlist = ""
        partlist = ""
        flag = request.form['flag']
        with open("c:\kribb\sasa\db.txt") as f:
            partlist = f.read().splitlines()
        if len(partlist) == 0:
            id=1
        else:
            id = int(partlist[len(partlist)-1].split(' ')[0])+1
        
        if flag == "partinput":
            name = request.form['name']
            ptype = request.form['type']
            seq = request.form['sequence']
            f = open("C:\kribb\sasa\db.txt", 'a')
            # random number generation (time)
            data = "%d %s %s %s\n" % (id, name, ptype, seq)
            f.write(data)
            f.close()
            partlist.append(data)
        
        elif flag == "circuitinput":
            circuitlist = request.form['partchk']
        
#         result = {'partlist':partlist, 'circuitlist':circuitlist}
        print(circuitlist) 
        return render_template('gcircuitmain.html', partlist=partlist, circuitlist=circuitlist)
