from dolfin import inner, grad, dx
import dolfin
import numpy as np


def bc_active(control_k, g):
    return - dolfin.Constant(control_k) * g

def bc_passive(kappa, theta, temp_amb):
    return dolfin.Constant(kappa) * (theta - dolfin.Constant(temp_amb))

def avg(u_k, u_kp1, implicitness):
    return implicitness * u_kp1 + (1 - implicitness) * u_k

def a(
        u_k, u_kp1, v,
        alpha, kappa, temp_amb,
        control_k, g, implicitness, dt, ds):

    u_avg = avg(u_k, u_kp1, implicitness)

    a_ = dolfin.Constant(alpha) * (u_kp1 - u_k) * v  * dx\
       + dt * inner(grad(u_avg), grad(v)) * dx\
       + dt * bc_active(control_k, g) * v * ds(1) \
       + dt * bc_passive(kappa, u_avg, temp_amb) * v * ds(2)

    return a_


def solve_forward(
        theta_init, alpha, kappa, temp_amb,
        control, g, implicitness, dt, V, ds):

    # initialize the state functions
    theta_k = dolfin.Function(V)    # stands for theta[k]
    theta_kp1 = dolfin.Function(V)  # stands for theta[k+1]
    # u_kp1 = dolfin.TrialFunction(V)

    # FEM equation setup
    v = dolfin.TestFunction(V)

    Nt = len(control)
    evo = np.zeros((Nt+1, len(V.dofmap().dofs())))

    # preparing for the first iteration
    theta_k.assign(theta_init)
    evo[0] = theta_k.vector().get_local()

    # solve forward, i.e. theta_k -> theta p_kp1, k = 0, 1, 2, ..., Nt-1
    for k in range(Nt):
        a_ = a(
                theta_k, theta_kp1, v,
                alpha, kappa, temp_amb,
                control[k], g, implicitness, dt, ds)

        dolfin.solve(a_ == 0, theta_kp1)
        evo[k+1] = theta_kp1.vector().get_local()

        # preparing for the next iteration
        theta_k.assign(theta_kp1)

    return evo
