#定义一个股票的类
class Stock(object):
    '''stock类中包含属性code和price'''
    def __init__(self,code,name='', price=0):
        self.code=code
        self.price=price
        self.name = name

    # '''stock类中包含属性name和code'''
    # def __init__(self,name,code):
    #     self.name=name
    #     self.code=code
    def get_stock(self):
        return (self.name, self.code)

        # 定义打印属性的函数

    def get_attr(self):
        return (self.__code, self.__price)
    def print_attr(self):
        print(f'股票代码为：{self.code}')
        print(f'股票价格为：{self.price}')