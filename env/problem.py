import dolfin
import numpy as np
import sympy as sym

# dolfin.set_log_level(40)

# set the mesh, the space, and the measure on the boundary
mesh = dolfin.UnitSquareMesh(32, 32)
V = dolfin.FunctionSpace(mesh, "CG", 1)

# define the boundary
active_boundary = dolfin.CompiledSubDomain('near(x[1], 1) && on_boundary')
passive_boundary = dolfin.CompiledSubDomain('near(x[1], 0) && on_boundary')
boundary_markers = dolfin.MeshFunction('size_t', mesh, mesh.topology().dim()-1)
active_boundary.mark(boundary_markers, 1)
passive_boundary.mark(boundary_markers, 2)

ds = dolfin.Measure('ds', domain=mesh, subdomain_data=boundary_markers)

# set the time domain
T, Nt = 100, 500
dt = T / Nt
time_line = np.linspace(0, T, num=Nt, endpoint=False)
implicitness = .5

# set the coefficients
alpha = 4.
kappa = 1.

temp_amb = 25.
theta_init = dolfin.project(temp_amb, V)

# define the active boundary condition
x = sym.symbols('x[0]')
g_ = sym.poly((x**4 - 2*x**3 + x**2))
g = dolfin.Expression(sym.ccode(g_.as_expr()), degree=g_.degree())
control = 10**3 * np.sqrt(time_line / T)
# control = 10**3 * (time_line / T)**2