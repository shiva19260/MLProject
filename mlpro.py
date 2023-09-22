
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#plt.style.use('./deeplearning.mplstyle')
x_train = np.array([1.0, 5.0])
y_train = np.array([300.0, 500.0])
print(f"x_train = {x_train}")
print(f"y_train = {y_train}")

print(f"x_train.shape: {x_train.shape}")
m = x_train.shape[0]
print(f"Number of training examples is: {m} ")

m = len(x_train)
print(f"Number of training examples is: {m}")
i = 0
x_i = x_train[i]
y_i = y_train[i]
print(f"(x^({i}), y^({i}) = ({x_i}, {y_i})")
plt.scatter(x_train,y_train, marker = 'x' , c = 'r')
plt.title("Housing Prices")
plt.ylabel('Price(in 1000s of dollars)')
plt.xlabel('size (1000 sqft)')
plt.show()