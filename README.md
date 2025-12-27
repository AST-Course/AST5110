# AST5110/AST9110: Numerical Modeling

Welcome to AST5110, a course on numerical modeling with applications to astrophysics. This wiki contains the **theoretical background, explanations, and practical guidance** needed to complete the course exercises and projects. The course focuses on understanding, implementing, and testing numerical methods for solving **partial differential equations (PDEs)** relevant to astrophysical problems.


The course begins with the discretization of functions and their convergence. Utilizing Burger's equation, we explore stability using different spatial derivatives. Key elements such as time advancement and initial validation tests are integral to this phase. These tests also facilitate the integration of a Continuous Integration (CI) pipeline, ensuring code reliability for each new commit in the _nm_lib_ library.

We then delve into the von Neumann stability analysis to constrain the timeste of time derivatives in various Partial Differential Equations (PDEs). The course covers explicit, semi-implicit, and implicit methods combined with operator splitting and numerical analytical techniques to address diffusive term challenges. Students will have the opportunity to implement these methods in their code.

The curriculum expands to include a broader range of terms, variables, and equations necessary for solving hydrodynamic equations. During this segment, students will implement operator splitting, gaining insights into its applicability and limitations, and focusing on stellar and solar atmospheric problems.

Optionally, students can enhance their skills by extending their code to 2D or 3D models, incorporating new physical phenomena, or conducting and analyzing various numerical experiments tailored to their interests.

## 📚 Topics Covered

Numerical simulations are a cornerstone of modern astrophysics. In this course, you will learn how to:

**Mathematical and Numerical Foundations**
- [Discretization](Discretization): Basics of numerical discretization
- [Introduction to PDEs and Classifications](Introduction-to-PDEs-and-classifications): Fundamentals of Partial Differential Equations and their classifications.
- [Error analysis](Errors): Insight into various computational error types.
- [Stability Concepts](Stability): Explore Von Neumann analysis, the CFL condition, and stability principles.

**Numerical Schemes and Methods**
- [Basic Numerical Schemes](Examples-of-hyperbolic-numerical-schemes-book)
- [Hyper Diffusive methods](Hyper-diffusive)
- [Riemann Solvers](Riemann-solvers)
- [Staggered Mesh techniques](Staggered-mesh)
- [Implicit Methods](Implicit-methods)  
- [Newton-Raphson Method](Newton-Raphson-method)
- [Crank-Nicolson in Multidimensions](Crank-Nicolson-in-Multidimensions)
- [Super Time Stepping](Super-time-stepping)
- [Operator Splitting](Operator-splitting)  

**Special Topics and Applications**
- [Self-similar Solution for Parabolic Eq.](Self-similar-solution-for-parabolic-eq)


## 📁 Repository Structure

The course contains two repositories and a wiki. This repository is organized into:

