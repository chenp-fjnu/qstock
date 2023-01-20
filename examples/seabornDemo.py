import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
# windows用户可使用下方的中文显示方法
# #plt.rcParams['font.sans-serif'] = ['SimHei']
# #plt.rcParams['axes.unicode_minus']=False
def sinplot(flip=1):
    x = np.linspace(0, 14, 100)
    for i in range(1, 7):
        # 随便设计的y函数
        plt.plot(x, np.sin(x + i * 0.5) * x)

plt.figure ( figsize =( 12 , 8 ))

sns.set_style ( 'darkgrid' )
plt.subplot ( 221 ) #在两行两列的画布中位于第一个位置（左上角）
sinplot ()

sns.set_style ( 'whitegrid' )
plt.subplot ( 222 )#在两行两列的画布中位于第 2 个位置（右上角）
sinplot ()

sns.set_style ( 'dark' )
plt.subplot ( 223 )#在两行两列的画布中位于第 3 个位置（左下角）
sinplot ()

sns.set_style ( 'ticks' )
plt.subplot ( 224 )#在两行两列的画布中位于第 4 个位置（右下角）
sinplot()
plt.show()