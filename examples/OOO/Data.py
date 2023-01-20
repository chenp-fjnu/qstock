import tushare as ts
import pandas as pd
import qstock as qs
from sqlalchemy import create_engine
class Data(object):
    def __init__(self,
                 start='20230101',
                 end='20230120',
                 table_name='daily_data'):
        self.pro = ts.pro_api('a03cdee7026cbae830bbbb9b618b5b5d9fc99d525dee2aaf1969d36b')
        self.start=start
        self.end=end
        self.table_name=table_name
        self.codes=self.get_code()
        self.cals=self.get_cals()
        # 使用python3自带的sqlite数据库
        self.engine = create_engine('sqlite:///D:\workspace\AI\Quant\qstock\examples\OOO\data\stock_data.db')
    #获取股票代码列表
    def get_code(self):
        codes = self.pro.stock_basic(list_status='L').ts_code.values
        return codes
    #获取股票交易日历
    def get_cals(self):
        #获取交易日历
        cals=self.pro.trade_cal(exchange='')
        cals=cals[cals.is_open==1].cal_date.values
        return cals
    #每日行情数据
    def daily_data(self,code):
        try:
            df0=self.pro.daily(ts_code=code,start_date=self.start,
                end_date=self.end)
            df1=self.pro.adj_factor(ts_code=code,trade_date='')
            #复权因子
            df=pd.merge(df0,df1)  #合并数据
        except Exception as e:
            print(code)
            print(e)
        return df
    #保存数据到数据库
    def save_sql(self):
        for code in self.codes:
            data=self.daily_data(code)
            data.to_sql(self.table_name,self.engine,
                 index=False,if_exists='append')

    def saveToDB(self, dataToStore,tb_name):
            dataToStore.to_sql(tb_name, self.engine,
                        index=False, if_exists='append')
    def getFromDB(self, dataFromDB,tb_name):
        dataFromDB.read_query(tb_name, self.engine)
    #获取最新交易日期
    def get_trade_date(self):
        #获取当天日期时间
        pass
    #更新数据库数据
    def update_sql(self):
        pass #代码省略
    #查询数据库信息
    def info_sql(self):
        pass #代码省略