import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import torch

#通用一元函数
# abs sqrt square exp log log2 log10
# ceil 向上取整， floor 向下取整 sin cos tan
x = np.arange(9).reshape((3,3))
x1 = torch.tensor(x)
sqrtx = np.sqrt(x)
arcsinx = np.arcsinh(x)
sigmoidx = torch.sigmoid(x1)


'''np的广播机制'''

array1 = np.arange(15).reshape((5,3))
array2 = [1,2,3]

array1+array2 #（5，3） * (1,3),列的元素个数相同可以广播，此时 广播成为 （5，3）

array3 = np.arange(15).reshape((3,5))
array4 = np.array([2,2,2]).reshape((3,1))
array3+array4  #水平传播

#np中一些有用的函数  unique：删除重复值
#split/hsplit/vsplit 拆分
#stack/hstack/vstack 堆叠



'''Matrix'''
# matrix 矩阵乘法 使用 @ 符号
#矩阵的一些属性
#A  获取Matrix对应的ndarray对象
#I  获取他的逆矩阵
#T  获取转置矩阵
#shape  size：个数
'''
dot 点积   inner 内积  outer叉积

'''
m = np.matrix([1,2,3])
n = np.matrix([4,5,6]).T
res = m@n
print(res)

