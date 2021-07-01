import argparse

import numpy as np
from matplotlib import pyplot as plt
import matplotlib

from env.problem import g_
from parameters import font


# parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('-o', '--outfile')
args = parser.parse_args()


matplotlib.rc('font', **font)

fig, ax = plt.subplots()
fig.set_size_inches(3, 2.25)

x = np.linspace(0, 1, 100)

ax.plot(x, np.vectorize(g_)(x), color='blue', zorder=0,
        label=r'$g(x, 1)$')
ax.legend(loc='upper left')

plt.tight_layout()
plt.savefig(args.outfile)




