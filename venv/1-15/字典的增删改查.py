# 字典的创建
a1 = '123456'
b1 = 'abcdef'
dict1 = dict(zip(a1,b1 ))
print(dict1)
# 字典的构造器语法
dict2 = dict(one = 1 ,two=2,three=3)
print(dict2)
# 字典的推导式语法
dict3 = {num: num for num in a1}
print(dict3)

# 字典的遍历
for key in dict1:
    print(key, dict1[key])


# 字典的遍历 -》键值对 dict.items()   dict.values()  dict.keys()
for key , val in dict2.items():
    print(key ,val)


# 字典的增加 ，第一种给定键值对 item ，第二种upgrad,合并字典
dict1['7'] = 'h'
print(dict1)
# 何丽是猪猪猪
dict1.update(dict2)
print(dict1)


# 字典的删除
dict1.popitem()  # 删除最后一个元素
dict1.pop('1')  # 删除指定的key 对应的键值对
print(dict1)


# 字典的值查找   查所有key ，values
print(dict1.keys())
print(dict1.values())
print(dict(sorted(dict1.items(),reverse=True)))