from flask import Flask, render_template, request
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna
import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches 

UPLOAD_FOLDER = "/images/"

app = Flask(__name__,
           static_url_path='', 
           static_folder='static',
           template_folder='templates')

app.config.from_object(__name__) 



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
        return None
    def show_location(self):
        print(self.location)
        return None
    
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
        return None
    def show_sequence(self):
        print(self.seq)
        return None
    def show_parts(self):
        for p in self.parts:
            print(p.name)
        return None
    def set_parts(self, parts):
        self.parts = parts
        return None
    def set_location(self):
        l=1
        for p in self.parts:
                p.location = l
                l+=len(p.seq)
        return None
    def make_seq_figure(self):
        x=0
        fig2 = plt.figure(figsize=(4,4))
        plt.axis('off')
        for i in self.parts: 
            show_gene(fig2, i.type, len(i.seq), x/10)
            x+=len(i.seq)/10
        fig2.savefig("gcircuit/static/images/genegraphics.png",format="png")
        return None
    
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
    return None
        

@app.route('/count')
def count_from_html():
    return render_template("count.html")

@app.route('/length', methods=['post'])
def count_Length():
    value = request.form['l_id']
    my_dna=Seq(value)
#     return "Number of base pairs: "+str(len(my_dna))+"\n"+"Number of Adenine: "+str(my_dna.count("A"))+"\n"+"Number of Thymine: "+str(my_dna.count("T"))+"\n"+"Number of Guanine: "+str(my_dna.count("G"))+"\n"+"Number of Citricine: "+str(my_dna.count("C"))
    return None


@app.route('/display', methods=['GET', 'POST'])
def save():
    if request.method=='GET':
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
        acircuit.make_seq_figure()
        full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'genegraphics.png')
        return render_template("graphic_test.html", image_file_name=full_filename) 

