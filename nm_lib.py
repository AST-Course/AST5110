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
import matplotlib.pyplot as plt 


def disc_func(func = lambda x: np.sin(x), nump=65, x0=0, xf=50):
    """
    This function discretize any function (hh) of a single 
    variable (xx). 
    Consider to use lambda function in python 
    (https://realpython.com/python-lambda/)
    """

    return xx, hh

def deriv_2ndo(xx, hh):
    """
    returns the 2nd order derivative of hh respect to xx
    """
   
    return hp

def order_conv(xx, hh):
    """
    Computes the order of convergence of a derivative function 
    - Depends on: 
        * disc_func
        * deriv_2ndo
    """
   
    return m

def deriv_4tho(xx, hh): 
    """
    returns the 4th order derivative of hh respect to xx
    """
   
    return hp

def deriv_upw(xx, hh):
    """
    returns the up wind, i.e., not centered, ?? order derivative of hh respect to xx
    """
   
    return hp

def deriv_dnw(xx, hh):
    """
    returns the down wind, i.e., not centered, ?? order derivative of hh respect to xx
    """
   
    return hp

def right_burgers(xx, hh, ddx = lambda x: deriv_2ndo(xx, hh),
                  cha_vel = lambda x: deriv_2ndo(xx, hh)):
    """
    Right hand side of Burger's eq. /
    """
   
    return brg

def dvardt(xx, hh, dt_fact=0.98, 
           righteq = lambda x: right_burgers(xx, hh)):
    """
    Advance a time-step in time. Uses the derivative 
    function. Lambda function allows to change the 
    derivative function. 
    Use dt = dt_fact |dx|/|a| expression to define the 
    size of dt 
    """
   
    return un1


def evolv(xx, hh, nt, 
          ddt = lambda x: dvardt(xx, hh)):
    """
    Advance nt time-step in time. 
    Lambda function allows to change the time 
    derivative function. 
    Use dt = dt_fact |dx|/|a| expression to define the 
    size of dt 
    Use **kwargs to transfer inputs from one to another 
    function. 
    """
   
    return unnt 

def cfl_burger(a,dx): 
    """
    Computes the dt_fact, i.e., Courant, Fredrich, and 
    Lewy condition
    """