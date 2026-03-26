
import matplotlib.pyplot as plt
import numpy as np
overs=np.arange(1,21)
scores=[2,3,5,7,9,12,43,26,3,4,5,8,9,5,23,12,8,3,12,3]
plt.bar(overs,scores,color="blue")
plt.title("india score")
plt.xlabel("overs 1-20")
plt.ylabel("scores")
plt.xticks(overs)
plt.grid(axis='x',linestyle="--")
plt.show()
