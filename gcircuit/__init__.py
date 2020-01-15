from flask import Flask, render_template, request
app = Flask(__name__)

class Part:
    def __init__(self, id, seq, name, type) :
        self.id= id
        self.seq= seq
        self.name= name
        self.type= type
        self.location = ""
    def show_sequence(self):
        print(self.seq)
    def show_location(self):
        print(self.location)
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
    def show_sequence(self):
        print(self.seq)
    def show_parts(self):
        for p in self.parts:
            print(p.name)
    def set_parts(self, parts):
        self.parts = parts
    def set_location(self):
        l=1
        for p in self.parts:
                p.location = l
                l+=len(p.seq)
                
                
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

from Bio.Seq import Seq
from Bio.Alphabet import generic_dna

@app.route('/count')
def count_A_from_html():
    return render_template("count.html")

@app.route('/length', methods=['post'])
def count_Length():
    value = request.form['l_id']
    my_dna=Seq(value)
    return "Number of base pairs: "+str(len(my_dna))+"\n"+"Number of Adenine: "+str(my_dna.count("A"))+"\n"+"Number of Thymine: "+str(my_dna.count("T"))+"\n"+"Number of Guanine: "+str(my_dna.count("G"))+"\n"+"Number of Citricine: "+str(my_dna.count("C"))

@app.route('/idparts', methods=['post'])
def count_Length():
    
    value = request.form['p_id']
    my_part=Seq(value)
    return 