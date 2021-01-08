# vim: set fileencoding=utf-8 :
import __main__
__main__.pymol_argv = [ 'pymol', '-qc'] # Quiet and no GUI

import sys, time, os
import pymol


def main():
        
    pymol.finish_launching()
    
    
    # Load Structures
    
    pymol.cmd.load('D:/PDB/Q12634/1DOH/1DOH_protein.pdb', '1DOH')
    pymol.cmd.load('D:/PDB/Q12634/1G0N/1G0N_protein.pdb', '1G0N')
    # 1DOH aligned to 1G0N, with alignment object,   
    # object = string: name of alignment object to create {default: (no alignment object)}
    '''
    This returns a list with 7 items:
        
        RMSD after refinement
        Number of aligned atoms after refinement
        Number of refinement cycles
        RMSD before refinement
        Number of aligned atoms before refinement
        Raw alignment score
        Number of residues aligned
     '''
    res =pymol.cmd.align( '1DOH & chain A', '1G0N & chain A' )
    
    print(res)
     
    
if __name__ == '__main__':
	 main() 