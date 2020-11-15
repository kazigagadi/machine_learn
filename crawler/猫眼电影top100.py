import requests
import re

# # 代理
# proxies={
#     # "http":"http://ip地址:端口号"
#     "http":"http://116.209.55.227:9999"
# }
#
# response=requests.get("http://httpbin.org/ip",proxies=proxies)
# print(response.text)

def get_html(url):
    proxies={
    # "http":"http://ip地址:端口号"
    "http":"http://36.248.133.15:9999"
    }
    headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20200101 Firefox/66.0'}
    try:
        response=requests.get(url,headers=headers,proxies=proxies)
        if response.status_code==200:
            try:
                return response.content.decode("utf-8")
            except Exception as e:
                return response.content.decode("gbk")
            
        else:
            print("响应状态码错误！")
    except Exception as e:
        print("请求出现错误，错误类型是：s%"%e)

def parse_html(html):
    "<dd>.+</dd>"
    tlist=[]
    pattern = re.compile('<dd>.+?>(\d{1,3})</i>.+?title="(\w+)".+?data-src="(.+?)".+?'
                           'star">\s+主演：(.+?)\s+</p>.+?releasetime">上映时间：(.+?)</p>.+?'
                           'integer">(\d\.)</i>.+?fraction">(\d)</i>.+?</dd>',re.S)
    result=re.findall(pattern,html)
    for line in result:
        tlist.append([line[0],line[1],line[2],line[3].replace(",","、"),line[4],line[5]+line[6]])
    print("*"*50)
    # print(tlist)
    return tlist

def save_to_csv(info_list):
    with open("mayantop100.csv",'a',encoding='utf-8') as f:
        for line in info_list:
            f.write(','.join(line))
            f.write('\n')
    
def main():
    with open("mayantop100.csv",'w',encoding='utf-8') as f:
        f.write('排名,电影名称,图片链接,主演,上映时间,评分\n')
    for i in range(10):
        start_url='https://maoyan.com/board/4?offset={}'.format(i*10)
        html=get_html(start_url)
        info_list=parse_html(html)
        save_to_csv(info_list)
        print("正在写入第%s页信息......"%(i+1))

if __name__ == '__main__':
    main()