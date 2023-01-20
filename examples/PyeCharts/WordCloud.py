#使用tushare获取新闻数据
import tushare as ts
import jieba
import jieba.analyse
import re
token='a03cdee7026cbae830bbbb9b618b5b5d9fc99d525dee2aaf1969d36b'
pro=ts.pro_api(token)
df=pro.news(src='sina', start_date='2022-03-27 09:00:00', end_date='2022-03-27 18:50:00')
df.to_csv('WordCloud.csv')
#df=pd.read_csv('20220327news.csv',index_col=0)
stopwords = [i.strip() for i in open('WordCloud.csv').readlines()]

def cut_word(sentence):
    text = jieba.lcut(''.join(re.findall('[\u4e00-\u9fa5]', sentence)), cut_all = False)
    for i in range(len(text)-1, -1, -1):
        if text[i] in stopwords:
            del text[i]
    return text

news_list = list(df.content.values)
word_list = [" ".join(cut_word(sentence)) for sentence in news_list]
new_text = ' '.join(word_list)
tags=jieba.analyse.extract_tags(new_text,topK=200,withWeight=True)
tf=dict((a[0],a[1]) for a in tags)
data=[[k,v] for k,v in tf.items()]

c = (WordCloud()
    .add(series_name="热点分析", data_pair=data, word_size_range=[6, 66])
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="热点分析", title_textstyle_opts=opts.TextStyleOpts(font_size=23)),
        tooltip_opts=opts.TooltipOpts(is_show=True),))

c.width = "100%"

c.render("WordCloud.html")
