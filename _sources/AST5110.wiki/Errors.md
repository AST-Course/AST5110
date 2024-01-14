# Errors

Exercises [ex_1b](https://github.com/AST-Course/AST5110/blob/main/ex_1b_v1.5.ipynb), and [ex_3](https://github.com/AST-Course/AST5110/blob/main/ex_3a.ipynb) summarizes the most common errors we can find in any numerical code. Here we classified those types of errors with a brief description of each.

These errors come from the fact that: 1) space and time are discretized, 2) the information in each grid point has a fixed (and limited) number of bits (floating number), and 3) the methods can be unstable, 4) or non-conservatives.

| Type of error   | Description |
| ---            | ---                 |
| Floating point | Any number (real, imaginary, complex, or integer) is limited to the number of bits used to define them |
| Roundoff error | Arithmetic among numbers in floating-point representations is not exact and characteristic of computer hardware. For instance, if two operands differ largely in magnitude, the smaller operand is effectively replaced by zero. |
| Truncation error | It is characterized by the program or algorithm which, typically, computes discrete approximations of some desired continuous quantity, e.g., discretization of the numerical domain  |
| Stability | The methods can be unstable. In this case, the roundoff error is magnified exponentially. These are also known as amplitude errors. |
| Conservation | Other varieties of error are phase errors which shift our concern to accuracy rather than stability.   |