- [notebooks](https://github.com/AST-Course/AST5110) — Exercises and experiments.  
- [nm_lib](https://github.com/AST-Course/nm_lib) — Core numerical routines.
- [wiki](https://github.com/AST-Course/AST5110/wiki/Home) — Documentation, guidelines, theory and derivations.



## 🚀 Getting Started

1. **Create a Private Fork**: Start your journey by establishing a private fork of the course repository. Follow the detailed [instructions for setting up a private fork](https://github.com/AST-Course/AST5110/wiki/Setup-private-fork) to get started.

2. **Environment Setup**: Prepare your Python environment in line with the course requirements. The [Python environment setup guide](https://github.com/AST-Course/AST5110/wiki/Setup-python-environment) will walk you through the necessary steps.

3. ** Setup nm lib**: Follow the README in [nm_lib](https://github.com/AST-Course/nm_lib).

- `nm_lib`: A library of essential functions used throughout the course.
- `pyproject.toml`, `requirements.txt`: Setup files to configure the course environment.

4. **Course Familiarization**: Familiarize yourself with the overall structure of the course, including the repository layout and the wiki. Explore the course [concepts and notebooks](https://github.com/AST-Course/AST5110/wiki/Notebooks-and-concepts) to understand the core components.

5. **Exercise Instructions**: Engage with the course exercises in the `notebooks/` directory. All the necessary guidelines are in the [exercise instructions](https://github.com/AST-Course/AST5110/wiki/Exercise-instructions).

6. **Jupyter Book**: To access a compiled notebook that combines both exercises and the wiki, follow the [guide to setting up GitHub Pages](https://github.com/AST-Course/AST5110/wiki/Setup-GitHub-pages-for-private-fork). This will help you configure GitHub Pages to view the course content in a structured, book-like format.

## 🔗 Important Pages

- [AST5110: Course Overview](https://www.uio.no/studier/emner/matnat/astro/AST5110/index-eng.html)
- [Course Wiki](https://github.com/AST-Course/AST5110/wiki)
- [Course Notebooks](https://github.com/AST-Course/AST5110)
- [Course library](https://github.com/AST-Course/nm_lib)


## Further Reading and References 

The course material is compiled from diverse resources, including:

## Core Numerical PDE & Scientific Computing

1. **LeVeque, R. J.**  
   *Finite Volume Methods for Hyperbolic Problems*  
   Cambridge University Press, 2002  
   https://doi.org/10.1017/CBO9780511791253

2. **LeVeque, R. J.**  
   *Numerical Methods for Conservation Laws*  
   Birkhäuser, 1992  
   https://link.springer.com/book/10.1007/978-3-0348-8629-1

3. **Strikwerda, J. C.**  
   *Finite Difference Schemes and Partial Differential Equations*  
   SIAM, 2nd ed., 2004  
   https://epubs.siam.org/doi/book/10.1137/1.9780898717938

4. **Morton, K. W., & Mayers, D. F.**  
   *Numerical Solution of Partial Differential Equations*  
   Cambridge University Press, 2005  
   https://doi.org/10.1017/CBO9780511812248

## Implicit Methods & Time Integration

5. **Ascher, U. M., & Petzold, L. R.**  
   *Computer Methods for Ordinary Differential Equations and Differential-Algebraic Equations*  
   SIAM, 1998  
   https://epubs.siam.org/doi/book/10.1137/1.9781611971392

6. **Hundsdorfer, W., & Verwer, J. G.**  
   *Numerical Solution of Time-Dependent Advection-Diffusion-Reaction Equations*  
   Springer, 2003  
   https://link.springer.com/book/10.1007/978-3-662-09017-6

7. **Alexiades, V., Amiez, G., & Gremaud, P.-A.**  
   *Super-Time-Stepping Acceleration of Explicit Schemes for Parabolic Problems*  
   Communications in Numerical Methods in Engineering, 1996  
   https://doi.org/10.1002/(SICI)1099-0887(199610)12:1<31::AID-CNM453>3.0.CO;2-O

## Computational Physics & Applied Methods

8. **Toro, E. F.**  
   *Riemann Solvers and Numerical Methods for Fluid Dynamics*  
   Springer, 3rd ed., 2009  
   https://link.springer.com/book/10.1007/b79761

9. **Fletcher, C. A. J.**  
   *Computational Techniques for Fluid Dynamics*  
   Springer, 1991  
   https://link.springer.com/book/10.1007/978-3-642-97088-7

10. **Laney, C. B.**  
    *Computational Gasdynamics*  
    Cambridge University Press, 1998  
    https://doi.org/10.1017/CBO9780511605604

11. **W. H. Press et al.** 
    Cambridge University Press.
    [Numerical Recipes](http://numerical.recipes)

12. **Å. Nordlund & K. Galsgaard** 
    *A 3D MHD code for Parallel Computers*
    1995

13. **B. Gudiksen et al.** 
    A&A 531, A154, 2011: The stellar atmosphere simulation code Bifrost: Code description and validation
    https://www.aanda.org/articles/aa/pdf/2011/07/aa16520-11.pdf

14. **Q. Wargnier et al. (2025)**
    *Time-Adaptive PIROCK Method with Error Control for Multi-Fluid and Single-Fluid MHD Systems*
    A&A 695, A262
    https://ui.adsabs.harvard.edu/abs/2024arXiv240915552W/abstract

## Self-Similarity & Theory

15. **Pattle, R. E.**
    Q. J. Mech. Appl. Math., 12, 407, 1959
    https://academic.oup.com/qjmam/article/12/4/407/1851084

16. **Furuseth, S. V., Cherry, G., & Martínez-Sykora, J.** 
    A&A, 659, A186, 2024
    https://doi.org/10.1051/0004-6361/202451707

17. **Moreno-Insertis, F., Nóbrega-Siverio, D., Priest, E. R., & Hood, A. W.**
    A&A, 662, A42, 2022
    https://www.aanda.org/articles/aa/pdf/2022/06/aa41449-21.pdf

18. **Barenblatt, G. I.**  
    *Scaling, Self-Similarity, and Intermediate Asymptotics*  
    Cambridge University Press, 1996  
    https://doi.org/10.1017/CBO9780511599149

19. **Evans, L. C.**  
    *Partial Differential Equations*  
    AMS, 2nd ed., 2010  
    https://bookstore.ams.org/gsm-19

## Python, Reproducibility & Workflow

20. **Langtangen, H. P.**  
    *A Primer on Scientific Programming with Python*  
    Springer, 2016  
    https://link.springer.com/book/10.1007/978-3-662-49887-3

21. **Wilson et al.**  
    *Best Practices for Scientific Computing*  
    PLOS Biology, 2014  
    https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1001745

22. **Jupyter Book Documentation**  
    https://jupyterbook.org

## Other courses ##

23. F. Moreno-Insertis 
    Numerical simulation techniques for fluid dynamics, Universidad de La Laguna.
    2018

24. V. H. Hansteen 
    AST 5110 Numerical modeling, University of Oslo
    2018


## 📌 Tips for Success

- Read the theory **before** coding
- Test your implementations on simple cases first
- Think about **stability and errors**, not just whether the code runs
- Ask questions early if something is unclear
