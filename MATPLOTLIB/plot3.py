import matplotlib.pyplot as mplt
import numpy as np

mplt.plot([1,2,3,4,5], np.square([1,2,3,4,5]), color='b', linestyle='-', marker='o', label='Square')
mplt.plot([1,2,3,4,5],np.sqrt([1,2,3,4,5]),'r--',label="square-root")
mplt.scatter([1,2,3,4,5],[1,2,3,4,5] , color='r', marker='^', s=100,label='number')

mplt.grid()
mplt.legend()

mplt.show()