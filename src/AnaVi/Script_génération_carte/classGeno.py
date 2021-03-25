
class Geno:
    # constructor
    def __init__(self):
        # integer : num
        self.strain = None
        # integer : is the daughter of..
        self.daughter = None
        # String : Genotype
        self.genotype = None
        # dictionary containing the mutations with their ec number
        self.mutation = {}

    def add_trick(self, trick):
        self.tricks.append(trick)
