import math

x_min = math.sqrt(2019**2 - 1867**2)
x_max = math.sqrt(1867**2 + 2019**2)

print(x_min, x_max)

n_x = math.floor(x_max)- math.ceil(x_min) + 1
print(n_x)
