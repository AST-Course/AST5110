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

* In addition, you will create your own python library.
As a starting point, fork the
[numerical methods repository for AST5110](https://github.com/AST-Course/nm_lib.git).

## Download

In order to solve the excersices, it is highly recommended to create a private fork and provide access to jumasy1980@gmail.com.
This will allow me interactively to follow the progress of each of the students
([fork info](https://gist.github.com/0xjac/85097472043b697ab57ba1b1c7530274)).

## Get jupyter-book

If interested to have a notebook of the exersices and wiki, you can download from ([jupyter-book](https://github.io/AST-Course/AST5110/AST5110.wiki/Home.html)).
# nm_lib

This is intendend for student to develop the library of a numerical code following the [excersices](https://github.com/AST-Course/AST5110/).

Please create [AST 5110 wiki](https://github.com/AST-Course/AST5110/wiki) to add a detailed description about this code and what it can do!

### Fork this repository privately:
[to create a fork follow the instructions](https://gist.github.com/0xjac/85097472043b697ab57ba1b1c7530274)

### In case you want to do the course in a different enviroment, do the following:
```
conda create --name ast5110_course
conda activate ast5110_course
conda install jupyter
pip install matplotlib
```

### To install the files:
```
cd nm_lib
pip install -e .
```

### To start using the library:
Run this code to get started:
```
from nm_lib import nm_lib as nm
```
