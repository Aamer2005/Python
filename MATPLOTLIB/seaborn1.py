import seaborn as sns
import pandas as pd 
import matplotlib.pyplot as plt

var = sns.load_dataset('penguins')

sns.lineplot(x = 'bill_length_mm',y='bill_depth_mm',data=var,hue = 'sex',style='sex',palette = 'Accent',markers=['o','>'])

# sns.lineplot(x = 'bill_length_mm',y='bill_depth_mm',data=var,hue = 'sex',style='sex',palette = 'Accent')
# sns.lineplot(x = 'bill_length_mm',y='bill_depth_mm',data=var,hue = 'sex')
# sns.lineplot(x = 'bill_length_mm',y='bill_depth_mm',data=var)


plt.show()