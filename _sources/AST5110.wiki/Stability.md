# Stability

In exercises 2 and 3, we learned that some numerical discretization methods are stable and others are not. To further understand this, let's introduce von Neumann's stability analysis.

The von Neumann analysis is local: Imagine that the coefficients of the different equations are so slowly varying as to be considered constant in space and time. In that case, the independent solutions, or eigenmodes, of the different equations are all of the form:

$$ u^n_j = \xi^n e^{ikj \Delta x}, \tag{1} $$

where $k$ is a real spatial wavenumber (which can have any value) and $\xi = \xi(k)$ is a complex number that depends on $k$. The key fact is that the time dependence of a single eigenmode is nothing more than successive integer powers of the complex number $\xi$. Therefore, the difference equations are unstable (have exponentially growing modes) if $|\xi(k)| > 1$ for _some_ $k$. The number is called the amplification _factor_ at a given wavenumber $k$.

Exercise [Ex 4a](https://github.com/AST-Course/AST5110/blob/main/ex_4a.ipynb) is meant to deduce the Courant-Friedrichs-Lewy (CFL) condition stability for the FTCS method.

In the previous section, we classified the PDEs in different ways accordingly, if it is a numerical or mathematical approach. Here we will subclassify the Cauchy problems of PDEs according to their result from applying von Neumann's stability analysis.

Let's consider the following three terms on the right-hand side of this expression:

$$\frac{\partial u}{\partial t} = - a\, u - b\,\frac{\partial u}{\partial x} - c\, \frac{\partial^2 u}{\partial x^2} \tag{2}$$

where $a$, $b$, and $c$ are constant. The first term on the right-hand side is a source term, the second is an advective term, and the last is a diffusive one. We already deduced the CFL condition in [Ex 4a](https://github.com/jumasy/AST5110/blob/main/ex_4a.ipynb). Let's do the same for a source term or a diffusive term:

## 1. Source term

$$\frac{\partial u}{\partial t} = - S(u) \tag{3}$$

For instance, for a 2nd order cell-centered scheme, the Courant condition is:

$$dt\, S'(u) \leq 1 \tag{4}$$

i.e., the Courant condition for the source term in expression (2) is:

$$dt\, a \leq 1 \tag{5}$$

## 2. Advection term

See [Ex 4a](https://github.com/AST-Course/AST5110/blob/main/ex_4a.ipynb)

### 3. Diffusion term

$$\frac{\partial u}{\partial t} = - \frac{\partial ^2 G(u)}{\partial x^2}  \tag{6}$$

For instance, for a 2nd order cell-centered scheme, the Courant condition is:

$$\frac{dt\, G'(u)}{dx^2} \leq 1 \tag{7}$$

i.e., the Courant condition for the diffusive term in expression (2) is:

$$\frac{dt\, c}{dx^2} \leq 1 \tag{8}$$

---

Important: to solve the full eq. (2), it is required to perform the von Neumann instability of the entire expression unless each term is solved using an [operation splitting](Operator splitting).

---

Note that the stability criteria depend differently on the grid size ($dx$) in these three terms. Consequently, the maximum time-step size in which the method is stable is invariant with $dx$ for a source term. On the contrary, the maximum time-step will decrease linearly with $dx$ for the advection term and quadratically with a diffusive term. As a result, a diffusive term is highly stiff and increasing the spatial resolution largely decreases the step size. For more details, please look at the exercise [Ex 5a](https://github.com/AST-Course/AST5110/blob/main/ex_5a.ipynb).
