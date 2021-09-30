from scipy.optimize import minimize
import numpy as np
from math import exp
import pandas as pd
from itertools import combinations_with_replacement, combinations,product
#customers=[(5,10,200),(10,5,150),(0,12,200),(12,0,300)]
medias=[]



#with open('LocationModel.csv') as csvfile:
 #   customers=np.loadtxt(csvfile, delimiter=',')

df1 = pd.read_excel('AdvertisingModel.xlsx', header=1,sheet_name="AM1")
for row in df1.itertuples():
    medias.append(tuple(row)[2:])
    
#print(medias)


RequiredExposures=[60,60,28,60,60,28] #123



'''
df2 = pd.read_excel('AdvertisingModel.xlsx', header=1,sheet_name="Coefficient")
for row in df2.itertuples():
    coefficients.append(tuple(row)[2:])

df3 = pd.read_excel('AdvertisingModel.xlsx', header=1,sheet_name="Required Exposures")
for row in df3.itertuples():
    Required.append(tuple(row)[1:])

df4=pd.read_excel('AdvertisingModel.xlsx',sheet_name="CostPerID")
CostPerID=tuple(df4)[1:]
print(CostPerID)

print(constants)
print(coefficients)
print(Required)
print(CostPerID)
'''
'''
medias = [(93.061,61.129,33.376,105.803,71.784,56.82,0.029,0.084,0.071,0.035,0.089,0.01,140),]
'''

def objective(x):
    cost=0
    for idx, media in enumerate(medias):
        cost += x[idx]*media[12] 
    return cost

def constraint0(x):
    exposure=0
    for idx, media in enumerate(medias):
        exposure += media[0]*(1-exp(-media[6]*x[idx]))
    return exposure-RequiredExposures[0]

def constraint1(x):
    exposure=0
    for idx, media in enumerate(medias):
        exposure += media[1]*(1-exp(-media[7]*x[idx]))
    return exposure-RequiredExposures[1]

def constraint2(x):
    exposure=0
    for idx, media in enumerate(medias):
        exposure += media[2]*(1-exp(-media[8]*x[idx]))
    return exposure-RequiredExposures[2]

def constraint3(x):
    exposure=0
    for idx, media in enumerate(medias):
        exposure += media[3]*(1-exp(-media[9]*x[idx]))
    return exposure-RequiredExposures[3]

def constraint4(x):
    exposure=0
    for idx, media in enumerate(medias):
        exposure += media[4]*(1-exp(-media[10]*x[idx]))
    return exposure-RequiredExposures[4]

def constraint5(x):
    exposure=0
    for idx, media in enumerate(medias):
        exposure += media[5]*(1-exp(-media[11]*x[idx]))
    return exposure-RequiredExposures[5]



x0=[5,0,3,22,15,8,13,0]
b=(0,30)
bnds=(b,b,b,b,b,b,b,b)
con0 = {'type': 'ineq', 'fun': constraint0}
con1 = {'type': 'ineq', 'fun': constraint1}
con2 = {'type': 'ineq', 'fun': constraint2}
con3 = {'type': 'ineq', 'fun': constraint3}
con4 = {'type': 'ineq', 'fun': constraint4}
con5 = {'type': 'ineq', 'fun': constraint5}
cons=[con0,con1,con2,con3,con4,con5]
sol=minimize(objective,x0, bounds=bnds,constraints=cons)
#print(sol)

x1=[sol.x[0],sol.x[1],sol.x[2],sol.x[3],sol.x[4],sol.x[5],sol.x[6],sol.x[7]]

#print(x1)

x2=[]
for element in x1:
    x2.append(int(element))

print(x2)




arr=np.arange(-4,4)
r=8

#print('test',constraint0(x2))
combinations=list(product(arr, repeat=r))

print('len_combinations', len(combinations))
good_combinations=[]
for combination in combinations:
    combination=list(np.sum([combination,x2],axis=0))
    if not any(x<0 for x in combination):
        if constraint0(combination)>=0:
            if constraint1(combination)>=0:
                if constraint2(combination)>=0:
                    if constraint3(combination)>=0:
                        if constraint4(combination)>=0:
                            if constraint5(combination)>=0:
                                good_combinations.append(combination)
                            
                                                        
print('len_good_combinations', len(good_combinations))
print(good_combinations[0], type(good_combinations[0]))

print([5,0,3,22,15,8,13,0] in good_combinations)


values=[]

for combination in good_combinations:
    values.append(objective(combination))



min_value = min(values)

min_indices = [index for index, element in enumerate(values) if element == min_value]


for min_index in min_indices:
    print(good_combinations[min_index])

'''
import itertools

square = [a, s, d, f, g, h, j, k, l ]
circle = [w, e, r, t, z, u, i, o, p ]
line = [y, x, c, v, b, n, m ]
radiusshape = [1, 2, 3, 4, 5, 6, 7, 8, 9 ]

for L in range(0, len(stuff)+1):
  for subset in itertools.combinations(stuff, L):
    print(subset)
'''

'''
arr=np.arange(-3,3)
r=8
#print(list(combinations_with_replacement(arr, r)))
#combinations=list(combinations_with_replacement(arr, r))
combinations=list(product(arr, repeat=r))


a=(5,0,3,22,15,8,13,0)
#print(a in combinations)

good_combinations=[]
for combination in combinations:
    if constraint0(combination)>=0:
        if constraint1(combination)>=0:
            if constraint2(combination)>=0:
                if constraint3(combination)>=0:
                    if constraint4(combination)>=0:
                        if constraint5(combination)>=0:
                            good_combinations.append(combination)

#print('PT', a in good_combinations)
#print(len(good_combinations))

values = []

for combination in good_combinations:
    values.append(objective(combination))

min_value = min(values)
min_index = values.index(min_value)

print(good_combinations[min_index])
'''