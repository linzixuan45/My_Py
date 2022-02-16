import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Series 对象的两种索引方式
data =np.arange(5)
index=['一季度','二季度','三季度','四季度','五季度']
s = pd.Series(data,index )
s['一季度'] = 23
s[1] = 12
#print(s)
'''
一季度    23
二季度    12
三季度     2
四季度     3
'''
# 配置支持中文的非衬线字体（默认的字体无法显示中文）
plt.rcParams['font.sans-serif'] = ['SimHei', ]
# 使用指定的中文字体时需要下面的配置来避免负号无法显示
plt.rcParams['axes.unicode_minus'] = False
dict1 = {'一季度': 320, '二季度': 180, '三季度': 300, '四季度': 405}
s2 = pd.Series({'一季度': 320, '二季度': 180, '三季度': 300, '四季度': 405})
s2.plot(kind = 'bar',color = ['r', 'g', 'b' , 'y'])
plt.xticks(rotation = 0)
for i in range(4):
    plt.text(i, s2[i] + 5, s2[i], ha='center')

# 显示图像
plt.show()