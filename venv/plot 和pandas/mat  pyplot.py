import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import torch

#Matplotlib 默认情况不支持中文
# 需要加字体关键词 fontproperties = setFont

SetFont = matplotlib.font_manager.FontProperties(fname = "SourceHanSansSC-Bold.otf")

x = np.arange(-5,5,1)
x = torch.from_numpy(x)
y = torch.sigmoid(x)
y2 = torch.relu(x)
plt.subplot(1,2,1)
plt.plot(x,y,marker = 'o')

plt.subplot(1,2,2)
plt.plot(x,y2,marker = 'o')
plt.xlabel('axis = x 中文',fontproperties = SetFont)
plt.ylabel('axis = y 轴对称',fontproperties=SetFont)
plt.title('sigmoid & relu')
#图片增加网格线
plt.grid()

#绘制多图 subplot

plt.show()