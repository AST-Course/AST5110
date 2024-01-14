# 3 Other methods that can relax the stiffness (Super-time stepping or wave methods)

Super time stepping (STS; [Alexiades et al. 1996](https://onlinelibrary.wiley.com/doi/10.1002/(SICI)1099-0887(199601)12:1%3C31::AID-CNM950%3E3.0.CO;2-5)) is a technique that can be used to accelerate explicit [parabolic calculations](Introduction to PDEs and clarifications.). It is based on the stability properties of the Chebyshev polynomials, which allow us to relax the CFL condition and take a larger timestep,  $\Delta t_{STS}$. The method uses two input parameters, n, a positive integer, and $\nu \in (0, 1)$, which is a damping factor. The timestep allowed by the STS method is then given by

$$\Delta t_{STS} = \frac{n}{2\sqrt{\nu}}\left[\frac{(1+\sqrt{\nu})^{2n}-(1-\sqrt{\nu})^{2n}}{(1+\sqrt{\nu})^{2n}+(1-\sqrt{\nu})^{2n}}\right] \Delta t_{CFL}$$

and is divided into $n$ sub-timesteps $\tau_i$ as

$$\Delta t_{STS} = \sum_{i=1}^n (\tau_i)$$

with

$$\tau_i = \Delta t_{CFL}\left[(\nu -1)\cos \left(\frac{\pi (2\,i - 1)}{2\,n} \right) + \nu + 1 \right]^{-1}$$

where  $\Delta t_{CFL}$ is the timestep of the parabolic problem given by the classic CFL condition. It is important to note that the intermediate values computed along the $n$ sub-timesteps have no approximating properties: it is only after the whole $\Delta t_{STS}$ has been reached that the results approximate the solution and, consequently, have a physical meaning.

The above expressions can be easily implemented to improve the calculation efficiency of parabolic terms; nevertheless, the drawback is that the STS is a first-order scheme in time. In addition, the method has two free parameters, $n$, and it is necessary to carefully choose their values to optimize the performance while keeping numerical stability. The maximum ratio $\Delta t_{STS}/\Delta t_{CFL}$ that can be reached for any given $n$ corresponds to the following limit:

$${\lim}_{\nu \rightarrow 0} \frac{\Delta t_{STS}}{\Delta t_{CFL}} = {\lim}_{\nu \rightarrow 0} \frac{n}{2\sqrt{\nu}} \left[\frac{(1+\sqrt{\nu})^{2n}-(1-\sqrt{\nu})^{2n}}{(1+\sqrt{\nu})^{2n}+(1-\sqrt{\nu})^{2n}}\right] = n^2$$

In this limit, the CFL criterion would need $n^2$ steps to reach one $\Delta t_{STS}$, while the STS method requires just $n$, as explained above (Eq. (15)). Assuming a similar computing load for each step, whether, in the STS or the CFL-limited calculation, this implies that the STS method would be $n$ times faster than the simple CFL-limited one. However, it is necessary to impose a lower threshold for $\nu$ because  $\nu = 0$ is a stability limit. Choosing low values of $\nu$ can make the STS method very sensitive to round-off errors ([Alexiades et al. 1996](https://onlinelibrary.wiley.com/doi/10.1002/(SICI)1099-0887(199601)12:1%3C31::AID-CNM950%3E3.0.CO;2-5)). In the next subsection; we explain our choices made for $\nu$ and $n$.
