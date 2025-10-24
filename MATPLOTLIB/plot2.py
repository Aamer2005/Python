import matplotlib.pyplot as plt
import numpy as np

numbers = np.array([1,2,3,4,5])
squares = np.square(numbers)

plt.figure(1)
plt.plot(numbers,[1,4,9,16,25],'ro')

plt.title("Square Relation")
plt.xlabel("Numbers")
plt.ylabel("Squares")

plt.grid()

plt.figure(2)
plt.plot(numbers,np.sqrt(numbers),'b--')

plt.title("Square Root Realation")
plt.xlabel("Numbers")
plt.ylabel("Square Root")
plt.grid()

plt.show()