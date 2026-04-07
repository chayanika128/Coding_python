import numpy as np
arr=np.array([20,35,25,30])
target=26
closest=arr[np.abs(arr-target).argmin()]
print(closest)
