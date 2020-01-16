from flask import Flask, render_template, request

PARTDB = 'db_part.txt'
CIRCUITDB = 'db_circuit.txt'
DB = 'db.txt'

app = Flask(__name__, 
            static_url_path='',
            static_folder='static',
            template_folder='templates')

# load config from this file
app.config.from_object(__name__) 


@app.route("/")
def circuit_design():
    return render_template('gcircuitmain.html')


@app.route('/result',methods = ['POST', 'GET'])
def result():

    if request.method == 'POST':
        circuitlist = ""
        partlist = ""
        strnum = ""
        cirdata = ""
        flag = request.form['flag']
        
        # read part list
        with open(app.config['PARTDB']) as f:
            partlist = f.read().splitlines()
            
        # part list
        partlist_all = []
        partlist_all_short = []
        for p in partlist:
            tmplist = p.split(' ')
            partlist_all.append(tmplist)
            tmpseq = tmplist[len(tmplist)-1]
            tmplist[len(tmplist)-1] = (tmpseq[:25] + '...') if len(tmpseq) > 25 else tmpseq
            partlist_all_short.append(tmplist)
        # get part id
        if len(partlist_all) == 0:
            pid=1
        else:
            pid = int(partlist_all[len(partlist_all)-1][0])+1
            
            
        # read circuit list 
        with open(app.config['CIRCUITDB']) as f:
            circuitlist = f.read().splitlines()
        # get circuit id 
        if len(circuitlist) == 0:
            cid=1
        else:
            cid = int(circuitlist[len(circuitlist)-1].split(' ')[0])+1
            
        # save part
        
        if flag == "circuitinput":
            #circuitlist = request.form.getlist('partchk')
#             print("======"+request.form["partchk"])
            r = open(app.config['PARTDB'], mode='rt')
            y = open(app.config['DB'], mode='a', newline='')
            part1 = (r.readlines())[int(request.form["partchk"])- 1].split(' ')[3].rstrip()
            y.write(part1)
            r.close()
            y.close()
        elif flag == "resetpartdb":
            a = open(app.config['PARTDB'], mode='w')
            a.close()
            partlist_all_short = ""
        elif flag == "resetdb":
            a = open(app.config['DB'], mode='w')
            a.close()
        elif flag == "resetcircuitdb":
            a = open(app.config['CIRCUITDB'], mode='w')
            a.close()
        elif flag == "circuitassembly":
            q1 = open(app.config['DB'])
            circuitlist1 = q1.read()
            q1.close()
            d = open(app.config['CIRCUITDB'], mode='a')
            txtcirdata = "%d %s \n" %(cid, circuitlist1)
            d.write(txtcirdata)
            d.close()
            a = open(app.config['DB'], mode='w')
            a.close()
        elif flag == "partinput":
            name = request.form['name']
            ptype = request.form['type']
            seq = request.form['sequence']
            f = open(app.config['PARTDB'], 'a')
            # random number generation (time)
            data = "%d %s %s %s\n" % (pid, name, ptype, seq)
            f.write(data)
            f.close()
            seq = (seq[:75] + '..') if len(seq) > 75 else seq
            partlist_all_short.append([pid, name, ptype, seq])
        c = open(app.config['DB'], mode='rt')
        cirdata = c.read()
        c.close()
        c1 = open(app.config['CIRCUITDB'], mode='rt')
        circuitlist = c1.readlines()
        c1.close()
        return render_template('gcircuitmain.html', partlist=partlist_all_short, circuitlist=circuitlist, cirdata=cirdata)

