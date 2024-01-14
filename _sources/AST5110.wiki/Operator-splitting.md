# Operator splitting

Operator splitting is a standard technique to advance in time the solution at each timestep separately for groups of terms that contain different physics (hence with different numerical requirements).  For instance, diffusive terms such as

$$\frac{\partial u}{\partial t} =  \frac{\partial }{\partial x}\left( D\frac{\partial u}{\partial x}\right) \tag{1}$$

could be solved with implicit methods and source or advective terms, e.g.,

$$\frac{\partial u}{\partial t} =  A\, u + v\frac{\partial u}{\partial x}$$

explicitly. Considering an equation that contains these terms:

$$\frac{\partial u}{\partial t} =  A\, u + v\frac{\partial u}{\partial x} + \frac{\partial }{\partial x}\left( D\frac{\partial u}{\partial x}\right) $$

then each term could be separated and solved over a timestep $\Delta t$ determined by von Neuman analysis for each term separately. For instance, one might use an explicit scheme for the advective term combined with a Crank-Nicolson or another implicit scheme for the diffusion term.

This could be done with the so-called Operator Splitting (OS). The basic idea of operator splitting, which is also called time splitting or the method of fractional steps, is this: Suppose you have an initial value equation of the form

$$\frac{\partial u}{\partial t} = F\, u \tag{2}$$

where the operator $F$ is some operator. While $F$ is not necessarily linear, suppose that it can at least be written as a linear sum of $m$ pieces, which act additively on $u$,

$$F u = F_1 u + F_2 u + ... + F_m u \tag{3}$$

Finally, suppose that for __each__ of the pieces, you already know a differencing scheme for updating the variable $u$ from timestep $n$ to timestep $n+1$, valid if that piece of the operator were the only one on the right-hand side. We will write these updatings symbolically as

$$u^{n+1} = U_1(u^n,\Delta t)$$

$$u^{n+1} = U_2(u^n,\Delta t)$$

$$...$$

$$u^{n+1} = U_m(u^n,\Delta t) \tag{4}$$

Now, one form of operator splitting would be to get from $n$ to $n+1$ by the following sequence of updating:

$$u^{n+(1/m)} = U_1(u^n,\Delta t)$$

$$u^{n+(2/m)} = U_2(u^{n+(1/m)},\Delta t)$$

$$...$$

$$u^{n+1} = U_m(u^{n+(m-1)/m},\Delta t) \tag{5}$$

where $t=n\, \Delta t$ and $\Delta t\rightarrow 0$.

The following describes different techniques where one could apply an OS.

## Lie-Trotter Splitting

Lie-Trotter splitting is a first-order splitting method that solves two sub-problems sequentially on subintervals $[t^n,t^{n+1}]$ where $t^{n+1/2} = t^n + \Delta t/2$ and $\Delta t = t^{n+1}-t^n$. The different subproblems are connected via the initial conditions as follows:

$$\frac{\partial u}{\partial t} = F_1 u(t)$ with $t \in [t^n,t^{n+1}]$ and $u(t^n)=u^n_{sp}$$

$$\frac{\partial v}{\partial t} = F_2 v(t)$ with $t \in [t^n,t^{n+1}]$ and $v(t^n)=u(t^{n+1})$$

where $u^n_{sp}= U_0$. The approximated split solution at the point $t=t^{n+1}$ is defined as $u^{n+1}_{sp}=v(t^{n+1})$.

## Strang Splitting

Strang splitting is one of the most popular and widely used operator splitting methods. By small modification, it is possible to make the splitting algorithm second-order accurate. The idea is that instead of first solving the first sub-problem for a full-time step, we solve it for a half-time step. We then solve the second sub-problem for a full-time step and then go back to the first sub-problem and solve it for a half-time step.

$$\frac{\partial u^*}{\partial t} = F_1 u(t)$ with $t \in [t^n,t^{n+1/2}]$ and $u(t^n)=u^n_{sp}$$

$$\frac{\partial v}{\partial t} = F_2 v(t)$ with $t \in [t^n,t^{n+1}]$ and $v(t^n)=u(t^{n+1/2})$$

$$\frac{\partial w}{\partial t} = F_1 w(t)$ with $t \in [t^{n+1/2},t^{n+1}]$ and $w(t^{n+1/2})=v(t^{n+1})$$

where $t^{n+1/2} = t^n + \Delta t/2$, and the approximated split solution at the point  $t=t^{n+1/2}$ is defined as $u^{n+1}_{sp}=w(t^{n+1})$.

## Additive Splitting

The additive operator splitting method is a first-order method, and it is based on a simple idea in which we solve the different sub-problems using the same initial condition. The computed split solution of the two sub-problems is added, and the initial condition is subtracted from the sum. In this manner, we obtain a splitting method where the different sub-problems do not affect each other. This motivates the use of additive splitting, first because the result of an additive operator splitting is independent of the order in which the operators are applied. For methods like Lie-Trotter and Strang splitting, the operators will generally not commute in the non-linear case, which means the result depends on the order in which the operators are applied. Another advantage is that the operators are applied independently so that they can be computed in parallel

$$\frac{\partial u}{\partial t} = F_1 u(t)$ with $t \in [t^n,t^{n+1}]$ and $u(t^n)=u^n_{sp}$$

$$\frac{\partial v}{\partial t} = F_2 v(t)$ with $t \in [t^n,t^{n+1}]$ and $v(t^n)=u^n_{sp}$$

$$u^{n+1}_{sp} = u(t^{n+1}) + v(t^{n+1}) - u^n_{sp}$$

## Alternating-direction implicit (ADI) method

Equation (2.3) in Section [Implicit methods](Implicit-methods) is an example of operator splitting with a slightly different twist. Let us reinterpret (4) to have a different meaning: Let $U_1$ now denote an updating method that includes all the pieces of the total operator $F$ algebraically, but which is desirably stable only for the $F_1$ piece; likewise $U_2, ..., U_m$. Then a method of getting from $u^n$ to $u^{n+1}$ is

$$u^{n+(1/m)} = U_1(u^n,\Delta t/m)$$

$$u^{n+(2/m)} = U_2(u^{n+(1/m)},\Delta t/m)$$

$$...$$

$$u^{n+1} = U_m(u^{n+(m-1)/m},\Delta t/m)  \, (6)$$

<!-- AP: Equations are not being rendered properly here -->
The timestep for each fractional step in (6) is now only $1/m$ of the whole timestep because each partial operation acts with the original operator's terms.

Equation (6) is usually, though not always, stable as a differencing scheme for the operator $F$. In fact, as a rule of thumb, it is often sufficient to have stable $U_i$’s only for the operator pieces having the highest number of spatial derivatives — the other $U_i$’s can be _unstable_ —to make the overall scheme stable!
