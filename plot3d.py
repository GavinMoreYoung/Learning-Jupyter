# import tools we are using
import pandas as pd
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
# read in the car ‘table’ – not a csv, so we need
# to add in the column names
column_names = ['mpg', 'cylinders', 'displacement', 'horsepower','weight', 'acceleration', 'year', 'origin', 'name']
df = pd.read_table('http://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data', sep=r"\s+", index_col=0, header=None,names = column_names)
print(df.head())
#start out plotting (uses a subplot as that can be 3d)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')# pull out the 3 columns that we want
xs = []
ys = []
zs = []
for index, row in df.iterrows():
    xs.append(row['weight'])
    ys.append(index) #read_table uses first column as index
    zs.append(row['cylinders'])# based on our dataset the extents of the axes
plt.xlim(min(xs), max(xs))
plt.ylim(min(ys), max(ys))
ax.set_zlim(min(zs), max(zs))
# standard scatter diagram (except it is 3d)
ax.scatter(xs, ys, zs)
ax.set_xlabel('Weight')
ax.set_ylabel('MPG')
ax.set_zlabel('Cylinders')
plt.show()