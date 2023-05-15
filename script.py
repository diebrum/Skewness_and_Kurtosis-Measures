import numpy as np
import pandas as pd
import seaborn as sbs
import scipy as scp
import matplotlib.pyplot as plt



data=pd.read_csv('online.csv',delimiter=',')
data.head()



def histogram_plot(data,field):
  return sbs.histplot(data=data,x=i,kde=True,bins=20)

def skewness_func(data,field):
  return scp.stats.skew(data[field])

def kurtosis_func(data,field):
  return scp.stats.kurtosis(data[field]) 
  
 
 
fields=['Marketing_Spend','Administration','Transport','Profit']


 
for i in fields:
  
  hist=histogram_plot(data,i)
  plt.show()  
  
    
for i in fields:
  skew=skewness_func(data,i)
  kurt=kurtosis_func(data,i)
  print("Skewness e Kurtosis de " +i+":",skew,kurt)
  

