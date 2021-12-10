# Portfolio Optimization Folder

This folder contains the complete explanation and the code to replicate a portfolio optimization model with the characteristicis that was explained in https://github.com/JuanPChicaC/Optimization/tree/main/Static%20Optimization

### Portfolio Optimization.ipynb
This file contains all the theoric and functionality explanation to implement a portfolio optimization Model. There can be finded graphs, equation and methods used to generate a solution about the problem of investment selection

### Generralization.py
This file contain the classes that were used in the section "Generalization for n-stocks portfolio". The class *Price_Array* contain the methods and attributes required to standarize an income for the optimization mode,
the general porpouse of this class is generate a price DataFrame just asking as an input the Symbol of the stocks published in yahoo finance. On the other hand, the class Portfolio, contain all the solution for a portfolio optimization problem just receiving as input
a DataFrame with prices and symbols that want to be optimized. The idea is that this file could be used as a library for anyone that want to implement a solution for portfolio optimization problems
