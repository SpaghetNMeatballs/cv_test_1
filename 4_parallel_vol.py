import numpy as np

a = np.array([float(i) for i in input().split()])
b = np.array([float(i) for i in input().split()])
c = np.array([float(i) for i in input().split()])
print(np.linalg.det([a, b, c]))
