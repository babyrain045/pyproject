import requests
from bs4 import BeautifulSoup

url = "https://movie.douban.com/subject/26588308/comments?start=161&limit=20&sort=new_score&status=P&percent_type="
requrl = requests.Session().get(url)
soup = BeautifulSoup(requrl.text,'lxml')
comments_list = soup.findAll('div',{'class','comment'})
for i in comments_list:
    print(i.p.get_text())

next_page = soup.find('div',{'id':'paginator'}).find('a',{'class','next'})
next_url = next_page.attrs['href']
url_start = url.split('?')[0]
url_ = url_start + next_url
print(url_)
requrl = requests.Session().get(url_)
soup = BeautifulSoup(requrl.text,'lxml')
comments_list = soup.findAll('div',{'class','comment'})
for i in comments_list:
    print(i.p.get_text())
