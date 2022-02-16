import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random


#生成器和迭代器
dict_list = {}
list0 = [x for x in range(5) if x]
list1 = [x for x in range(5,10)]
list2 = [x for x in range(10,15)]
list3 = [x for x in range(15,20)]

#创建numpy的对象  array ，random.normal ,random.rand ,random.randint , arang
np_dict = {}
np_dict[0] = np.array((list0,list1,list2,list3))
np_dict[1] = np.random.normal(0,2,10)

#创建指定形态的数组 np.zeros np.ones np.eye np.full() .reshape(-1)

np_dict[2] = np.zeros((3,3))
np_dict[3] = np.ones((3,3))
np_dict[4] = np.full((3,3),2)
np_dict[5] = np.eye(3,3)
np_dict[6] = np.eye(3, 3).reshape(-1)

#np矩阵的拼接  水平 hstack   垂直 vstack np类型的切片操作与列表不同，他是引用类型
#【开始，结束，步长】  左右开
# 高维数据的切片应当理解为 *arg ，传入元素，一层层剥离 ，一层层调整，猜测是基于迭代器的操作
np_array1 = np.array(([1,1,1,1,1],[2,2,2,2,2],[3,3,3,3,3],[4,4,4,4,4],[5,5,5,5,5]))
np_array2 = np.arange(16).reshape((4,4))
npslice = {}
npslice[0] = np_array1[::-1][:] #行倒置

npslice[1] = np.hstack((np_array1,np.array([6,6,6,6,6]).reshape((5,1))))
npslice[2] = np_array2[::-1][:] #实际上只是执行了np_array2[::-1],都是对于 最外围迭代器的操作
npslice[3] = np_array2[:][:2] #实际上只是执行了np_array2[:2]，都是对于最外围迭代器的操作
npslice[4] = np_array2[:,::-1]# 每个元素内部自行逆排

'''创建 Bool类型'''
npslice[5] = np_array2 > 1
a = np.arange(10).reshape((2,5))




'''array 的统计运算'''
#summary 求和  mean 求均方  std standard deviation 标准差  variation 方差 累计和 cumulation summary
