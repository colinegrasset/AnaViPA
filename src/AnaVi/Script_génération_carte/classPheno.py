class Pheno:
    #constructeur
    def __init__(self):
        # integer : num
        self.strain = None
        # integer : first do
        self.do1 = None
        # integer: second do
        self.do2 = None
        # integer: third do
        self.do3 = None
        # list de do
        self.listdo = None

    def add_trick(self, trick):
        self.tricks.append(trick)