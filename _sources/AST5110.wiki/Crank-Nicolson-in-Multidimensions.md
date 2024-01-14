# 2 Crank-Nicolson in Multidimensions (ADI methods)

Let us consider the two-dimensional diffusion equation,

$$\frac{\partial u}{\partial t} = D \left(\frac{\partial^2 u }{\partial x^2}+ \frac{\partial^2 u}{\partial x^2} \right)  \tag{2.1}$$

An explicit method can be generalized from the one-dimensional case in an obvious way. However, we have seen that diffusive problems are usually best treated implicitly. Suppose we implement the Crank-Nicolson scheme in two dimensions. This would give us

$$u^{n+1} = u^n_{j,l} + \frac{1}{2} \alpha \left(\delta_x^2 u^{n+1}_{j,l} + \delta_x^2 u^{n}_{j,l}+\delta_y^2 u^{n+1}_{j,l} + \delta_y^2 u^{n}_{j,l}\right) \tag{2.2}$$

Here

$\alpha \equiv \frac{D \Delta t}{\Delta^2}$  where $\Delta \equiv \Delta x = \Delta y$

$\delta^2_x u^n_{j,l} \equiv u^n_{j+1,l} - 2u^n_{j,l}+u^n_{j-1},l $

and similarly for $\delta^2_y u^n_{j,l}$. This is certainly a viable scheme; the problem arises in solving the coupled linear equations. Whereas in one space dimension, the system was tridiagonal, that is no longer true, though the matrix is still very sparse.

Another possibility is a slightly different way of generalizing the Crank-Nicolson algorithm. It is still second-order accurate in time and space and unconditionally stable, but the equations are easier to solve than (2.2). Called the _alternating-direction implicit method_ (ADI), this embodies the powerful concept of _[operator splitting](Operator-splitting)_ or _time splitting_, about which we will say more below. Here, the idea is to divide each timestep into two steps of size $\Delta t/2$. Then, in each substep, a different dimension is treated implicitly:

$$u^{n+1/2}_{j,l} = u^n_{j,l} + \frac{1}{2}\alpha\left(\delta^2_x u^{n+1/2}_{j,l} + \delta_y^2 u^n_{j,l}\right)$$

$$u^{n+1}_{j,l} = u^{n+1/2}_{j,l} + \frac{1}{2}\alpha\left(\delta^2_x u^{n+1/2}_{j,l} + \delta_y^2 u^{n+1}_{j,l}\right) \tag{2.3}$$

The advantage of this method is that each substep requires only the solution of a simple tridiagonal system.
