import argparse
import numpy as np
from solver.core import solve_forward
from env.problem import (
        theta_init, alpha, kappa, temp_amb,
        control, g, implicitness, dt, V, ds
        )


# parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('-o', '--outfile')
args = parser.parse_args()


evo = solve_forward(
        theta_init, alpha, kappa, temp_amb,
        control, g, implicitness, dt, V, ds)

np.save(args.outfile, evo)
