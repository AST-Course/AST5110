#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 02 10:25:17 2021

@author: Juan Martinez Sykora

"""

# import external public "common" modules
import numpy as np


def deriv_fwd(xx: np.ndarray, hh: np.ndarray, **kwargs) -> np.ndarray:
    """
    Returns the forward derivative of hh array with respect to xx array.

    Parameters
    ----------
    xx : `array`
        Spatial axis.
    hh : `array`
        Function that depends on xx.

    Returns
    -------
    `array`
        The forward derivative of hh respect to xx. The last
        grid point is ill (or missing) calculated.
    """


def order_conv(hh: np.ndarray, hh2: np.ndarray, hh4: np.ndarray, **kwargs) -> np.ndarray:
    """
    Computes the order of convergence of a derivative function

    Parameters
    ----------
    hh : `array`
        A function that depends on xx.
    hh2 : `array`
        A function that depends on xx but with twice the number of grid points than hh.
    hh4 : `array`
        A function that depends on xx but with twice the number of grid points than hh2.
    Returns
    -------
    `array`
        The order of convergence.
    """


def deriv_4tho(xx: np.ndarray, hh: np.ndarray, **kwargs) -> np.ndarray: 
    """
    Returns the 4th order derivative of hh with respect to xx.

    Parameters
    ----------
    xx : `array`
        Spatial axis.
    hh : `array`
        A function that depends on xx.

    Returns
    -------
    `array`
        The centered 4th order derivative of hh with respect to xx.
        The last and first two grid points are ill-calculated.
    """


def step_adv_burgers(
    xx: np.ndarray,
    hh: np.ndarray,
    a: float,
    cfl_cut: float = 0.98,
    ddx = lambda x,y: deriv_fwd(x, y),
    **kwargs
) -> np.ndarray: 
    r"""
    Right-hand side of Burger's eq. where a can be a constant or a function that
    depends on xx.

    Requires
    ----------
    cfl_adv_burger function which computes np.min(dx/a)

    Parameters
    ----------
    xx : `array`
        Spatial axis.
    hh : `array`
        A function that depends on xx.
    a : `float` or `array`
        Either constant or array multiplies the right-hand side of the Burger's eq.
    cfl_cut : `float`
        Constant value to limit dt from cfl_adv_burger.
        By default, clf_cut=0.98.
    ddx : `lambda function`
        Allows the selection of the type of spatial derivative.
        By default lambda x,y: deriv_fwd(x, y)

    Returns
    -------
    `array`
        Time interval.
        Right hand side of (u^{n+1}-u^{n})/dt = from burgers eq, i.e., x \frac{\partial u}{\partial x}
    """


def cfl_adv_burger(a: float, x: np.ndarray) -> float:
    """
    Computes the dt_fact, i.e., Courant, Fredrich, and
    Lewy's condition for the advective term in Burger's equation.

    Parameters
    ----------
    a : `float` or `array`
        Either constant or array multiplies the right-hand side of the Burger's eq.
    x : `array`
        Spatial axis.

    Returns
    -------
    `float`
        min(dx/|a|)
    """


def evolv_adv_burgers(
    xx: np.ndarray,
    hh: np.ndarray,
    nt: int,
    a: float,
    cfl_cut: float = 0.98,
    ddx = lambda x,y: deriv_fwd(x, y),
    bnd_type: str = 'wrap',
    bnd_limits: list=[0,1],
    **kwargs
    ):
    r"""
    Advance nt time-steps in time the burger eq for a being a fix constant or array.
    Requires
    ----------
    step_adv_burgers

    Parameters
    ----------
    xx : `array`
        Spatial axis.
    hh : `array`
        A function that depends on xx.
    nt : `int`
        Number of time iterations. 
    a : `float` or `array`
        Either constant or array, which multiplies the right-hand side of the Burger's eq.
    cfl_cut : `float`
        Constant value to limit dt from cfl_adv_burger.
    ddx : `lambda function`
        Allows to change the space derivative function.
        By default lambda x,y: deriv_fwd(x, y).
    bnd_type : `string`
        Allows to select the type of boundaries.
        By default 'wrap'.
    bnd_limits : `list(int)`
        Array of two integer elements. The number of pixels
        will need to be updated with the boundary information.
        By default [0,1].

    Returns
    -------
    t : `array`
        time 1D array
    unnt : `array`
        Spatial and time evolution of u^n_j for n = (0,nt), and where j represents
        all the elements of the domain.
    """


def deriv_bck(xx: np.ndarray, hh: np.ndarray, **kwargs) -> np.ndarray:
    r"""
    Returns the backward derivative of hh with respect to xx.

    Parameters
    ----------
    xx : `array`
        Spatial axis.
    hh : `array`
        A function that depends on xx.

    Returns
    -------
    `array`
        The backward derivative of hh respect to xx. The first
        grid point is ill-calculated.
    """


def deriv_cent(xx: np.ndarray, hh: np.ndarray, **kwargs) -> np.ndarray:
    r"""
    Returns the centered 2nd derivative of hh with respect to xx.

    Parameters
    ----------
    xx : `array`
        Spatial axis.
    hh : `array`
        Function that depends on xx.

    Returns
    -------
    `array`
        The centered 2nd order derivative of hh with respect to xx. The first
        and last grid points are ill-calculated.
    """


def evolv_uadv_burgers(
    xx: np.ndarray,
    hh: np.ndarray,
    nt: int,
    cfl_cut: float = 0.98,
    ddx = lambda x,y: deriv_fwd(x, y),
    bnd_type: str='wrap',
    bnd_limits: list = [0,1],
    **kwargs,
):
    r"""
    Advance nt time-steps in time the burger eq for a being u.

    Requires
    --------
    step_uadv_burgers

    Parameters
    ----------
    xx : `array`
        Spatial axis.
    hh : `array`
        Function that depends on xx.
    nt : `int`
        Number of time iterations. 
    cfl_cut : `float`
        Constant value to limit dt from cfl_adv_burger.
        By default 0.98.
    ddx : `lambda function`
        Allows to change the space derivative function.
    bnd_type : `string`
        It allows one to select the type of boundaries.
        By default, 'wrap'
    bnd_limits : `list(int)`
        List of two integer elements. The number of pixels that
        will need to be updated with the boundary information.
        By default [0,1]

    Returns
    -------
    t : `array`
        Time 1D array
    unnt : `array`
        Spatial and time evolution of u^n_j for n = (0,nt), and where j represents
        all the elements of the domain.
    """


def evolv_Lax_uadv_burgers(
    xx: np.ndarray,
    hh: np.ndarray,
    nt: int,
    cfl_cut: float = 0.98,
    ddx = lambda x,y: deriv_fwd(x, y),
    bnd_type: str='wrap',
    bnd_limits: list = [0,1],
    **kwargs,
):
    r"""
    Advance nt time-steps in time the burger eq for a being u using the Lax method.

    Requires
    --------
    step_uadv_burgers

    Parameters
    ----------
    xx : `array`
        Spatial axis.
    hh : `array`
        A function that depends on xx.
    nt : `int`
        Number of time iterations.
    cfl_cut : `array`
        Constant value to limit dt from cfl_adv_burger.
        By default 0.98
    ddx : `array`
        The lambda function allows to change of the space derivative function.
        By derault  lambda x,y: deriv_fwd(x, y)
    bnd_type : `string`
        It allows to select the type of boundaries
    bnd_limits : `list(int)`
        List of two integer elements. The number of pixels
        will need to be updated with the boundary information.
        By default [0,1]

    Returns
    -------
    t : `array`
        Time 1D array
    unnt : `array`
        Spatial and time evolution of u^n_j for n = (0,nt), and where j represents
        all the elements of the domain.
    """


def evolv_Lax_adv_burgers(
    xx: np.ndarray,
    hh: np.ndarray,
    nt: int,
    cfl_cut: float = 0.98,
    ddx = lambda x,y: deriv_fwd(x, y),
    bnd_type: str='wrap',
    bnd_limits: list = [0,1],
    **kwargs,
):
    r"""
    Advance nt time-steps in time the burger eq for a being a fix constant or array.

    Requires
    --------
    step_adv_burgers

    Parameters
    ----------
    xx : `array`
        Spatial axis.
    hh : `array`
        A function that depends on xx.
    nt : `int`
        Number of time iterations. 
    a : `float` or `array`
        Either constant or array multiplies the right-hand side of the Burger's eq.
    cfl_cut : `float`
        Constant value to limit dt from cfl_adv_burger.
        By default 0.98
    ddx : `lambda function`
        Allows to change the space derivative function.
        By default lambda x,y: deriv_fwd(x, y)
    bnd_type : `string`
        It allows one to select the type of boundaries.
        By default, 'wrap'
    bnd_limits : `list(int)`
        Array of two integer elements. The number of pixels that
        will need to be updated with the boundary information.
        By default [0,1]

    Returns
    -------
    t : `array`
        Time 1D array
    unnt : `array`
        Spatial and time evolution of u^n_j for n = (0,nt), and where j represents
        all the elements of the domain.
    """


def step_uadv_burgers(
    xx: np.ndarray,
    hh: np.ndarray,
    cfl_cut: float = 0.98,
    ddx = lambda x,y: deriv_fwd(x, y),
    **kwargs,
):
    r"""
    Right-hand side of Burger's eq. where a is u, i.e., hh.

    Requires
    --------
        cfl_adv_burger function which computes np.min(dx/a)

    Parameters
    ----------
    xx : `array`
        Spatial axis.
    hh : `array`
        A function that depends on xx.
    cfl_cut : `array`
        Constant value to limit dt from cfl_adv_burger.
        By default 0.98
    ddx : `lambda function`
        Allows to select the type of spatial derivative.
        By default lambda x,y: deriv_fwd(x, y)


    Returns
    -------
    dt : `array`
        time interval
    unnt : `array`
        right hand side of (u^{n+1}-u^{n})/dt = from burgers eq, i.e., x \frac{\partial u}{\partial x}
    """


def cfl_diff_burger(a: float, x: np.ndarray) -> float: 
    r"""
    Computes the dt_fact, i.e., Courant, Fredrich, and
    Lewy condition for the diffusive term in the Burger's eq.

    Parameters
    ----------
    a : `float` or `array`
        Either constant or array multiplies the right-hand side of the Burger's eq.
    x : `array`
        Spatial axis.

    Returns
    -------
    `float`
        min(dx/|a|)
    """


def ops_Lax_LL_Add(
    xx: np.ndarray,
    hh: np.ndarray,
    nt: int,
    a: np.ndarray,
    b: np.ndarray,
    cfl_cut: float = 0.98,
    ddx = lambda x,y: deriv_fwd(x, y), 
    bnd_type: str = 'wrap',
    bnd_limits: list = [0,1],
    **kwargs,
):
    r"""
    Advance nt time-steps in time the burger eq for a being a and b
    a fix constant or array. Solve two advective terms separately
    with the Additive Operator Splitting scheme.  Both steps are
    with a Lax method.

    Requires
    --------
    step_adv_burgers
    cfl_adv_burger

    Parameters
    ----------
    xx : `array`
        Spatial axis.
    hh : `array`
        A function that depends on xx.
    nt : `int`
        Number of time iterations.
    a : `float` or `array`
        Either constant or array multiplies the right-hand side of the Burger's eq.
    b : `float` or `array`
        Either constant or array multiplies the right-hand side of the Burger's eq.
    cfl_cut : `float`
        Constant value to limit dt from cfl_adv_burger.
        By default 0.98
    ddx : `lambda function`
        Allows to change the space derivative function.
        By default lambda x,y: deriv_fwd(x, y)
    bnd_type : `string`
        It allows one to select the type of boundaries
        By default, 'wrap'
    bnd_limits : `list(int)`
        List of two integer elements. The number of pixels
        will need to be updated with the boundary information.
        By default [0,1]

    Returns
    -------
    t : `array`
        Time 1D array
    unnt : `array`
        Spatial and time evolution of u^n_j for n = (0,nt), and where j represents
        all the elements of the domain.
    """


def ops_Lax_LL_Lie(
    xx: np.ndarray,
    hh: np.ndarray,
    nt: int,
    a: np.ndarray,
    b: np.ndarray,
    cfl_cut: float = 0.98,
    ddx = lambda x,y: deriv_fwd(x, y),
    bnd_type: str = 'wrap',
    bnd_limits: list = [0,1],
    **kwargs,
):
    r"""
    Advance nt time-steps in time the burger eq for a being a and b
    a fix constant or array. Solving two advective terms separately
    with the Lie-Trotter Operator Splitting scheme.  Both steps are
    with a Lax method.

    Requires:
    step_adv_burgers
    cfl_adv_burger

    Parameters
    ----------
    xx : `array`
        Spatial axis.
    hh : `array`
        Function that depends on xx.
    nt : `int`
        Number of time iterations. 
    a : `float` or `array`
        Either constant or array multiplies the right-hand side of the Burger's eq.
    b : `float` or `array`
        Either constant or array multiplies the right-hand side of the Burger's eq.
    cfl_cut : `float`
        Limit dt from cfl_adv_burger.
        By default 0.98
    ddx : `lambda function`
        Allows to change the space derivative function.
        By default lambda x,y: deriv_fwd(x, y)
    bnd_type : `string`
        It allows one to select the type of boundaries.
        By default, 'wrap'
    bnd_limits : `list(int)`
        List of two integer elements. The number of pixels that
        will need to be updated with the boundary information.
        By default [0,1]

    Returns
    -------
    t : `array`
        Time 1D array
    unnt : `array`
        Spatial and time evolution of u^n_j for n = (0,nt), and where j represents
        all the elements of the domain.
    """


def ops_Lax_LL_Strang(
    xx: np.ndarray,
    hh: np.ndarray,
    nt: int,
    a: np.ndarray,
    b: np.ndarray,
    cfl_cut: float = 0.98,
    ddx = lambda x,y: deriv_fwd(x, y),
    bnd_type: str = 'wrap',
    bnd_limits: list = [0,1],
    **kwargs,
):
    r"""
    Advance nt time-steps in time the burger eq for a being a and b
    a fix constant or array. Solving two advective terms separately
    with the Lie-Trotter Operator Splitting scheme. Both steps are
    with a Lax method.

    Requires
    --------
    step_adv_burgers
    cfl_adv_burger
    numpy.pad for boundaries.

    Parameters
    ----------
    xx : `array`
        Spatial axis.
    hh : `array`
        Function that depends on xx.
    nt : `int`
        Number of time iterations.
    a : `float` or `array`
        Either constant or array multiplies the right-hand side of the Burger's eq.
    b : `float` or `array`
        Either constant or array multiplies the right-hand side of the Burger's eq.
    cfl_cut : `float`
        Constant value to limit dt from cfl_adv_burger.
        By default 0.98
    ddx : `lambda function`
        Allows to change the space derivative function.
        By default lambda x,y: deriv_fwd(x, y)
    bnd_type : `string`
        Allows to select the type of boundaries.
        By default, `wrap`
    bnd_limits : `list(int)`
        The number of pixels that will need to be updated with the boundary information.
        By default [0,1]

    Returns
    -------
    t : `array`
        Time 1D array
    unnt : `array`
        Spatial and time evolution of u^n_j for n = (0,nt), and where j represents
        all the elements of the domain.
    """


def osp_Lax_LH_Strang(
    xx: np.ndarray,
    hh: np.ndarray,
    nt: int,
    a: np.ndarray,
    b: np.ndarray,
    cfl_cut: float = 0.98,
    ddx = lambda x,y: deriv_fwd(x, y),
    bnd_type: str = 'wrap',
    bnd_limits: list = [0,1],
    **kwargs,
):
    r"""
    Advance nt time-steps in time the burger eq for a being a and b
    a fix constant or array. Solving two advective terms separately
    with the Strang Operator Splitting scheme. One step is with a Lax method
    and the second is the Hyman predictor-corrector scheme.

    Requires
    --------
    step_adv_burgers
    cfl_adv_burger

    Parameters
    ----------
    xx : `array`
        Spatial axis.
    hh : `array`
        Function that depends on xx.
    nt : `int`
        Number of time iterations.
    a : `float` or `array`
        Either constant or array multiplies the right-hand side of the Burger's eq.
    b : `float` or `array`
        Either constant or array multiplies the right-hand side of the Burger's eq.
    cfl_cut : `float`
        Limit dt from cfl_adv_burger.
        By default 0.98
    ddx : `lambda function`
        Allows to change the space derivative function.
        By default lambda x,y: deriv_fwd(x, y)
    bnd_type : `string`
        It allows one to select the type of boundaries.
        By default, 'wrap'
    bnd_limits : `list(int)`
        Array of two integer elements. The number of pixels that
        will need to be updated with the boundary information.
        By default [0,1]

    Returns
    -------
    t : `array`
        Time 1D array
    unnt : `array`
        Spatial and time evolution of u^n_j for n = (0,nt), and where j represents
        all the elements of the domain.
    """


def step_diff_burgers(
    xx: np.ndarray,
    hh: np.ndarray,
    a: float,
    ddx = lambda x,y: deriv_cent(x, y),
    **kwargs
) -> np.ndarray:
    r"""
    Right hand side of the diffusive term of Burger's eq. where nu can be a constant or a function that
    depends on xx.

    Parameters
    ----------
    xx : `array`
        Spatial axis.
    hh : `array`
        A function that depends on xx.
    a : `float` or `array`
        Either constant or array multiplies the right-hand side of the Burger's eq.
    ddx : `lambda function`
        Allows to change the space derivative function.
        By default lambda x,y: deriv_fwd(x, y)

    Returns
    -------
    `array`
        Right hand side of (u^{n+1}-u^{n})/dt = from burgers eq, i.e., x \frac{\partial u}{\partial x}
    """


def NR_f(
    xx: np.ndarray,
    un: np.ndarray,
    uo: np.ndarray,
    a: float,
    dt: float,
    **kwargs,
) -> np.ndarray:
    r"""
    NR F function.

    Parameters
    ----------
    xx : `array`
        Spatial axis.
    un : `array`
        A function that depends on xx.
    uo : `array`
        A function that depends on xx.
    a : `float` or `array`
        Either constant or array multiplies the right-hand side of the Burger's eq.
    dt : `float`
        Time interval

    Returns
    -------
    `array`
        function  u^{n+1}_{j}-u^{n}_{j} - a (u^{n+1}_{j+1} - 2 u^{n+1}_{j} -u^{n+1}_{j-1}) dt
    """


def jacobian(    
    xx: np.ndarray,
    un: np.ndarray,
    a: float,
    dt: float,
    **kwargs
) -> np.ndarray: 
    r"""
    Jacobian of the F function. 

    Parameters
    ----------
    xx : `array`
        Spatial axis.
    un : `array`
        A function that depends on xx.
    a : `float` or `array`
        Either constant or array multiplies the right-hand side of the Burger's eq.
    dt : `float`
        Time interval

    Returns
    -------
    `array`
        Jacobian F_j'(u^{n+1}{k})
    """


def Newton_Raphson(
    xx: np.ndarray,
    hh: np.ndarray,
    a: np.ndarray,
    dt: float, 
    nt: int,
    toll: float = 1e-5,
    ncount: int = 2, 
    bnd_type: str = 'wrap',
    bnd_limits: list = [0,1],
    **kwargs,
):
    r"""
    NR scheme for the burgers equation.

    Parameters
    ----------
    xx : `array`
        Spatial axis.
    hh : `array`
        A function that depends on xx.
    a : `float` or `array`
        Either constant or array multiplies the right-hand side of the Burger's eq.
    dt : `float`
        Time interval
    nt : `int`
        Number of time iterations.
    toll : `float`
        Error limit.
        By default 1e-5
    ncount : `int`
        Maximum number of iterations.
        By default 2
    bnd_type : `string`
        Allows to select the type of boundaries.
        By default, 'wrap'
    bnd_limits : `list(int)`
        Array of two integer elements. The number of pixels that
        will need to be updated with the boundary information.
        By default [1,1]

    Returns
    -------
    t : `array`
        Array of time.
    unnt : `array`
        Spatial and time evolution of u^n_j for n = (0,nt), and where j represents
        all the elements of the domain.
    errt : `array`
        Error for each timestep
    countt : `list(int)`
        number iterations for each timestep
    """
    err = 1.
    unnt = np.zeros((np.size(xx), nt))
    errt = np.zeros((nt))
    countt = np.zeros((nt))
    unnt[:, 0] = hh
    t = np.zeros((nt))

    # Looping over time
    for it in range(1, nt):
        uo = unnt[:, it-1]
        ug = unnt[:, it-1]
        count = 0
        # iteration to reduce the error.
        while ((err >= toll) and (count < ncount)):

            jac = jacobian(xx, ug, a, dt) # Jacobian 
            ff1 = NR_f(xx, ug, uo, a, dt) # F
            # Inversion:
            un = ug - np.matmul(np.linalg.inv(jac), ff1)

            # error:
            err = np.max(np.abs(un - ug) / (np.abs(un) + toll))
            # err = np.max(np.abs(un - ug))
            errt[it] = err

            # Number of iterations
            count += 1
            countt[it] = count

            # Boundaries
            if bnd_limits[1] > 0:
                u1_c = un[bnd_limits[0]:-bnd_limits[1]]
            else:
                u1_c = un[bnd_limits[0]:]
            un = np.pad(u1_c, bnd_limits, bnd_type)
            ug = un
        err = 1.
        t[it] = t[it-1] + dt
        unnt[:, it] = un

    return t, unnt, errt, countt


def NR_f_u(
    xx: np.ndarray,
    un: np.ndarray,
    uo: np.ndarray,
    dt: float,
    **kwargs,
) -> np.ndarray:
    r"""
    NR F function.

    Parameters
    ----------
    xx : `array`
        Spatial axis.
    un : `array`
        A function that depends on xx.
    uo : `array`
        A function that depends on xx.
    dt : `int`
        Time interval

    Returns
    -------
    `array`
        function  u^{n+1}_{j}-u^{n}_{j} - u^{n}_{j} (u^{n+1}_{j+1} - 2 u^{n+1}_{j} -u^{n+1}_{j-1}) dt
    """


def jacobian_u(
    xx: np.ndarray,
    un: np.ndarray,
    dt: float,
    **kwargs,
) -> np.ndarray:
    """
    Jacobian of the F function.

    Parameters
    ----------
    xx : `array`
        Spatial axis.
    un : `array`
        A function that depends on xx.
    dt : `int`
        Time interval

    Returns
    -------
    `array`
        Jacobian F_j'(u^{n+1}{k})
    """


def Newton_Raphson_u(
    xx: np.ndarray,
    hh: np.ndarray,
    dt: float, 
    nt: int,
    toll: float = 1e-5,
    ncount: int = 2, 
    bnd_type: str = 'wrap',
    bnd_limits: list = [0,1],
    **kwargs,
):
    """
    NR scheme for the burgers equation.

    Parameters
    ----------
    xx : `array`
        Spatial axis.
    hh : `array`
        A function that depends on xx.
    dt : `float`
        Time interval
    nt : `int`
        Number of time iterations.
    toll : `float`
        Error limit.
        By default 1-5
    ncount : `int`
        Maximum number of iterations.
        By default 2
    bnd_type : `string`
        Allows to select the type of boundaries.
        By default, 'wrap'
    bnd_limits : `list(int)`
        Array of two integer elements. The number of pixels that
        will need to be updated with the boundary information.
        By default [1,1]

    Returns
    -------
    t : `array`
        Time.
    unnt : `array`
        Spatial and time evolution of u^n_j for n = (0,nt), and where j represents
        all the elements of the domain.
    errt : `array`
        Error for each timestep
    countt : `array(int)`
        Number iterations for each timestep
    """
    err = 1.
    unnt = np.zeros((np.size(xx), nt))
    errt = np.zeros((nt))
    countt = np.zeros((nt))
    unnt[:, 0] = hh
    t = np.zeros((nt))

    # Looping over time
    for it in range(1, nt):
        uo = unnt[:, it-1]
        ug = unnt[:, it-1]
        count = 0
        # iteration to reduce the error.
        while ((err >= toll) and (count < ncount)):
            jac = jacobian_u(xx, ug, dt) #  Jacobian
            ff1 = NR_f_u(xx, ug, uo, dt) #  F
            # Inversion:
            un = ug - np.matmul(np.linalg.inv(jac), ff1)

            # error
            err = np.max(np.abs(un - ug) / (np.abs(un) + toll))
            errt[it] = err

            # Number of iterations
            count += 1
            countt[it] = count

            # Boundaries
            if bnd_limits[1] > 0:
                u1_c = un[bnd_limits[0]:-bnd_limits[1]]
            else:
                u1_c = un[bnd_limits[0]:]
            un = np.pad(u1_c, bnd_limits, bnd_type)
            ug = un
        err = 1.
        t[it] = t[it-1] + dt
        unnt[:, it] = un

    return t, unnt, errt, countt


def taui_sts(nu: float, niter: int, iiter: int) -> float:
    """
    STS parabolic scheme. [(nu -1)cos(pi (2 iiter - 1) / 2 niter) + nu + 1]^{-1}

    Parameters
    ----------
    nu : `float`
        Coefficient, between (0,1).
    niter : `int`
        Number of time iterations.
    iiter : `int`
        Iterations number

    Returns
    -------
    `float`
        [(nu -1)cos(pi (2 iiter - 1) / 2 niter) + nu + 1]^{-1}
    """


def evol_sts(
    xx: np.ndarray,
    hh: np.ndarray,
    nt: int,
    a: np.ndarray,
    cfl_cut: float = 0.98,
    ddx = lambda x,y: deriv_fwd(x, y),
    bnd_type: str='wrap',
    bnd_limits: list = [0,1],
    nu: float = 0.9,
    n_sts: float = 10,
): 
    """
    Evolution of the STS method. 

    Parameters
    ----------
    xx : `array`
        Spatial axis.
    hh : `array`
        A function that depends on xx.
    nt : `int`
        Number of time iterations.
    a : `float` or `array`
        Either constant or array multiplies the right-hand side of the Burger's eq.
    cfl_cut : `float`
        Constant value to limit dt from cfl_adv_burger.
        By default 0.45
    ddx : `lambda function`
        Allows to change the space derivative function.
        By default lambda x,y: deriv_fwd(x, y)
    bnd_type : `string`
        Allows to select the type of boundaries
        by default 'wrap'
    bnd_limits : `list(int)`
        List of two integer elements. The number of pixels that
        will need to be updated with the boundary information.
        By default, [0,1]
    nu : `float`
        STS nu coefficient between (0,1).
        By default 0.9
    n_sts : `int`
        Number of STS sub iterations.
        By default 10

    Returns
    -------
    t : `array`
        time 1D array
    unnt : `array`
        Spatial and time evolution of u^n_j for n = (0,nt), where j represents
        all the elements of the domain.
    """


def hyman(
    xx: np.ndarray,
    f: np.ndarray,
    dth: float, 
    a: np.ndarray,
    fold: np.ndarray = None,
    dtold: float = None,
    cfl_cut: float = 0.8,
    ddx = lambda x,y: deriv_fwd(x, y),
    bnd_type: str='wrap',
    bnd_limits: list = [0,1],
    **kwargs
):
    """
    Hyman Corrector-predictor method

    Parameters
    ----------
    xx : `array`
        Spatial axis.
    f : `array`
        A function that depends on xx.
    dth : `float`
        Time step interval
    a : `float` or `array`
        Either constant or array multiplies the right-hand side of the Burger's eq.
    fold : `array`
        A function that depends on xx from the previous timestep.
    dtold : `array`
        Time step interval from previous step.
    cfl_cut : `float`
        Constant value to limit dt from cfl_adv_burger.
        By default 0.45
    ddx : `lambda function`
        Allows to change the space derivative function.
        By default lambda x,y: deriv_fwd(x, y)
    bnd_type : `string`
        Allows to select the type of boundaries
        by default 'wrap'
    bnd_limits : `list(int)`
        List of two integer elements. The number of pixels that
        will need to be updated with the boundary information.
        By default, [0,1]

    Returns
    -------
    f : `array`
        Spatial and time evolution of u^n_j for n = (0,nt), where j represents
        all the domain elements.
    fold : `array`
        Spatial and time evolution of u^n_j_1/2 for n = (0,nt), where j represents
        all the domain elements, i.e., from the previous step.
    dt : `float`
        time interval
    """
    dt, u1_temp = step_adv_burgers(xx, f, a, ddx=ddx)

    if (np.any(fold) is None):
        firstit = False
        fold = np.copy(f)
        f = (np.roll(f, 1) + np.roll(f, -1)) / 2.0 + u1_temp * dth
        dtold = dth
    else:
        ratio = dth/dtold
        a1 = ratio**2
        b1 =  dth * (1.0 + ratio)
        a2 =  2. * (1.0 + ratio) / (2.0 + 3.0 * ratio)
        b2 =  dth * (1.0 + ratio**2) / (2.0 + 3.0 * ratio)
        c2 =  dth * (1.0 + ratio) / (2.0 + 3.0 * ratio)

        f, fold, fsav = hyman_pred(f, fold, u1_temp, a1, b1, a2, b2)

        if bnd_limits[1] > 0:
            u1_c = f[bnd_limits[0]:-bnd_limits[1]]
        else:
            u1_c = f[bnd_limits[0]:]
        f = np.pad(u1_c, bnd_limits, bnd_type)

        dt, u1_temp = step_adv_burgers(xx, f, a, cfl_cut, ddx=ddx)

        f = hyman_corr(f, fsav, u1_temp, c2)

    if bnd_limits[1] > 0:
        u1_c = f[bnd_limits[0]:-bnd_limits[1]]
    else:
        u1_c = f[bnd_limits[0]:]
    f = np.pad(u1_c, bnd_limits, bnd_type)

    dtold = dth

    return f, fold, dtold


def hyman_corr(
    f: np.ndarray,
    fsav: np.ndarray,
    dfdt: np.ndarray,
    c2: float
) -> np.ndarray:
    """
    Hyman Corrector step

    Parameters
    ----------
    f : `array`
        A function that depends on xx.
    fsav : `array`
        A function that depends on xx from the interpolated step.
    dfdt : `array`
        A function that depends on xx. The right-hand side of the time derivative.
    c2: `float`
        Coefficient.

    Returns
    -------
    corrector : `array`
        A function of the Hyman corrector step
    """
    return fsav + c2 * dfdt


def hyman_pred(
    f: np.ndarray,
    fold: np.ndarray,
    dfdt: np.ndarray,
    a1: float,
    b1: float,
    a2: float,
    b2: float,
): 
    """
    Hyman Predictor step

    Parameters
    ----------
    f : `array`
        A function that depends on xx.
    fold : `array`
        A function that depends on xx from the previous step.
    dfdt : `array`
        A function that depends on xx. The right-hand side of the time derivative.
    a1: `float`
        Coefficient.
    b1: `float`
        Coefficient.
    a2: `float`
        Coefficient.
    b2: `float`
        Coefficient.

    Returns
    -------
    f : `array`
        A function that depends on xx.
    fold : `array`
        A function that depends on xx from the previous step.
    fsav : `array`
        A function that depends on xx from the interpolated step.
    """
    fsav = np.copy(f)
    tempvar = f + a1 * (fold - f) + b1 * dfdt
    fold = np.copy(fsav)
    fsav = tempvar + a2 * (fsav - tempvar) + b2 * dfdt
    f = tempvar

    return f, fold, fsav
