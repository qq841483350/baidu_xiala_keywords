#coding:utf8
#百度下拉关键词挖掘
import requests,re,MySQLdb,socket
# conn=MySQLdb.connect(host='localhost',user='root',passwd='',db='seo_keyword',port=3306,charset='utf8')
# cursor=conn.cursor()
# cursor.execute("SET NAMES utf8")
socket.setdefaulttimeout(30)
requests.packages.urllib3.disable_warnings()
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0"}
def get_html(word):
    url='https://sp0.baidu.com/5a1Fazu8AA54nxGko9WTAnF6hhy/su?wd=%s'%word

    r=requests.get(url,verify=False)
    # print url
    # r=requests.get(url)
    r.encoding='gb2312'
    html=r.text
    return html

def get_xiala(word):
    html=get_html(word)
    keywords=re.findall('s:\[([\s\S]*?)\]\}\);',html)[0]
    if keywords:
        keyword=re.findall('"([\s\S]*?)"',keywords)
        num=len(keyword)
        for x in range(0,num):
            baidu_word=keyword[x]
            if word in baidu_word:
                print baidu_word        #打印抓取到的下拉词
                # try:
                #     cursor.execute("insert into baidu_xiala_word(word) VALUES ('%s')"%baidu_word)
                #     conn.commit()
                #     get_xiala(baidu_word)
                #
                # except:
                #     continue
            else:
                pass

    else:
        pass

if __name__=="__main__":
    print '百度下拉关键词收集   开发者：李亚涛  微信：841483350'
    word=raw_input('inter the word:')
    get_xiala(word)
    # words=open('words.txt','r').readlines()    #如果杨一次性抓取非常多的关键词，取消注释，然后把你要查询的关键词放到命名为words的文件里，每1行只能有1个关键词
    # for word in words:
    #     word=word.strip('\n')
    #     print word
    #
    # try:
    #     cursor.execute("insert into baidu_xiala_word(word) VALUES ('%s')"%word)
    #     conn.commit()
    #     get_xiala(word)
    # except:
    #     print  '关键词',word, '已经抓取过了'




