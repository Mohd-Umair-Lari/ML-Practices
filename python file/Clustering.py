import numpy as np
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster
import matplotlib.pyplot as plt

data = np.array([
    [1, 1],
    [2, 1],
    [3, 4],
    [5, 7],
    [3, 3]
])

methods = ["single", "complete", "average", "centroid", "ward"]

plt.figure(figsize=(12, 8))

for i, method in enumerate(methods, 1):
    Z = linkage(data, method=method)
    plt.subplot(2, 3, i)
    dendrogram(Z, labels=[f"P{i}" for i in range(1, 6)])
    plt.title(f"{method.capitalize()} linkage")

plt.tight_layout()
plt.show()
