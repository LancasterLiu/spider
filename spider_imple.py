# 静态网页实践
# coding: utf-8

import requests
from bs4 import *
from pandas import *

headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.69",
         'Host': "movie.douban.com"}
movie_dic={}
ALLname=[]
ALLstar=[]
ALLinfo=[]
for i in range(10):
    link="https://movie.douban.com/top250?start="+str(i*25)
    r=requests.get(link,headers=headers,timeout=10)
    print("第",str(i+1),"页状态码：",r.status_code)

	#以html.parser来解析
    soup=BeautifulSoup(r.text,"html.parser")
    div_list=soup.find_all("div",class_="info")
    
    for i in div_list:
        name=i.find("div",class_="hd").a.span.text.strip()
        info=i.find("div",class_="bd").p.text.strip()
        info = info.replace("\n", " ").replace("\xa0", " ")
        info =  ' '.join(info.split())
        star=i.find('span',class_="rating_num").text.strip()
        
        ALLname.append(name)
        ALLstar.append(star)
        ALLinfo.append(info)

#保存至excel文件
movie_dic["name"]=ALLname
movie_dic["info"]=ALLinfo
movie_dic["star"]=ALLstar
df=DataFrame(movie_dic)
df.to_excel("data.xlsx")

# print(movie_dic)

