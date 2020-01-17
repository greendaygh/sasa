from flask import Flask, render_template, request

import matplotlib.pyplot as plt
import matplotlib.patches as patches 

app = Flask(__name__)

##Circuit Part
class Part:
    def __init__(self, id, seq, name, type) :
        self.id= id
        self.seq= seq
        self.name= name
        self.type= type
        self.location = ""
    def show_sequence(self):
        print(self.seq)
        return
    def show_location(self):
        print(self.location)
        return
## Circuit Class        
class Circuit:
    def __init__(self, id, name, type):
        self.id=id
        self.name=name
        self.seq= ""
        self.type=type
        self.parts= [] 
    def set_sequence(self):
        for p in self.parts:
            self.seq+=p.seq
        return
    def show_sequence(self):
        print(self.seq)
        return
    def show_parts(self):
        for p in self.parts:
            print(p.name)
        return
    def set_parts(self, parts):
        self.parts = parts
        return
    def set_location(self):
        l=1
        for p in self.parts:
                p.location = l
                l+=len(p.seq)
        return
    def show_sequence(self):
        x=0
        fig2 = plt.figure(figsize=(10,10))
        plt.axis('off')
        for i in self.parts: 
             show_gene(fig2, i.type, len(i.seq), x/10)
             x+=len(i.seq)/10
            
            
        fig2.savefig("genegraphics.png",format="png")
        
        
        
        
        return
def show_gene(fig2, typ, leng, location):
    ax2 = fig2.add_subplot(1,1,1)
    if typ=='Promoter':
        ax2.add_patch(
        patches.Rectangle(
        (location, 0.2),
        int(leng)/100,
        0.3,
        color='c'
        ) )
    if typ=='RBS':
        ax2.add_patch(
        patches.Rectangle(
        (location, 0.2),
        int(leng)/100,
        0.1,
        color='m'
        ) )
    if typ=='CDS':
        ax2.add_patch(
        patches.Rectangle(
        (location, 0.2),
        int(leng)/100,
        0.1,
        color='y'
        ) )
    if typ=='Terminator':
        ax2.add_patch(
        patches.Rectangle(
        (location, 0.2 ),
        int(leng)/100,
        0.1,
        color='g'
        ))
'''                
@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/eggplant')
def eggplant_from_html():
    return render_template("eggplant.html")

@app.route('/grape')
def grape_from_html():
    return render_template("grape.html")

@app.route('/banana_party', methods=['post'])
def post():
    value = request.form['id']
    return value
'''

from Bio.Seq import Seq
from Bio.Alphabet import generic_dna
@app.route('/count')
def count_from_html():
    return render_template("count.html")
@app.route('/length', methods=['post'])
def count_Length():
    value = request.form['l_id']
    my_dna=Seq(value)
    return "Number of base pairs: "+str(len(my_dna))+"\n"+"Number of Adenine: "+str(my_dna.count("A"))+"\n"+"Number of Thymine: "+str(my_dna.count("T"))+"\n"+"Number of Guanine: "+str(my_dna.count("G"))+"\n"+"Number of Citricine: "+str(my_dna.count("C"))

@app.route('/display')
def save():
    apro=Part(1, "AGC", "Ap", "Promoter")
    arbs=Part(2, "TTG", "Ar", "RBS")
    acds=Part(3, "ACC", "Ac", "CDS")
    brbs=Part(4, "CCC", "Bc", "CDS")
    crbs=Part(6, "TAG", "Cr", "RBS")
    bcds=Part(7, "ATC", "Bc", "CDS")
    drbs=Part(8, "CTC", "Dc", "CDS")
    ater=Part(9, "ATT", "At", "Terminator")
    acircuit=Circuit(1, "circuit A", "biosensor")
    acircuit.set_parts([apro,arbs,acds,apro,arbs,acds,acds,brbs,crbs,bcds,drbs,brbs,crbs, bcds, drbs, ater])
    acircuit.set_sequence()
    acircuit.show_sequence()
    return
def display_pic():
    return render_template("graphic_test.html")   