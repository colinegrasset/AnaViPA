import numpy as np


class Geno:
    # constructor
    def __init__(self):
        # integer : num
        self.strain = None
        # integer : is the daughter of..
        self.daughter = None
        # String : Genotype
        self.genotype = None

    def add_trick(self, trick):
        self.tricks.append(trick)
