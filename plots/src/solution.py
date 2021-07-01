import argparse

import dolfin
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import colors
import matplotlib

from env.problem import V, Nt
from env.parameters import times

from parameters import font


# parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('-o', '--outfile')
parser.add_argument('-e', '--evo')
args = parser.parse_args()

evo = np.load(args.evo)
theta = dolfin.Function(V)

matplotlib.rc('font', **font)

fig, axes = plt.subplots(1, 4)
fig.set_size_inches(6.5, 3.5)


x = np.linspace(0, 1, 100)
y = np.linspace(0, 1, 100)
x, y = np.meshgrid(x, y)

images = []
for t, ax in zip(times, axes):
    theta.vector().set_local(evo[t])
    z = np.flip(np.vectorize(theta)(x, y), 0)
    images.append(ax.imshow(z, interpolation='bicubic', cmap='plasma'))

vmin = min(image.get_array().min() for image in images)
vmax = max(image.get_array().max() for image in images)
norm = colors.Normalize(vmin, vmax)
for im in images:
    im.set_norm(norm)

fig.colorbar(images[0], ax=axes, orientation='horizontal', fraction=.1)

# plt.tight_layout()
plt.savefig(args.outfile)
