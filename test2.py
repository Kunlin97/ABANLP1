from numpy.lib.function_base import average
from scipy.optimize import minimize
from numpy import mean
import numpy as np
from math import exp
import pandas as pd
from itertools import combinations_with_replacement, combinations,product

df1 = pd.read_excel('PortfolioAnalysis.xlsx', header=1,)

print(df1)
A=np.array(df1)
print(A)
AT=np.transpose(A)
print(AT)

averages=[]
for annualReturn in AT:
    averages.append(np.mean(annualReturn))

covMatrix = np.cov(AT, bias=True)


def constraint0(x):
    sum=1
    for xi in x:
        sum -= xi
    return sum

def constraint1(x):
    annualReturn=0.12
    expectedReturn = np.dot(x,averages)
    return annualReturn-expectedReturn

def objective(x):
    return np.sum(np.dot(x,covMatrix)*x)

#0.000957216	0.001169159	0.001224051
x0=np.array([0.2,0.6,0.1])

#print(averages)
#print(objective(x))

con0 = {'type': 'eq', 'fun': constraint0}
con1 = {'type': 'ineq', 'fun': constraint1}
cons=[con0, con1]

sol=minimize(objective,x0,constraints=cons)

print(sol)

print(objective(sol.x))