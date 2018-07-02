import urllib.request
import  re
import numpy as np
import pandas as pd
import matplotlib.pylab as plt
import matplotlib
import math
'''CollectionUrl = "http://www.forbeschina.com/review/list/002265.shtml"
data = urllib.request.urlopen(CollectionUrl).read().decode('utf-8','ignore')
pat='154px">(.*?)</td'
rs=re.compile(pat).findall(data)
file = open('/Users/yiliu/lllyeeData/ForbesRe', 'w')
file.write(str(rs))
print("finish")
file.close()'''

file=open('/Users/yiliu/lllyeeData/ForbesRe', 'r')
data=file.readline()
data=eval(data)
d=np.array(data).reshape((2001,5))
result=pd.DataFrame(d,columns=['排名','公司','地区','销售额','利润(亿美元)'])
result.to_csv('/Users/yiliu/lllyeeData/rank.csv',header=True, index=False, encoding='utf_8_sig')
#print(result['排名'])
#x=result['利润(亿美元)']
#y=result['销售额']


'''
ply.figure(1,dpi=50) #dpi指定分辨率
plt.subplot(223)#创建2*2的图表，绘制的子图为矩阵中的序号3
plt.subplot(221)
plt.plot(x,np.sin(x))#曲线图
plt.sca(x1)#选择子图x1
data=[1,1,1,2,2,2,3,3,4,5,5,6,4]
plt.hist(data)#直方图，只要传入数据，直方图就会统计数据出现的次数
#产生测试数据  
x = np.arange(1,10)  
y = x  
fig = plt.figure()
plt.scatter(x,y,c = 'r',marker = 'o')  #c = 'r'表示散点的颜色为红色，marker 表示指定三点多形状为圆形


'''
#利润和销售的点图
plt.figure()#创建图表
x=result['销售额']
y=result['利润(亿美元)']
x=x.astype(float)
y=y.astype(float)
print(x.max())
plt.scatter(x,y,s=5,marker=".",c='g')
plt.xlabel('sale')
plt.ylabel('profit')
plt.xticks(np.linspace(x.min(),x.max(),10))
plt.yticks(np.linspace(y.min(),y.max(),10))
plt.show()#显示图表

