#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 02 10:25:17 2021

@author: Juan Martinez Sykora

--------------------------------------------------------------------------------------------------

NOTE TO NEW USERS:

--------------------------------------------------------------------------------------------------

"""

# import builtin modules
import os

# import external public "common" modules
import numpy as np 


def deriv_2ndo(xx, hh, **kwargs):
    """
    returns the downwind 2nd order derivative of hh respect to xx. 
    Requires: 
        numpy.roll
    Input: 
        xx :: spatial axis. 
        hh :: function that depends on xx. 
    Output: 
        returns the downwind 2nd order derivative of hh respect to xx. Last 
        grid point is ill calculated. 
    """


def order_conv(hh, hh2, hh4, **kwargs):
    """
    Computes the order of convergence of a derivative function 
    Input: 
        hh  :: function that depends on xx. 
        hh2 :: function that depends on xx but with twice number of grid points than hh. 
        hh4 :: function that depends on xx but with twice number of grid points than hh2.
    Output: 
        returns the order of convergence.  
    """
   

def deriv_4tho(xx, hh, **kwargs): 
    """
    returns the 4th order derivative of hh respect to xx. 
    Requires: 
        numpy.roll
    Input: 
        xx :: spatial axis. 
        hh :: function that depends on xx. 
    Output: 
        returns the centered 4th order derivative of hh respect to xx. Last 2 and first two 
        grid points are ill calculated. 
    """


def step_adv_burgers(xx, hh, a, cfl_cut = 0.98, 
                    ddx = lambda x,y: deriv_2ndo(x, y), **kwargs): 
    """
    Right hand side of Burger's eq. where a can be a constant or a function that 
    depends on xx. 
    Requires: 
        cfl_adv_burger function which computes np.min(dx/a)
    Input:    
        xx :: spatial axis. 
        hh :: function that depends on xx.
        a  :: either constant, or array which multiply the right hand side of the Burger's eq.
        cfl_cut:: constant value to limit dt from cfl_adv_burger. 
        ddx :: lambda function that allows to select the type of spatial derivative
    Output: 
        dt :: time interval
        right hand side of u^{n+1}-u^{n} = from burgers eq, i.e., x \frac{\partial u}{\partial x} * dt
    """    


def cfl_adv_burger(a,x): 
    """
    Computes the dt_fact, i.e., Courant, Fredrich, and 
    Lewy condition for the advective term in the Burger's eq. 
    Requires: 
        numpy gradient, abs, and min
    Input: 
        a :: either constant, or array which multiply the right hand side of the Burger's eq.
        x :: spatial axis. 
    Ouput: 
        min(dx/|a|)
    """
    

def evolv_adv_burgers(xx, hh, nt, a, cfl_cut = 0.98, 
        ddx = lambda x,y: deriv_2ndo(x, y), 
        courant = lambda a, x: cfl_adv_burger(a,x), 
        bnd_type='wrap', bnd_limits=[0,1], **kwargs):
    """
    Advance nt time-steps in time the burger eq for a being a a fix constant or array.
    Requires: 
         step_adv_burgers
         numpy.pad for boundaries. 
    Input: 
        xx :: spatial axis. 
        hh :: function that depends on xx.
        a  :: either constant, or array which multiply the right hand side of the Burger's eq.
        cfl_cut:: constant value to limit dt from cfl_adv_burger. 
        ddx :: Lambda function allows to change the space derivative function. 
        courant:: Lambda function which allows to select the cfl for 
                dt = dt_fact |dx|/|a| expression to define the size of dt 
        bnd_type:: String. It allows to select the type of boundaries 
        bnd_limits:: Array of two integer elements. The number of pixels that
                will need to be updated with the boundary information. 
    Output: 
        t :: time 1D array
        unnt :: Spatial and time evolution of u^n_j for n = (0,nt), and where j represents
        all the elements of the domain. 
    """
 

def deriv_upw(xx, hh, **kwargs):
    """
    returns the upwind 2nd order derivative of hh respect to xx. 
    Requires: 
        numpy.roll
    Input: 
        xx :: spatial axis. 
        hh :: function that depends on xx. 
    Output: 
        returns the upwind 2nd order derivative of hh respect to xx. First 
        grid point is ill calculated. 
    """


def deriv_cent(xx, hh, **kwargs):
    """
    returns the centered 2nd derivative of hh respect to xx. 
    Requires: 
        numpy.roll
    Input: 
        xx :: spatial axis. 
        hh :: function that depends on xx. 
    Output: 
        returns the centered 2nd order derivative of hh respect to xx. First 
        and last grid points are ill calculated. 
    """


def evolv_uadv_burgers(xx, hh, nt, cfl_cut = 0.98, 
        ddx = lambda x,y: deriv_2ndo(x, y), 
        courant = lambda a, x: cfl_adv_burger(a,x), 
        bnd_type='wrap', bnd_limits=[0,1], **kwargs):
    """
    Advance nt time-steps in time the burger eq for a being u.
    Requires: 
         step_uadv_burgers
         numpy.pad for boundaries. 
    Input: 
        xx :: spatial axis. 
        hh :: function that depends on xx.
        cfl_cut:: constant value to limit dt from cfl_adv_burger. 
        ddx :: Lambda function allows to change the space derivative function. 
        courant:: Lambda function which allows to select the cfl for 
                dt = dt_fact |dx|/|a| expression to define the size of dt 
        bnd_type:: String. It allows to select the type of boundaries 
        bnd_limits:: Array of two integer elements. The number of pixels that
                will need to be updated with the boundary information. 
    Output: 
        t :: time 1D array
        unnt :: Spatial and time evolution of u^n_j for n = (0,nt), and where j represents
        all the elements of the domain. 
    """


def evolv_Lax_uadv_burgers(xx, hh, nt, cfl_cut = 0.98, 
        ddx = lambda x,y: deriv_2ndo(x, y), 
        courant = lambda a, x: cfl_adv_burger(a,x), 
        bnd_type='wrap', bnd_limits=[0,1], **kwargs):
    """
    Advance nt time-steps in time the burger eq for a being u using the Lax method.
    Requires: 
         step_uadv_burgers
         numpy.pad for boundaries. 
    Input: 
        xx :: spatial axis. 
        hh :: function that depends on xx.
        cfl_cut:: constant value to limit dt from cfl_adv_burger. 
        ddx :: Lambda function allows to change the space derivative function. 
        courant:: Lambda function which allows to select the cfl for 
                dt = dt_fact |dx|/|a| expression to define the size of dt 
        bnd_type:: String. It allows to select the type of boundaries 
        bnd_limits:: Array of two integer elements. The number of pixels that
                will need to be updated with the boundary information. 
    Output: 
        t :: time 1D array
        unnt :: Spatial and time evolution of u^n_j for n = (0,nt), and where j represents
        all the elements of the domain. 
    """


def step_uadv_burgers(xx, hh, cfl_cut = 0.98, 
                    ddx = lambda x,y: deriv_2ndo(x, y), **kwargs): 
    """
    Right hand side of Burger's eq. where a is u, i.e hh.  
    Requires: 
        cfl_adv_burger function which computes np.min(dx/a)
    Input:    
        xx :: spatial axis. 
        hh :: function that depends on xx.
        cfl_cut:: constant value to limit dt from cfl_adv_burger. 
        ddx :: lambda function that allows to select the type of spatial derivative
    Output: 
        dt :: time interval
        right hand side of u^{n+1}-u^{n} = from burgers eq, i.e., x \frac{\partial u}{\partial x} * dt
    """       
 

def cfl_diff_burger(a,dx): 
    """
    Computes the dt_fact, i.e., Courant, Fredrich, and 
    Lewy condition for the diffusive term in the Burger's eq. 
    Requires: 
        numpy gradient, abs, and min
    Input: 
        a :: either constant, or array which multiply the right hand side of the Burger's eq.
        x :: spatial axis. 
    Ouput: 
        min(dx/|a|)
    """
 

def hyman(f,dvart, dt, *args, **kwargs): 

    deriv_4tho()
    courant()

    if (firstit):
        firstit=False
        dvardt(f)
    else:
        ratio = dt/dtold
        a1 = ratio**2
        b1 =  dt*(1.0+ratio   )
        a2 =  2.*(1.0+ratio   )/(2.0+3.0*ratio)
        b2 =  dt*(1.0+ratio**2)/(2.0+3.0*ratio)
        c2 =  dt*(1.0+ratio   )/(2.0+3.0*ratio)
    hyman_pred(f, fold, fsav, dfdt, a1,b1,a2,b2)
     
    deriv_4tho()
    hyman_corr(f, fsav, dfdt, c2)

    t = t+dt

def hyman_corr(f, fsav, dfdt, c2):

    f =  fsav  + c2* dfdt

def hyman_pred(f, fold, fsav, dfdt, a1, b1, a2, b2): 

    fsav = np.copy(f)
    tempvar = f + a1*(fold-f) + b1*dfdt
    fold = np.copy(fsav)
    fsav = tempvar + a2*(fsav-tempvar) + b2*dfdt    
    f = tempvar

