# Introduction to PDEs and classifications

Partial Differential Equations (PDEs) are part of many continuous physical systems, fluids, plasma, Electromagnetic fields, etc. This chapter briefly summarizes the classification of the most common PDEs.  

## 1. Mathematical Classification

These can be classified as complete PDEs EQs or by the different terms in the PDEs.

### 1.1 Mathematical Classification of PDEs

The PDEs can be classified into three big categories, _hyperbolic, parabolic_, and _elliptic_. These three categories differ in their _characteristics_, i.e., propagation curves.

#### 1.1.1 Hyperbolic eq. (wave eq.)

The following is the typical example of a 1D hyperbolic eq., i.e., wave eq.

$$\frac{\partial^2 u}{\partial t^2} = v^2 \frac{\partial^2 u}{\partial x^2} \tag{1}$$

Where $v = const$ is the velocity of wave propagation  

#### 1.1.2 Parabolic eq. (diffusion eq.)

The prototypical parabolic equation is the so-called diffusion equation:

$$\frac{\partial u}{\partial t} = \frac{\partial}{\partial x} \left(D \frac{\partial u}{\partial x} \right) \tag{2}$$

Where $D$ is the diffusion coefficient.

#### 1.1.3 Elliptic eq. (Poisson eq.)

Finally, the prototypical elliptic eq. is the Poisson eq.

$$\frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} = \rho(x,y) \tag{3}$$

Where $\rho$ is the source term, if the source term equals zero, the equation is _Laplace's equation_.

### 1.2 Mathematical Classification of the various terms in the PDEs

One can also separate individual terms in the PDEs. These terms can be treated with different numerical techniques since they typically have very different properties and stiffness.

#### 1.2.1 Linear or source (or sink) terms

Source (or sink) terms do not have spatial derivatives and depend on the variable that needs to be advanced in time. Some examples are ionization and recombination, chemical reactions, and collisional terms. This term can be very stiff, and often implicit methods can be easily implemented.

#### 1.2.2 Advection terms

Advection or convection terms are single derivatives ($\frac{\partial u}{\partial x}$). Often solved explicitly, and the CFL condition originally comes from this term.

#### 1.2.3 Diffusive terms

Diffusive terms are single derivatives ($\frac{\partial D \partial u}{\partial x^2}$), where $D$ is the diffusive coefficient). Some examples are thermal conduction or ohmic diffusion. Often solved explicitly, and the CFL condition originally comes from this term.

Sometimes, some terms are tough to put in this classification and are a combination or mix of several. For instance, the Hall term and ambipolar diffusion  (also known as Pedersen resistivity).

## 2 Computational Classification

Computationally, the previous classification is not very meaningful. Therefore, the best is to classify in propagating and static functions.

### 2.1 Initial value (Cauchy) problems  

The equations describe how the information $u(x,t)$ propagates forward in time. Those equations require that the information $u$ is given at some initial time ($t_0$) for all $x$. This is exemplified in the following figure.

![cauchy_init](figures/cauchy_init.png)

In the figure, initial values are given on a one-time slice, and it is desired to advance the solution in time, successive computing rows of open dots in the direction shown by the arrows. Boundary conditions at each row's left and right edges ($\bigotimes$) must also be supplied, but only one row at a time. Only one, or a few, previous rows need to be maintained in memory. Note Eq. 1 and 2 are part of this classification.

### 2.2 Boundary problems  

Single _static_ functions $u(x,y)$ satisfy the equation within some $(x,y)$ region of interest. These require some desired behavior on the boundary of the region of interest. This is exemplified in the following figure.

![bound](figures/bound.png)

In the figure, boundary values are specified around the edge of a grid, and an iterative process is employed to find the values of all the internal points (open circles). All grid points must be maintained in memory. Note Eq. 3 falls in this classification.

---

We will focus on _initial value (Cauchy)_ problems in the following. A large class of time-evolution PDEs in 1D can be cast into the form of _flux conservative equation_.

$$\frac{\partial {\bf u}}{\partial t} = - \frac{\partial \bf {F(u)}}{\partial x}$$

where ${\bf u}$ and ${\bf F}$ are vectors, and where ${\bf F}$ may depend on ${\bf u}$ and/or also on spatial derivatives of $u$. The vector ${\bf F}$ is called the _conserved flux_.

One of the simplest _flux-conservative_ equations of the _Cauchy_ problems is Burger's eq. Proceed to exercise [ex_2a_analytical](https://github.com/AST-Course/AST5110/blob/main/ex_2a_analytical.ipynb) to further understand Burger's eq:

$$\frac{\partial u}{\partial t} + u \frac{\partial u}{\partial x} =  \nu \frac{\partial^2 u}{\partial x^2}$$

When the diffusion term is absent (i.e., $\nu=0$), Burgers' equation becomes the inviscid Burgers' equation:

$$\frac{\partial u}{\partial t} + u \frac{\partial u}{\partial x} = 0,$$

and exercise 2 focuses on this expression to build the numerical code. Note that this expression is part of the hyperbolic equations as follows:

$$\frac{\partial^2 u}{\partial t^2} = v^2 \frac{\partial^2 u}{\partial x^2}$$

can be rewritten as a set of 1st-order eq.

$$\frac{\partial r}{\partial t} = v \frac{\partial s}{\partial x}$$

$$\frac{\partial s}{\partial t} = v \frac{\partial r}{\partial x}$$

where

$$r = v \frac{\partial u}{\partial x}$$

$$s = \frac{\partial u}{\partial t}$$
