# Implicit methods

Consider now a typical version of the __diffusion equation__

$$\frac{\partial u}{\partial t} = \frac{\partial}{\partial x}\left[ D \frac{\partial u}{\partial x} \right] \tag{1}$$

Equation (1) can be formulated as a conservative flux equation by setting the flux $F$ to

$$F = -D \frac{\partial u}{\partial x}$$

but as we shall see, the appearance of the second derivative makes a significant difference in the behavior of this equation and in the numerical methods that are used to solve it. Let us first assume that we have $D > 0$. If not, the equation is physically unstable, and all small perturbations in $u$ will grow without bounds. It is never possible to stably model a problem for which the governing equations are unstable.

Let us first discretize equation 1 using the FTCS scheme and, for simplicity, that $D$ is constant. We then get

$$\frac{u^{n+1}_j - u^n_j}{\Delta t} = D \left[ \frac{u^n_{j+1}-2u^n_j-u^n_{j-1}}{\Delta x^2} \right]$$

If we carry out von Neumann stability analysis on this equation, we find

$$\xi(k) = 1- \frac{4D \Delta}{(\Delta x)^2} \sin^2\left(\frac{k \Delta x}{2} \right)$$

Thus, we find that the stability condition $|\xi|^2\leq 1$ is satisfied when

$$\frac{2D\Delta t}{(\Delta x)^2} \leq 1$$

Assuming that the typical scale we are studying is given by $\lambda$ then the diffusion time scale for this scale is

$$\frac{\lambda^2}{D}\sim \tau$$

but since we have that $\lambda > \Delta x$, it follows that we will have to run of order $\lambda^2 / (\Delta x)^2$ timesteps before we see the evolution on the scales we are interested in. Note we _should_ be studying phenomena that are (much) larger than the grid scale ($\Delta x$ ). I.e. running this problem explicitly is prohibited by the large number of timesteps needed to solve the problem.

So, let us reformulate the problem using a Backward time, centered space (BCTS) method. The difference
equation then becomes

$$\frac{u^{n+1}_j - u^n_j}{\Delta t} = D \left[ \frac{u^{n+1}_{j+1}-2u^{n+1}_j-u^{n+1}_{j-1}}{\Delta x^2} \right]\, \tag{2}$$

Ignoring for a moment the question of how to solve this equation, define

$$\alpha \equiv \frac{D\Delta t}{(\Delta x)^2}$$

and carry out the von Neumann stability analysis to find that

$$\xi(k) = \frac{1}{1+ 4\alpha\sin^2\left(\frac{k \Delta x}{2} \right)}$$

It is quite clear from this that

$$|\xi(k)|<1 \, \forall k$$

and that, therefore, this algorithm is unconditionally stable, no matter the wavenumber $k$ or the length of the timestep  $\Delta t$.

Now turn to the problem of solving for $u^{n+1}_j$; moving all the unknowns in equation 17 to the left-hand side gives
<!-- AP: Equation 17 mentioned in previous line is unclear -->
$$-\alpha u^{n+1}_{j-1} + (1 + 2 \alpha)u^{n+1}_j - \alpha u^{n+1}_j = u_j^n \, \, j = 1,.... J-1$$

Supplemented with appropriate boundary conditions, this is a tridiagonal system that is readily inverted by standard methods. We can use the BTCS method to derive the equilibrium solution

$$\frac{\partial^2 u}{\partial x^2} = 0$$

of this equation via relaxation with a very long  t since the system is unconditionally stable. This is a characteristic feature of implicit methods.

Of course, solving the diffusion equation with a very long $\Delta t$ will not necessarily give a very _accurate_ time-dependent solution. If we want additional accuracy, we can combine the stability of an implicit method with a method that is second order in space and time by forming the average of the BTCS and FTCS schemes:

$$\frac{u^{n+1}_j - u^n_j}{\Delta t} = \frac{D}{2} \left[ \frac{u^{n+1}_{j+1}-2u^{n+1}_j-u^{n+1}_{j-1} + u^n_{j+1} - 2u^n_j - u^n_{j-1}}{\Delta x^2} \right] \tag{3}$$

Both left, and right-hand sides are centered at timestep $n+ 1/2$, so the method is second-order accurate in time. The amplification factor is

$$\xi(k) = \frac{1-2\alpha \sin^2\left(\frac{k\Delta x}{2}\right)}{1+2\alpha \sin^2\left(\frac{k\Delta x}{2}\right)}$$

so this method called _Crank-Nicolson_ is also unconditionally stable for any $\Delta t$.

It is also common to variably center the timestep; instead of exactly at $n + 1/2$, rather at $n + \theta$, where $0 \leq \theta \leq 1$, in which case the method goes under the name of the $\theta$-method.

## Content

- [Newton-Raphson method](Newton-Raphson-method)
- [Crank-Nicolson in Multidimensions](Crank-Nicolson-in-Multidimensions)
- [Super time stepping](Super-time-stepping)
- [Self similar solution for parabolic eq.](Self-similar-solution-for-parabolic-eq)
