# -*- coding: utf-8 -*-
"""class 4 problem 1 offline

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1b1FlV6lo-nDxUESU_e-QBtzz-1yE-AJg
"""

# libraries
import random 
import math
import numpy as np 
import matplotlib.pyplot as plt
random.seed(10)



def monte_carlo(N):

  A = 0 
  B = 2
  y_values = []
  y_square_values =[]
  for i in range(1,N+1):
    # x random value generation
    x = random.uniform(A,B)
    # calculating y 
    y = (x**2) * math.exp(-x) * math.log(x+2)
    # store y and y^2 values in  lists
    y_values.append(y)
    y_square_values.append(y*y)

  # calculate avg valus for y and y^2
  y_average = sum(y_values) / len(y_values)
  y_square_average = sum(y_square_values) / len(y_square_values)

  # intregal area value
  area_by_integral = y_average * (B-A) 
  print("For number of sample points: ", N)
  print("Integral Value: ",area_by_integral)

  # error estimate
  error = ( (B-A) / math.sqrt(N) ) * math.sqrt(y_square_average - y_average**2)
  print("Estimated Error: ", error)
  print("")
  return error

N =[100,1000,5000,10000]
est_error_list = []
for i in N: 
  est_error_list.append(monte_carlo(i))
#print(est_error_list)
# bar plot 
sample_points = ["100","1000","5000","10000"]
plt.bar(sample_points, est_error_list,color = "green")
plt.xlabel("Value of n (number of points)")
plt.ylabel("Error Estimate")
plt.show()