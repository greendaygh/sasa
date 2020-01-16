from flask import Flask, render_template, request

app = Flask(__name__,
           static_url_path='', 
           static_folder='static',
           template_folder='templates')


# @app.route("/")
# def helloworld():
#     return "Hellow world!!"


@app.route("/hello")
def helloworld_from_html():
    return render_template('hello.html')

@app.route("/html_test")
def html_form_test():
#     return render_template('html_test.html')
    return render_template('mdboost.html')

@app.route("/")
def circuit_design():
    return render_template('gcircuitmain.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
    
    if request.method == 'POST':
        circuitlist = ""
        partlist = ""
        flag = request.form['flag']
        
        # read part list
        with open("c:\kribb\sasa\partdb.txt") as f:
            partlist = f.read().splitlines()
            
        # convert to 2dim list  
        partlist_all = []
        partlist_all_short = []
        for p in partlist:
            tmplist = p.split(' ')
            partlist_all.append(tmplist)
            tmpseq = tmplist[len(tmplist)-1]
            tmplist[len(tmplist)-1] = (tmpseq[:25] + '...') if len(tmpseq) > 25 else tmpseq
            partlist_all_short.append(tmplist)
        
        # get pid
        if len(partlist_all) == 0:
            pid=1
        else:
            pid = int(partlist_all[len(partlist_all)-1][0])+1
            
        # read circuit list 
        with open("c:\kribb\sasa\circuitdb.txt") as f:
            circuitlist = f.read().splitlines()
            
        if len(circuitlist) == 0:
            cid=1
        else:
            cid = int(circuitlist[len(circuitlist)-1].split(' ')[0])+1
            
        # save part
        if flag == "partinput":
            name = request.form['name']
            ptype = request.form['type']
            seq = request.form['sequence']
            f = open("C:\kribb\sasa\partdb.txt", 'a')
            # random number generation (time)
            data = "%d %s %s %s\n" % (pid, name, ptype, seq)
            f.write(data)
            f.close()
            seq = (seq[:75] + '..') if len(seq) > 75 else seq
            partlist_all_short.append([pid, name, ptype, seq])
        
        # circuit assembly 
        elif flag == "circuitassembly":
            circuitlist = request.form.getlist('partchk')
            
#         print([i for i in circuitlist])
        return render_template('gcircuitmain.html', partlist=partlist_all_short, circuitlist=circuitlist)
