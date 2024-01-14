# Self similar solution for parabolic equations [Moreno-Insertis et al.](https://www.aanda.org/articles/aa/pdf/2022/06/aa41449-21.pdf)

Let us consider the following parabolic Eq.

$$\frac{\partial u}{\partial t} = \eta \frac{\partial^2 u}{\partial x^2}  \tag{1}$$

This equation becomes a nonlinear diffusion equation for $u$. Pattle's self-similar solution is of the form

$$u(x,t) \rightarrow \left(\frac{\phi}{4 \pi \eta t}\right)^{1/3}\left[1-\frac{x^2}{R^2(t)} \right]^{1/2} \tag{2}$$

for $r < R(t)$, and 0 otherwise, where

$$R^2(t) \rightarrow \frac{3}{2} \left[4 \pi \eta t \left(\frac{\phi}{\pi}\right)^2\right]^{1/3} \tag{3}$$

Here $\phi$ is the flux of $u$. From these expressions it is clear that $u \propto t^{-1/3}$ and $R \propto t^{1/6}$. The problem has the additional feature that any single-lobed initial condition with total flux $\phi$ is expected to then, asymptotically in time, to the shape given in Eq. 2 and 3 (Zel'dovich & Raizer 1967). This is a robust multidimensional test to check whether the code's STS or implicit methods were properly implemented.

In 1D, the coefficients are different. The 1D case can be used to test the implementation in [ex_5a](https://github.com/AST-Course/AST5110/blob/main/ex_5a.ipynb). In that case, the peak of the function follows $t^{-1/2}$ and $R \propto t^{1/2}$
