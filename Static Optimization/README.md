# Static Optimization Folder

This repository contains proposal and solution for several optimization problems, with non time variant condition.

## [Portfolio optimization Model](https://github.com/JuanPChicaC/Optimization/tree/main/Static%20Optimization/Portfolio%20Optimization%20Model)

This model was created by **Harry Markowitz** in 1952 *(Portfolio Selection, The Journal of Finance)*. It contains the solution for the optimal percentage of investment that each financial asset has in the way to maximize the investment or minimize the risk of the entire portfolio.

*Reference: https://www.math.ust.hk/~maykwok/courses/ma362/07F/markowitz_JF.pdf*

In this file, an alternative for the original optimization problem is presented. The main objective is to find an optimal combination of assets minimizing the variation coefficient of all the portfolio. In financial terms, it means minimice the risk by each monetary unit that is expected to be returned from the portfolio.

Also, please note that the studied assets should be considered as an investment project. Based on the principle of value in time, the expected return will be calculated as a geometric mean of the increments in the value. Risk will be computed as a geometric standard deviation for the same variable.

A proposed solution for a portfolio compossed by two assets is presented in order to better explain the problem. Lately, a general solution is developed for the n assets portfolio case. The model is the income for [Portfolio Optimization Service](https://github.com/JuanPChicaC/WebDevelopment/tree/main/API/Portfolio%20Optimization%20Service). this service is an API  to deliver optimal portfolios to any client that require it.

