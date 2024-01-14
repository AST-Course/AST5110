# Examples of hyperbolic numerical schemes

The following are some well-known examples of finite-difference __explicit__ schemes for the scalar advection equation. C=center, F=forward, B=Backward, T=Time, S=Space, e.g., FTBS= _Forward-time backward-space_.

| Name           | Difference equations| order (T/S) | Stability | Other Prop |
| ---            | ---                 | ---         | ---       |  ---       |
| explicit Euler (FTCS) | $u^{n+1}_j = u^{n}_j - \frac{\Delta t}{2 \Delta x}\lambda(u^{n}_{j+1}-u^{n}_{j-1})$ | (1st/2nd)  | No | |
| Upwind (FTFS) | $u^{n+1}_j = u^{n}_j - \frac{\Delta t}{\Delta x}\lambda(u^{n}_{j+1}-u^{n}_{j})$ |  (1st/1st)  | only for upwind prop | |
| Downwind (FTBS) | $u^{n+1}_j = u^{n}_j - \frac{\Delta t}{\Delta x}\lambda(u^{n}_{j}-u^{n}_{j-1})$ |  (1st/1st)  |  only for downwind prop | |
| Lax-Friedrichs | $u^{n+1}_j = \frac{1}{2}(u^{n}_{j-1}+u^{n}_{j+1}) - \frac{\Delta t}{2\Delta x}\lambda(u^{n}_{j+1}-u^{n}_{j-1})$ |  (1st/2nd)  | Yes | extremely diffusive |
| Lax-Wendroff | $u^{n+1}_j = u^{n} - \frac{\Delta t}{2\Delta x}\lambda(u^{n}_{j+1}-u^{n}_{j-1}) + \frac{(\Delta t)^2}{2(\Delta x)^2} \lambda^2 (u^{n}_{j+1}-2 u^{n}_{j}+u^{n}_{j-1})$ | (1st/2nd)  |   yes | diffusive at $k\Delta x$ |
| Beam-Warming | $u^{n+1}_j = u^{n} - \frac{\Delta t}{2\Delta x}\lambda(3 u^{n}_{j}-4u^{n}_{j-1}+u^n_{j-2}) + \frac{(\Delta t)^2}{2(\Delta x)^2} \lambda^2 (u^{n}_{j}-2 u^{n}_{j-1}+u^{n}_{j-2})$ | (1st/2nd)  | yes | conservative, and upwind |

The following are some well-known examples of finite-difference __implicit__ schemes for the scalar advection equation.

| Name           | Difference equations|  order | Stability | Other Prop |
| ---            | ---                 | ---    | ---       |  ---       |
| implicit Euler (BTCS) | $u^{n+1}_j = u^{n}_j - \frac{\Delta t}{2 \Delta x}\lambda(u^{n+1}_{j+1}-u^{n+1}_{j-1})$ | (1st/2nd)  |  yes  | has amplitude error but does not blow up |
| Upwind (BTFS) | $u^{n+1}_j = u^{n}_j - \frac{\Delta t}{\Delta x}\lambda(u^{n+1}_{j+1}-u^{n+1}_{j})$ |  (1st/1st) | highly unstable | despite that its implicit  |
| Downwind (BTBS) | $u^{n+1}_j = u^{n}_j - \frac{\Delta t}{\Delta x}\lambda(u^{n+1}_{j}-u^{n+1}_{j-1})$ |  (1st/1st)  | yes because its implicit |  extremely diffusive |

The following are some well-known examples of finite-difference __central__ schemes for the scalar advection equation. Note that these are explicit methods and need initial conditions and $u^0$ and $u^1$.

| Name           | Difference equations| order | Stability | Other Prop |
| ---            | ---                 | ---   | ---       |  ---       |
| Leapfrog (CTCS) | $u^{n+1}_j = u^{n-1}_{j} - \frac{\Delta t}{2\Delta x}\lambda(u^{n}_{j+1}-u^{n}_{j-1})$ | (2nd/2nd)  |  Stable | has amplitude error but does not blow up, even larger than BTCS. |
| Upwind (CTFS) | $u^{n+1}_j = u^{n-1}_j - \frac{\Delta t}{\Delta x}\lambda(u^{n}_{j+1}-u^{n}_{j})$ |  (2nd/1st) |   Unstable | |
| Downwind (CTBS) | $u^{n+1}_j = u^{n-1}_j - \frac{\Delta t}{\Delta x}\lambda(u^{n}_{j}-u^{n}_{j-1})$ |   (2nd/1st) |  Unstable | |
