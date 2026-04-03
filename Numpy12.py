import numpy as np

sample_array_1 = np.array([0, 4, 2])
sample_array_2 = np.array([1])

combined = np.concatenate((sample_array_1, sample_array_2))
print(combined)