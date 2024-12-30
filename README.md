# AST5110/AST9110: Numerical Modeling

Welcome to AST5110/AST9110, a course that explores numerical techniques in astrophysical research. The course begins with the discretization of analytical functions and the convergence of the discretization. Utilizing Burger's equation, we explore stability using different spatial derivatives. Key elements such as time advancement and initial validation tests are integral to this phase. These tests also facilitate the integration of a Continuous Integration (CI) pipeline, ensuring code reliability for each new commit in the `nm_lib` library.

We then delve into the von Neumann stability analysis to constrain the timestep of time derivatives in various Partial Differential Equations (PDEs). The course covers explicit, semi-implicit, and implicit methods combined with operator splitting and numerical analytical techniques to address diffusive term challenges. Students will have the opportunity to implement these methods in their code.

The curriculum expands to include a broader range of terms, variables, and equations necessary for solving hydrodynamic equations. During this segment, students will implement operator splitting, gaining insights into its applicability and limitations, and focusing on stellar and solar atmospheric problems.

Optionally, students can enhance their skills by extending their code to 2D or 3D models, incorporating new physical phenomena, or conducting and analyzing various numerical experiments tailored to their interests.

## Repository Structure

Our repository is organized into:

- `notebooks/`: Jupyter Notebooks containing exercises, examples, and projects.
- `AST5110.wiki/`: Extensive wiki pages detailing each covered topic.

There is another repository `nm_lib/`, which includes of essential functions used throughout the course.

## Getting Started

1. **Create a Private Fork**: Start your journey by establishing a private fork of the course repository. Follow the detailed [instructions for setting up a private fork](https://github.com/a04051127/AST5110/wiki/Setup-private-fork) to get started.

2. **Environment Setup**: Prepare your Python environment in line with the course requirements. The [Python environment setup guide](https://github.com/AST-Course/AST5110/wiki/Setup-python-environment) will walk you through the necessary steps, including __the installation of `nm_lib`__.

3. **Notebooks and concepts**: Familiarize yourself with the overall structure of the course, including the repository layout and the wiki. Explore the course [notebooks and concepts](https://github.com/AST-Course/AST5110/wiki/Notebooks-and-concepts) to understand the core components.

4. **Exercise Instructions**: Engage with the course exercises in the `notebooks/` directory. All the necessary guidelines are in the [exercise instructions](https://github.com/AST-Course/AST5110/wiki/Exercise-instructions).

5. **Jupyter Book**: To access a compiled notebook that combines both exercises and the wiki, follow the [guide to setting up GitHub Pages](https://github.com/AST-Course/AST5110/wiki/Setup-GitHub-pages-for-private-fork). This will help you configure GitHub Pages to view the course content in a structured, book-like format.

## Important Links

- [AST5110: Course Overview](https://www.uio.no/studier/emner/matnat/astro/AST5110/index-eng.html)
- [AST9110: Course Overview](https://www.uio.no/studier/emner/matnat/astro/AST9110/index-eng.html)
- [Course Repository](https://github.com/AST-Course/AST5110)

## Course Materials:

Start learning numerical modeling from [here](https://github.com/AST-Course/AST5110/wiki/Home).
