# 1. Newton-Raphson method

In general, in implicit methods, one is striving to solve a set of PDEs on a mesh covering $N$ points where ${\bf f}$ which are functions of the unknowns at timestep $n + 1$ (as well as the variables at timestep $n$ or earlier) such that

$${\bf f} (...,\rho_{j-1}^{n+1},u_{j-1}^{n+1},\rho_j^{n+1},u_j^{n+1},\rho_{j+1}^{n+1},u_{j+1}^{n+1},...) = 0$$

and the set of equations $f_i$ covers the entire numerical grid $1,...,N$ with one equation for each variable at every grid point; _i.e._ the equation of mass conservation, momentum conservation, energy conservation, etc.

Define now the solution vector $v \equiv (\rho^{n+1}, u^{n+1},...)$ and assume that we are close to the correct solution, i.e., that we can write

$$v = v' + \delta v$$

We can now do a Taylor expansion around $v$

$${\bf f} (v) = 0 = {\bf f}(v')+\sum\frac{\partial f_i}{\partial v_j}\delta v_j + O(\delta v^2)$$

To arrive at the correct solution, we must therefore solve for $\delta v$

$$ -{\bf f}(v') = \sum \frac{\partial f_i}{\partial v_j}\delta v_j$$

by inverting the matrix $\sum_{ij}\frac{\partial f_i}{\partial v_j}$ if our operator ${\bf f}$ is linear in ${\bf v}$ we will find the solution directly, if not we will need to solve this equation iteratively at every timestep. In practice, this means that we guess at a solution $v'$; typically, when solving for a time-evolving problem using the solution from the last time step, and then solving for a correction and adding this correction to our original guess, continuing until the correction is "small enough". It can then pay off to solve for $\delta v/v$ instead by multiplying every row $i$ by ${\bf v}$.

$$ -{\bf f}(v') = \sum v_j\frac{\partial f_i}{\partial v_j}({\delta v_j/v_j})$$

This makes checking for convergence much easier. In cases where a valid value for the variable $v_j$ (i.e., the velocity $u$) could be zero, it is better to multiply by a _typical_ value, _e.g.,_ use the speed of sound when solving for the velocity. We can invert the matrix $\sum v_j\frac{\partial f_i}{\partial v_j}$ using standard methods, the one chosen depending on the structure of the matrix: diagonal, tridiagonal, pentadiagonal, etc., which in turn depends on the order and structure of the scheme used to discretize the equations being solved.

## 2. A 1D example/exercise

To give a practical example, let us consider a system of two equations and two unknowns, _i.e.,_ the equations of mass and momentum conservation in one dimension (in this case, $z$).

$$\frac{\partial\rho}{\partial t}+\frac{\partial(\rho u_z)}{\partial z}=0$$

$$\frac{\partial\rho u_z}{\partial t}+\frac{\partial(\rho u_zu_z)}{\partial z}+\frac{\partial p(\rho)}{\partial z}-\rho g=0$$

Since we are not solving the energy equation, we will need to assume a relation between $p$ and $\rho$, _e.g.,_ that $p=p(\rho)$ (usually something like $p\propto \rho^\gamma$).

1. Discretise these equations on a 1D grid that spans $1,\ldots,N$
using an implicit method. How many equations will you need? What do the equations look like in central points? And what about the boundary points? Is this system linear or non-linear?

2. To solve the equations using the Newton-Raphson method, one will need
to compute the Jacobi matrix. Then, compute the coefficients of the matrix, and explain its structure. At some point, the expression ${\partial p}/{\partial\rho}$ will arise. What does that quantity signify?

3. Devise an algorithm that, given an initial state, advances the variables in time.

4. Implement the above in Python.
