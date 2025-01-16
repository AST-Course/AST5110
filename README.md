# AST5110/AST9110: Numerical Modeling

Welcome to AST5110/AST9110, a course that explores numerical techniques in astrophysical research. The course begins with the discretization of functions and their convergence. Utilizing Burger's equation, we explore stability using different spatial derivatives. Key elements such as time advancement and initial validation tests are integral to this phase. These tests also facilitate the integration of a Continuous Integration (CI) pipeline, ensuring code reliability for each new commit in the _nm_lib_ library.

We then delve into the von Neumann stability analysis to constrain the timeste of time derivatives in various Partial Differential Equations (PDEs). The course covers explicit, semi-implicit, and implicit methods combined with operator splitting and numerical analytical techniques to address diffusive term challenges. Students will have the opportunity to implement these methods in their code.

The curriculum expands to include a broader range of terms, variables, and equations necessary for solving hydrodynamic equations. During this segment, students will implement operator splitting, gaining insights into its applicability and limitations, and focusing on stellar and solar atmospheric problems.

Optionally, students can enhance their skills by extending their code to 2D or 3D models, incorporating new physical phenomena, or conducting and analyzing various numerical experiments tailored to their interests.

## Course Structure

- [**Discretization**](https://github.com/AST-Course/AST5110/wiki/Discretization): Delve into discretizing continuous models.
- [**Introduction to PDEs and Classifications**](https://github.com/AST-Course/AST5110/wiki/Introduction-to-PDEs-and-classifications): Fundamentals of Partial Differential Equations and their classifications.
- [**Errors**](https://github.com/AST-Course/AST5110/wiki/Errors): Insight into various computational error types.
- [**Stability**](https://github.com/AST-Course/AST5110/wiki/Stability): Explore Von Neumann analysis, the CFL condition, and stability principles.
- [**Numerical Schemes**](https://github.com/AST-Course/AST5110/wiki/Examples-of-hyperbolic-numerical-schemes-book):
  - [Hyper Diffusive methods](https://github.com/AST-Course/AST5110/wiki/Hyper-diffusive)
  - [Riemann Solvers](https://github.com/AST-Course/AST5110/wiki/Riemann-solvers)
  - [Staggered Mesh techniques](https://github.com/AST-Course/AST5110/wiki/Staggered-mesh)
- [**Implicit Methods**](https://github.com/AST-Course/AST5110/wiki/Implicit-methods): 
  - [Newton-Raphson Method](https://github.com/AST-Course/AST5110/wiki/Newton-Raphson-method)
  - [Crank-Nicolson in Multidimensions](https://github.com/AST-Course/AST5110/wiki/Crank-Nicolson-in-Multidimensions)
  - [Super Time Stepping](https://github.com/AST-Course/AST5110/wiki/Super-time-stepping)
  - [Self-similar Solutions for Parabolic Equations](https://github.com/AST-Course/AST5110/wiki/Self-similar-solution-for-parabolic-eq)
- [**Operator Splitting**](https://github.com/AST-Course/AST5110/wiki/Operator-splitting): Techniques and applications.

## Repository Structure

Our repository is organized into:

- `notebooks/`: Jupyter Notebooks containing exercises, examples, and projects.
- `AST5110.wiki/`: Extensive wiki pages detailing each covered topic.

## Getting Started

1. **Create a Private Fork**: Start your journey by establishing a private fork of the course repository. Follow the detailed [instructions for setting up a private fork](https://github.com/AST-Course/AST5110/wiki/Setup-private-fork) to get started.

2. **Environment Setup**: Prepare your Python environment in line with the course requirements. The [Python environment setup guide](https://github.com/AST-Course/AST5110/wiki/Setup-python-environment) will walk you through the necessary steps.

3. ** Setup nm lib**: Follow the README in [nm_lib](https://github.com/AST-Course/nm_lib).
- `nm_lib`: A library of essential functions used throughout the course.
- `setup.py`, `requirements.txt`: Setup files to configure the course environment.

4. **Course Familiarization**: Familiarize yourself with the overall structure of the course, including the repository layout and the wiki. Explore the course [concepts and notebooks](https://github.com/AST-Course/AST5110/wiki/Notebooks-and-concepts) to understand the core components.

5. **Exercise Instructions**: Engage with the course exercises in the `notebooks/` directory. All the necessary guidelines are in the [exercise instructions](https://github.com/AST-Course/AST5110/wiki/Exercise-instructions).

6. **Jupyter Book**: To access a compiled notebook that combines both exercises and the wiki, follow the [guide to setting up GitHub Pages](https://github.com/AST-Course/AST5110/wiki/Setup-GitHub-pages-for-private-fork). This will help you configure GitHub Pages to view the course content in a structured, book-like format.

## Important Links

- [AST5110: Course Overview](https://www.uio.no/studier/emner/matnat/astro/AST5110/index-eng.html)
- [AST9110: Course Overview](https://www.uio.no/studier/emner/matnat/astro/AST9110/index-eng.html)
- [Course Wiki](https://github.com/AST-Course/AST5110/wiki)
- [Course Repository](https://github.com/AST-Course/AST5110)


## Further Reading

The course material is compiled from diverse resources, including:

- F. Moreno-Insertis (2018): Numerical simulation techniques for fluid dynamics, Universidad de La Laguna.
- V. H. Hansteen (2018): AST 5110 Numerical modeling, University of Oslo.
- W. H. Press et al.: [Numerical Recipes](http://numerical.recipes), Cambridge University Press.
- Culbert B. Laney: Computational Gasdynamics, Cambridge University Press.
- K. W. Morton and D. F. Mayers: Numerical Solution of Partial Differential Equations, Cambridge University Press.
- Å. Nordlund & K. Galsgaard (1995): A 3D MHD code for Parallel Computers.
- B. Gudiksen et al. (2011): The stellar atmosphere simulation code Bifrost: Code description and validation, [A&A 531, A154](https://www.aanda.org/articles/aa/pdf/2011/07/aa16520-11.pdf).
