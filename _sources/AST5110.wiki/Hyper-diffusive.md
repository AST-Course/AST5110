# Hyper diffusive

In any flow, layers move at different velocities, and a fluid's viscosity arises from the shear stress between the layers that ultimately oppose any applied force. These shear stresses are communicated via collisions between the particles comprising the fluid, and the typical scale of viscosity is, therefore, of order the mean free collisional length $\lambda$.
This scale is usually much smaller than the scales that can be represented on a numerical grid,  $\lambda <<  \Delta x$ if one desires to model an astrophysical phenomenon of macroscopic size, and an understanding of this limitation is therefore vital to understanding the limitations of numerical modeling.

## 1. von Neumann-Richtmyer artificial viscosity

We will introduce an artificial viscosity as our dissipation mechanism to achieve smoothness in our numerical solutions. The 1D momentum and energy equations can be written as

$$\rho \left(\frac{Du}{Dt}\right) = F - \left[\frac{\partial (p + Q)}{\partial x}\right]$$

and

$$\left(\frac{De}{Dt}\right) + (p+Q)\left[ \frac{D(1/\rho)}{Dt}\right] = q$$

where $q$ is the energy input per unit mass from "external" sources (_e.g._ from radiation, conduction, or joule heating) and $Q$ is the equivalent viscous pressure given by

$$Q = - \frac{4}{3}\nu'\left(\frac{\partial^2 u}{\partial x^2}\right)$$

One possibility would be to use a large value of $\nu$, chosen such that the artificial _mean free path_ $\lambda$ would be of order with the grid spacing $\Delta x$. This is not a good procedure, however, since the shock thickness, for a given $\lambda$, is inversely proportional to its strength, and we would obtain sharp, strong shocks, but weak shocks would be spread over many grid points. In addition, such a large viscosity would spuriously reduce the Reynolds number of the flow in regions devoid of shocks and degrade the overall solution's quality. Von Neumann and Richtmyer came up with a _non-linear_ artificial viscosity that is large in shocks by very small otherwise. In particular, they use a $Q$ that is _quadratic_ in the rate of shear:

$$Q  = \left\{ \begin{array}{rcl}
        \frac{4}{3}\rho l^2 \left(\frac{\partial u}{\partial x}\right)^2 \, \mathrm{for} \, \frac{\partial u}{\partial x} < 0  \\
    0 \, \mathrm{for} \, \frac{\partial u}{\partial x} \ge 0
       \end{array}\right.$$

Since $\nu$ had dimensions [g cm$^{-3}$][cm$^{2}$s$^{-1}$], $l$ must have dimensions of length. Typically $l$ is chosen to be some small multiple of the grid spacing $\Delta x$.

The artificial viscosity, as given by this method, only occurs when the gas is compressed and is zero or very small in regions away from shocks. A large body of computational work has demonstrated that the von Neumann-Richtmyer method gives good results as long as the resulting shock thickness, say 3 to 4 $\Delta x$, is not too coarse to permit an accurate representation of other physical processes of interest (_e.g._ radiation transport).

Note that the Navier Stokes PDEs are conservative, which needs to be addressed in the numerical scheme, including the artificial diffusion. A constant and large enough diffusion coefficient can keep the conservation but a very high cost of purely resolving the shocks. The numerical scheme above is such that undesirable numerical behavior is prevented only where it is needed.

## 2. Bifrost Artificial diffusion

Often there is confusion between the diffusive effects from viscosity, heat conduction, and electrical resistivity in real astrophysical systems and the size of the numerical diffusive effects. Consequently, some concepts are necessary to clarify, such as "turbulent diffusion", artificial diffusion, hyper diffusion, or sub-grid scale diffusion.  

Bifrost uses highly localized diffusivities while retaining the PDE's original form. Various coefficients from the numerical diffusion are appropriately chosen to conceive a simulation without developing numerical instability being as non-diffusive as possible in those locations that only require very low diffusive effects. The diffusive operator in 1D is as follows:

$$\frac{\partial f}{\partial t} = .... + \frac{\partial}{\partial x}\left[\nu \Delta x (\nu_1 C_{fast} + \nu_2|u| + \nu_3 \Delta x \nabla^1_x u_x) \frac{\partial f}{\partial x} Q\left(\frac{\partial f}{\partial x}\right)\right]$$

where the quenching factor is as follows.

$$Q(g) = \frac{\frac{\partial}{\partial x}\left(|\frac{\partial g}{\partial x}|\right)}{|g|+\frac{1}{q}\frac{\partial}{\partial x}\left(|\frac{\partial g}{\partial x}|\right)}$$

and $\nabla^1_x$ is the first-order gradient in the $x$ direction. Note the hyper-diffusion is broken down with different terms as follows:

### 2.1 Sound waves

One type of artifact that we want to eliminate comes from wave speed (phase speed) error which may come from small variations coming from the discretization, which could lead to small-amplitude wave changes. In Bifrost, first of all, the staggered mesh warrants an accuracy at half-grid integer points. However, the truncation error can lead to growth for wavenumbers close to the Nyquist wavenumber. This First term on the right-hand introduces a 4th-order diffusion term that will dampen the wave perturbation. Note that the diffusion coefficient is dimensional.

As shown by [Nordlund & Gaslgard 1995](missing doc), the hyper-diffusion will effectively damp shorter waves than $2 \pi \Delta x$.

#### 2.1.1 Fast waves

Similar to the previous case, we have the same situation with Magneto-acoustic (fast) waves.

### 2.2 Advection

Small fluctuations of plasma elements transport (speed) from the advective transport will be dissipated with the second term of the hyperdiffusion. $\nu_2$ is dimensionless like $\nu_1$

### 2.3 Shocks

The remaining term in the hyper-diffusion ensures that shocks do not generate undesired numerical artifacts in the post-shock plasma.

This term is the local kinematic viscosity of the order of $\Delta u_x \Delta x$. Consequently, this viscosity is much more prominent in shocks than the previous two and localized, i.e., much smaller elsewhere. In other words, the shock viscosity is proportional to the local convergence rate.
