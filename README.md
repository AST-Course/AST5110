# README

## Material has been collected by

* F. Moreno-Insertis (2018).<br>
Course on numerical simulation techniques for fluid dynamics.<br>
Universidad de La Laguna (Tenerife, Spain).

* V. H. Hansteen (2018).<br>
AST 5110 Numerical modeling.<br>
University of Oslo (Oslo, Norway).

* W. H. Press et al..<br>
Numerical recipes.<br>
Cambridge University Press.<br>
<http://numerical.recipes>

* Culbert B. Laney.<br>
Computational Gasdynamics.<br>
University of Colorado, Cambridge University Press

* K. W. Morton and D. F. Mayers.<br>
Numerical Solution of Partial Differential Equations: And introduction.<br>
Computing Laboratory, University of Oxford, Cambridge University Press. 


## Dependencies

* Anaconda 3 includes most of the required libraries.

* We will have tests to run in CI/CD, so [pytest](https://docs.pytest.org/) will be convenient. 

* For good practices and clean the code [pre-commit](https://pre-commit.com). Run pre-commit run -a to clean the code. 

* You will also create your own Python library included in this repository (see below). 

## Download

To solve the exercises, it is highly recommended to create a private fork and provide access to jumasy1980@gmail.com.
This will allow me to follow the progress of each of the students
([fork info](https://gist.github.com/0xjac/85097472043b697ab57ba1b1c7530274)).

## Get jupyter-book

If you are interested in having a notebook of the exercises and wiki, you can download them from ([jupyter-book](https://github.io/AST-Course/AST5110/AST5110.wiki/Home.html)).
# nm_lib

This is intended for students to develop the library of a numerical code following the [excersices](https://github.com/AST-Course/AST5110/).

Please create [AST 5110 wiki](https://github.com/AST-Course/AST5110/wiki) to add a detailed description of this code and what it can do!

### Fork this repository privately:
[to create a fork follow the instructions](https://gist.github.com/0xjac/85097472043b697ab57ba1b1c7530274)

### It is recommended that you setup a separate (conda/mamba) environement for this course using the following:
```
mamba create --name ast5110_course python=3.11
mamba activate ast5110_course
mamba install --file requirements.txt
```

### To install the files:
In the root folder (`AST5110/`), which contains the `setup.cfg` and `setup.py` files run:
```
pip install -e .
```

### To start using the library:
Run this code to get started:
```
import nm_lib as nm
```

## Wiki
The AST5110 wiki is added here as a git submodule. To clone the wiki, run:
```
git submodule init
git submodule update
```
