import matplotlib.pyplot as plt
import numpy as np
numbers = [1,2,3,4,5]

#
#subplot(row,coloum,placing)
#placing : placing the plot in row sequence -->

plt.figure(1)
plt.subplot(2,2,1)
plt.plot(numbers,np.square(numbers),color='blue',linestyle='--',label='Square')
plt.grid()
plt.legend()

plt.subplot(2,2,2)
plt.plot(numbers,np.sqrt(numbers),color='red',linestyle='-',label='SQRT')
plt.grid()
plt.legend()

plt.subplot(2,2,3)
plt.plot(numbers,np.exp(numbers),color='red',linestyle=':',label='EXP')
plt.grid()
plt.legend()

plt.subplot(2,2,4)
plt.plot(numbers,np.abs(numbers),color='red',linestyle='dashed',label='abs')
plt.grid()
plt.legend()

plt.show()