class StockCode:
    def __init__(self,stock,code):
        self.stock=stock
        self.code=code
    @classmethod
    # 装饰器，立马执行下面的函数
    def split(cls,sc):
        # cls是默认的这个类的init函数，sc是传入参数
        stock,code=map(str,sc.split('-'))
        # 这里转换成了格式化的结构
        dd = cls(stock,code)
        # 然后执行这个类第一个方法
        return dd