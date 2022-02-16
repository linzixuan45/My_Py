# from random import randint
# from threading import Thread
# from time import time, sleep
# #   调用Thread类
# # This constructor should always be called with keyword arguments.  init（）
#
# class DownloadTask(Thread):
#
#     def __init__(self, filename):
#         super().__init__()  # 此句必须调用，完成线程的初始化操作
#         self._filename = filename
#
#     '''    def __init__(self, group=None, target=None, name=None,
#                      args=(), kwargs=None, *, daemon=None):'''
#
#     def run(self):
#         print('开始下载%s...' % self._filename)
#         time_to_download = randint(5, 10)
#         sleep(time_to_download)
#         print('%s下载完成! 耗费了%d秒' % (self._filename, time_to_download))
#
#
# def main():
#     start = time()
#     t1 = DownloadTask('Python从入门到住院.pdf')
#     t1.start()
#     t2 = DownloadTask('Peking Hot.avi')
#     t2.start()
#     t1.join()
#     t2.join()
#     end = time()
#     print('总共耗费了%.2f秒.' % (end - start))
#
#
# if __name__ == '__main__':
#     main()
# from time import sleep
# from threading import Thread
#
# # class Account ：
# class Account(object):
#     # python3中自带了object类，也就是自带了很多对象
#     # python2中 不带则class只有三种类型的对象，只拥有了__doc__ , __module__ 和 自己定义的变量
#
#     def __init__(self):
#         self._balance = 0
#
#     def deposit(self, money):
#         # 计算存款后的余额
#         new_balance = self._balance + money
#         # 模拟受理存款业务需要0.01秒的时间
#         sleep(0.01)
#         # 修改账户余额
#         self._balance = new_balance
#
# # 通过 @property 装饰器，可以直接通过方法名来访问方法，不需要在方法名后添加一对“（）”小括号
#     @property
#     def balance(self):
#         return self._balance
#
#
# class AddMoneyThread(Thread):
#
#     def __init__(self, account, money):
#         super().__init__()
#         self._account = account
#         self._money = money
#
#     def run(self):
#         self._account.deposit(self._money)
#
#
# def main():
#     account = Account()
#     threads = []
#     # 创建100个存款的线程向同一个账户中存钱
#     for _ in range(100):
#         t = AddMoneyThread(account, 1)
#         threads.append(t)
#         t.start()
#     # 等所有存款的线程都执行完毕
#     for t in threads:
#         t.join()
#     print('账户余额为: ￥%d元' % account.balance)
#
#
# if __name__ == '__main__':
    #main()

from time import sleep
from threading import Thread, Lock


class Account(object):

    def __init__(self):
        self._balance = 0
        self._lock = Lock()

    def deposit(self, money):
        # 先获取锁才能执行后续的代码
        self._lock.acquire()
        try:
            new_balance = self._balance + money
            sleep(0.01)
            self._balance = new_balance
        finally:
            # 在finally中执行释放锁的操作保证正常异常锁都能释放
            self._lock.release()

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def c_balance(self, value):
        self._balance = value


class AddMoneyThread(Thread):

    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self):
        self._account.deposit(self._money)


def main():
    account = Account()
    threads = []

    print(account.balance)
    for _ in range(100):
        t = AddMoneyThread(account, 1)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print('账户余额为: ￥%d元' % account.balance)
    account.c_balance
    print(account.balance)


if __name__ == '__main__':
    main()