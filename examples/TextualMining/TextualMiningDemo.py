import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
#画图正常显示中文
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']
# 用来正常显示中文标签
mpl.rcParams['axes.unicode_minus']=False
# 用来正常显示负号

file= '倚天屠龙记.txt'
with open(file,encoding='utf-8') as f:
        data = f.read()

Actress=['赵敏','周芷若','小昭','蛛儿',
         '朱九真','杨不悔']
for name in Actress:
    print("%s"% name,data.count(name))



actress_data = {'赵敏':1240,'周芷若': 819,
                '小昭': 352,'蛛儿': 231,
                '朱九真': 141,'杨不悔': 190}
for a, b in actress_data.items():
    plt.text(a, b + 0.05, '%.0f' % b,
    ha='center', va='bottom', fontsize=12)
    #ha 文字指定在柱体中间，
    #va指定文字位置
    #fontsize指定文字体大小
# 设置X轴Y轴数据，两者都可以是list或者tuple
x_axis = tuple(actress_data.keys())
y_axis = tuple(actress_data.values())
plt.bar(x_axis, y_axis, color='magenta')
# 如果不指定color，所有的柱体都会是一个颜色
#b: blue g: green r: red c: cyan
#m: magenta y: yellow k: black w: white
plt.xlabel("女角名")  # 指定x轴描述信息
plt.ylabel("小说中出现次数")  # 指定y轴描述信息
plt.title("谁是女主角？")  # 指定图表描述信息
plt.ylim(0, 1400)  # 指定Y轴的高度

#继续挖掘下倚天屠龙记里面人物出现次数排名
# namelist=[name.strip() for name in
#           novel_names['倚天屠龙记']]
namelist=''.join(Actress)
namelist=namelist.split('、')
count = []
num=10 #统计前10名

for name in namelist:
    count.append([name, data.count(name)])
count.sort(key=lambda x: x[1])
_, ax = plt.subplots()
numbers = [x[1] for x in count[-num:]]
names = [x[0] for x in count[-num:]]
ax.barh(range(num), numbers, align='center')
ax.set_title('倚天屠龙记', fontsize=14)
ax.set_yticks(range(len(names)))
ax.set_yticklabels(names, fontsize=10)
plt.show()