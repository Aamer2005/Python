import matplotlib.pyplot as plt
import numpy as np

numbers = np.array([1,2,3,4,5])
squares = np.square(numbers)

plt.plot(numbers,[1,4,9,16,25],'r--',label='Square',linewidth=3)

plt.title("Square Relation")
plt.xlabel("Numbers")
plt.ylabel("Squares")

plt.grid()
plt.legend()

plt.show()