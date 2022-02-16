# 面向对象相关知识
# 三大支柱：封装、继承、多态
# 例子：工资结算系统。


# 月薪结算系统 - 部门经理每月15000 程序员每小时200 销售员1800底薪加销售额5%提成
from abc import ABCMeta, abstractmethod
# ABCMeta :元类就是用来创建这些类（对象）的类，元类就是类的类
# type就是所有类的元类，可以理解为所有的类都是由type创建的
# 我们也可以创建自己的元类，这个类需要继承自type

class Employee(object,metaclass=ABCMeta):
    def __init__(self,name,salary=0):
        self.name = name
        self.salary = salary

    @abstractmethod
    def get_salary(self):
        pass

class Manager(Employee):
    def get_salary(self):
        self.salary =15000

class Programmer(Employee):
    def __init__(self,name,salary,working_hour=0,):
        self.working_hour = working_hour
        super().__init__(name,salary)

    def get_salary(self):
        self.salary = 200*self.working_hour

class Salesman(Employee):
    def __init__(self,name,sales = 0,salary=0):
        self.sales = sales
        super().__init__(name, salary)

    def get_salary(self):
        self.salary = self.sales * 0.05 +1800


class   EmployeeFactory:
    """创建员工的工厂（工厂模式 - 通过工厂实现对象使用者和对象之间的解耦合）"""
    #staticmethod 可以不用实例化就调用函数
    @staticmethod
    def creat(emp_type,*args,**kwargs):  # *args表示任何多个无名参数，它是一个tuple；**kwargs表示关键字参数，它是一个dict
        all_emp_type = {'M':Manager,'S':Salesman,'P':Programmer}
        cls = all_emp_type[emp_type.upper()]
        return cls(*args,**kwargs)  # 此时相当于调用了函数并返回了函数的值

def main():
    employees = [
        EmployeeFactory.creat('M','曹操'),
        EmployeeFactory.creat('P','子轩',salary=0,working_hour = 200),
        EmployeeFactory.creat('S','何丽',sales = 200000,salary = 0)
    ]
    for emp in employees:
        emp.get_salary()
        print(f'{emp.name}:{emp.salary}元')


if __name__ == '__main__':
    main()