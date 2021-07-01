import json
import argparse
import numpy as np

from env.problem import dt
from env.parameters import times

# parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('-o', '--outfile')
parser.add_argument('-e', '--evo')
args = parser.parse_args()


evo = np.load(args.evo)

report = {dt*t: [evo[t].max(), evo[t].min()] for t in times}

with open(args.outfile, 'w') as report_file:
    json.dump(report, report_file, indent=4)
