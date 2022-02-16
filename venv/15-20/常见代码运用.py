# #生成式（推导式）的用法
#
# prices = {
#     'AAPL': 191.88,
#     'GOOG': 1186.96,
#     'IBM': 149.24,
#     'ORCL': 48.44,
#     'ACN': 166.89,
#     'FB': 208.09,
#     'SYMC': 21.29
# }
# # 用股票价格大于100元的股票构造一个新的字典
#
# #用推导式建立一个字典
# prices2 = {key : value for key,value in prices.items() if value>100}
# prices4 = [value for value in prices.values() if value > 100]
# print(prices4)
# prices3 = prices
# #用常规for循环建立一个字典
# ls3 = list(prices3.items())
#
#
#
# for Y in list(prices3.items()):#  ('AAPL', 191.88), ('GOOG', 1186.96), ('IBM', 149.24), ('ORCL', 48.44)
# #此处必须设置为list，dictionary changed size during iteration
# #就是说在遍历的时候，字典改变了大小，有两种方法可以解决.
#     if Y[1]<=100 :
#         prices3.pop(Y[0])
# print(prices2)
# print(prices3)
"""
贪婪法：在对问题求解时，总是做出在当前看来是最好的选择，不追求最优解，快速找到满意解。
输入：
20 6
电脑 200 20
收音机 20 4
钟 175 10
花瓶 50 2
书 10 1
油画 90 9
"""
class Thing(object):
    """物品"""

    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    @property
    def value(self):
        """价格重量比"""
        return self.price / self.weight


def input_thing():
    """输入物品信息"""
    name_str, price_str, weight_str = input().split()
    return name_str, int(price_str), int(weight_str)


def main():
    """主函数"""
    """
    map(func, *iterables) --> map object

    Make an iterator that computes the function using arguments from
    each of the iterables.  Stops when the shortest iterable is exhausted.
    """
    max_weight, num_of_things = map(int, input().split())
    #  map(function, iterable, ...)
    all_things = []
    for _ in range(num_of_things):
        all_things.append(Thing(*input_thing()))
        all_things.sort(key=lambda x: x.value, reverse=True)
        total_weight = 0
        total_price = 0
        for thing in all_things:
            if total_weight + thing.weight <= max_weight:
                print(f'小偷拿走了{thing.name}')
                total_weight += thing.weight
                total_price += thing.price
    print(f'总价值: {total_price}美元')


if __name__ == '__main__':
    main()