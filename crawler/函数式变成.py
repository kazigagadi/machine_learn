import requests
import re

def get_html(url):# 请求网页,获得服务器响应内容
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0'}
    response=requests.get(url,headers=headers)
    return response.content

def parse_html(html):# 解析网页,提取所需信息
    pattern=re.compile(r'src="(https://imgsa.baidu.com/forum/.+?jpg)"')
    url_list=re.findall(pattern,html)
    return url_list

def save_to_picture(content,n):# 图片下载在本地
    path=r'F:\DataAnalysis\python\python基础\exercise_dir\图片{}.jpg'.format(n)
    with open(path,'wb') as f:
        f.write(content)

def main():# 调度整个爬虫
    number=1# 设置命名起始值
    for i in range(6):
        start_url='https://tieba.baidu.com/p/5815297430?pn={}'.format(i+1)# 设置起始url
        html=get_html(start_url).decode("utf-8")# 请求网页获得html信息
        url_list=parse_html(html)# 解析html获得图片url列表
        for url in url_list:# 访问url列表
            pic_content=get_html(url)# 请求图片url获得字节流数据
            save_to_picture(pic_content,number)# 将字节流数据保存在本地
            number+=1# 累计


main()# 调用整个函数