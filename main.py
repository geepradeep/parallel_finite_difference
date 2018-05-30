#!/usr/bin/python

import numpy as np
import sys
from create_fd_geoms import create_fd_geoms

def main(inputfile):
    xyz = np.genfromtxt(inputfile, delimiter='', invalid_raise=False, usecols=np.arange(0,4), dtype=None)
    fd_step_size=0.001      # Corresponds to 0.001 Angstroms, Q-Chem and Gaussian default
    input_method = 1        # Switch between Q-Chem and Gaussian inputs for FD calculations
    create_fd_geoms(xyz, fd_step_size, input_method)

main(sys.argv[1])
