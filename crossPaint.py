#coding:utf8

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data_csv = pd.read_table('trajectory.txt',sep=',')
data_origin = pd.DataFrame(data_csv)

data_origin['time'] = data_origin['time'] - 1493852410
data_origin['x-coordinate'] = data_origin['x-coordinate'] - 520955
data_origin['y-coordinate'] = data_origin['y-coordinate'] - 53380
#截取某一路口区域
#x_min,x_max,y_min,y_max = (450,477,1368,1612)
print(data_origin[(data_origin['x-coordinate'] > 450) & (data_origin['x-coordinate'] < 477) & (data_origin['y-coordinate'] > 1368) & (data_origin['y-coordinate'] < 1612)])
# print(data_origin['x-coordinate'])

# print("x-max,x-min,y-max,y-min",data_origin[['x-coordinate']].max,data_origin[['x-coordinate']].min,data_origin[['y-coordinate']].max,data_origin[['y-coordinate']].min)
# print(data_origin[['time','x-coordinate','y-coordinate']])
# print("x-max,x-min,y-max,y-min\n",int(max(data_origin['x-coordinate'])),int(min(data_origin['x-coordinate'])),int(max(data_origin['y-coordinate'])),int(min(data_origin['y-coordinate'])))

#画图展示
def paint():
    plt.plot(data_origin['x-coordinate'],data_origin['y-coordinate'],'ro')
    plt.xlim(xmax=965,xmin=0)
    plt.ylim(ymax=5335,ymin=0)
    plt.show()

