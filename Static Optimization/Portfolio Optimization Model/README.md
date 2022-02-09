# Portfolio Optimization Model Folder

This folder contains the complete explanation and the code to replicate a portfolio optimization model with the characteristics that was explained in [*Static Optimization*](https://github.com/JuanPChicaC/Optimization/tree/main/Static%20Optimization) directory in section ***Portfolio Optiomization Model***

### [Portfolio Optimization.ipynb](https://github.com/JuanPChicaC/Optimization/blob/main/Static%20Optimization/Portfolio%20Optimization%20Model/Portfolio%20Optimization%20Model.ipynb)
This file contains all the theoric and functionality explanation to implement a portfolio optimization Model. There can be finded graphs, equation and methods used to generate a solution about the problem of investment selection

### [Generalization.py](https://github.com/JuanPChicaC/Optimization/blob/main/Static%20Optimization/Portfolio%20Optimization%20Model/generalization.py)
This file contains the classes that were used in the section ***Generalization for n-stocks portfolio*** in the file ***Portfolio Optimization.ipynb***. The class *Price_Array* contains the methods and attributes required to standarize an income for the optimization model,
the general porpouse of this class is generate a price DataFrame just asking as an input the Symbols of the stocks published in yahoo finance. On the other hand, the class *Portfolio* contains all the solution for a portfolio optimization problem just receiving as input
a DataFrame with prices and symbols that want to be optimized. The idea is that this file could be used as a library for anyone that want to implement a solution for portfolio optimization problems
