import requests
import os
import time
import html2text
import sys
import traceback
from bs4 import BeautifulSoup as bs
import re

def patch_fix_image_links(text):
    # 正则表达式来匹配Markdown中的图片链接
    img_pattern = r'!\[[^\]]*\]\([^)]*\)'

    # 找到所有的图片链接
    img_links = re.findall(img_pattern, text)

    # 遍历图片链接并修复其中的换行符
    for img_link in img_links:
        fixed_img_link = img_link.replace('\n', '')
        text = text.replace(img_link, fixed_img_link)

    return text

starttime = time.time()
url1 = 'https://i.news.qq.com/trpc.qqnews_web.kv_srv.kv_srv_http_proxy/list?sub_srv_id=24hours&srv_id=pc&offset=0&limit=190&strategy=1&ext={"pool":["top","hot"],"is_filter":7,"check_type":true}'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}
qq1 = requests.get(headers=headers, url=url1).json()
datalist = []
for i in qq1["data"]["list"]:
    tmptitle = i["title"]
    tmpurl = i["url"]
    if time.strftime("%Y%m%d") not in tmpurl:
        print(f"EXPIRED\n{tmptitle}\n{tmpurl}\n\n")
        continue
    datalist.append(tuple([tmptitle, tmpurl]))

tmphtml = ""
tmpbs = ""
if not os.path.exists(f"{sys.path[0]}/{time.strftime('%Y-%m-%d')}"):
    os.makedirs(f"{sys.path[0]}/{time.strftime('%Y-%m-%d')}")
for i in datalist:
    time.sleep(1)
    try:
        tmphtml = requests.get(i[1]).text
        tmpbs = bs(tmphtml, "html.parser")
        ss = str(tmpbs.select("div.LEFT div.content.clearfix")[0])
        ss = ss.replace("//inews.gtimg.com", "https://inews.gtimg.com").replace("</img>", "</img><br/>")
        ss = html2text.html2text(ss)
        if len(ss.split()) <= 3:
            print(f"INVALID\n{i[0]}\n{i[1]}\n\n")
            continue
        if os.path.exists(f"{sys.path[0]}/{time.strftime('%Y-%m-%d')}/{i[0]}.md"):
            print(f"EXIST\n{i[0]}\n{i[1]}\n\n")
            continue
        # 修复Markdown文件中的图像链接和换行符
        ss = patch_fix_image_links(ss)
        with open(f"{sys.path[0]}/{time.strftime('%Y-%m-%d')}/{i[0]}.md", "w", encoding="utf-8") as x:
            x.write(ss)
        print(f"SUCCESS\n{i[0]}\n{i[1]}\n\n")

    except Exception as e:
        print(f"ERROR\n{i[0]}\n{i[1]}\n{e.args}\n======\n{traceback.format_exc()}\n")
