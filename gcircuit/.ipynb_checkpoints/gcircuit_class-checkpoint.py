from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

class Part:
    def __init__(self, id, name, seq, type):
        self.id = id
        self.name = name
        self.seq = seq
        self.type = type
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
        self.set_location()
    def set_location(self):
        l=1
        for p in self.parts:
                p.location = l
                l+=len(p.seq)