import matplotlib.pyplot as plt
import numpy as np

np.random.seed(1)
data = np.random.randn(100)
print(data)

plt.boxplot(data)
plt.show()