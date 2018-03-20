#coding:utf8

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data_csv = pd.read_table('trajectory.txt',sep=',')
data_origin = pd.DataFrame(data_csv)
#按照vehicle-id&time&speed&x-xxxx&y-yyyy等字段去重
data_origin.drop_duplicates(['vehicle-id','time','speed','x-coordinate','y-coordinate'])
#去除名为'NAN'的一列
data_origin.pop('NAN')
print("总记录数： \n",len(data_origin))

data_origin['time'] = data_origin['time'] - 1493852410
data_origin['x-coordinate'] = data_origin['x-coordinate'] - 520955
data_origin['y-coordinate'] = data_origin['y-coordinate'] - 53380
# print(data_origin[(data_origin['x-coordinate'] > 450) & (data_origin['x-coordinate'] < 477) & (data_origin['y-coordinate'] > 1368) & (data_origin['y-coordinate'] < 1612)])
# print(data_origin['x-coordinate'])

#载客数据
data_ctg_1 = data_origin[(data_origin['category'] == 1)]
#非载客数据
data_ctg_0 = data_origin[(data_origin['category'] == 0)]

print("载客：\n",data_ctg_1['speed'].describe())
print("记录数：\n",len(data_ctg_1))

print("非载客: \n",data_ctg_0['speed'].describe())
print("记录数: \n",len(data_ctg_0))


# print("x-max,x-min,y-max,y-min",data_origin[['x-coordinate']].max,data_origin[['x-coordinate']].min,data_origin[['y-coordinate']].max,data_origin[['y-coordinate']].min)
# print(data_origin[['time','x-coordinate','y-coordinate']])
# print("x-max,x-min,y-max,y-min\n",int(max(data_origin['x-coordinate'])),int(min(data_origin['x-coordinate'])),int(max(data_origin['y-coordinate'])),int(min(data_origin['y-coordinate'])))

#画图展示
def paint():
    plt.plot(data_origin['x-coordinate'],data_origin['y-coordinate'],'ro')
    plt.xlim(xmax=965,xmin=0)
    plt.ylim(ymax=5335,ymin=0)
    plt.show()

