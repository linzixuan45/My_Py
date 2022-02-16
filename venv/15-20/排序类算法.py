
ls = [3,2,4,5,1,6,7,12,45,25,656,123,453]
#简单选择排序
def simple_choice(ls1):
    ls = ls1[:]
    size = len(ls)
    for i in range(0,len(ls)-1):
        min = ls[i]
        min_index = i
        for j in range(i,len(ls)-1):
            min,min_index= (ls[j],j) if min>ls[j] else (min,min_index)

        ls[i] ,ls[min_index] = ls[min_index],ls[i]

    return ls


#冒泡排序
def bubble_sortbub(ls1):
    ls = ls1[:]
    max = ls[0]
    for i in range(0, len(ls)-1):
        m = len(ls)-1
        for j in range(0,m):
            ls[j],ls[j+1] = (ls[j+1],ls[j]) if ls[j] >ls[j+1] else (ls[j],ls[j+1])



#回溯法