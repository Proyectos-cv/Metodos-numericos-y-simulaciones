import numpy as np
A = np.array([[6, 15, 55], [15, 55, 225], [55, 225, 979]])
B = np.array([152.6, 585.6, 2488.8])
X = np.linalg.inv(A).dot(B)

print(X)