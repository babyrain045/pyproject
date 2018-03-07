
import requests
import urllib
from bs4 import BeautifulSoup
import os
import re

cookie = '''ELEARNING_00999=q1rjjc0ygcjbsda5datgbw5n; ELEARNING_00008=554c0523-0557-429c-b6af-c2b8f340786a; TY_SESSION_ID=65fd2ee6-0e70-4c49-8083-2ee5904de17c; ELEARNING_00003=StudyMenuGroup; ELEARNING_00006=FF007DE5E502B901771C10A59D7EE65BA797411997FE1B6BCE37A54CBCBE93DACCBC312B4FF7F2618AEC24D08D775C19E7D11BC0D21AC67447B6B66A146150C89B1F72F97B5881D2AF646C489B9E67C38FF4C41AFBE2393DCEB77CE49AC53D21EC7F21141946F35D1E3E07FED45992EAB8B7982B499B638C0117F8482737E9E31C32676C23976729027A8232063670A46CB27BC75A513646840AD7E2EF17123DFB93627E8320521A28BC153F54E3D01F2813C3568575177CCB38474B; ELEARNING_00016=18639980230; loginType=SMS; route=9237bd081bcb7ba1feb437a77addefe6; ELEARNING_00018=6Onr9az/yTIHCK924PAlX4IcluuUXgxUrhHi/uh46sjM5D6UfwMd6OU3WYsRisO8eBmYBilgUEUvssZfphpgbT53aizMinRnj5foKvZLb8joxlqjkuwckxLSx7WhigY7vui7Ooz0pVJKoHhphgB/dvz7cPiOt09TEBR7ew+BS3fE4iyNdbtMYZvoKr4HGd/XIeuxnfAwYRnitg2Ul9YDSw==; El_72949cd1-38ab-41d7-a9cd-065da30d4c47=72949cd1-38ab-41d7-a9cd-065da30d4c47; .ASPXAUTH=6CD50692DBFBF18EF3312AB6AE04B1E3A9797372065D452AA4DA53C40198DD85CA6241B3494AFD647C21D9A92B191B3A5E10919ADDAA1A2E435B9E6AC9BB7C981FC172 0BC441B5D73C7E28E3A0395B12E7EB7C73E1E4F8E58B82EAB93D85B7589DF449B983D0552427E14B021C7FE83DE09C8ED5E3F6948E0116563E538B1691A5FA364DF6C4E65F19B27C6D'''

header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
          'Connection':'keep-alive',
          'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
          'Cookie':cookie}

url = 'http://wydx.yunxuetang.cn/package/document/e011a1ae62d64bff8ea8663b9f2a67b0_ebe6719cd2a4493f805272d67d89b05f.html?uniqueid=1520235703898'

wbdata = requests.get(url,headers=header).text



searchresult = re.findall("https://gjnkw6amjgits2kc304.exp.bcedocument.com/target/[a-zA-Z0-9\-\/\.\?\=]*",wbdata)
print(searchresult)
imgName = 0

for i in searchresult:

    f = open("D://jpgs19/"+ str(imgName)+".jpg",'wb')
    f.write((urllib.request.urlopen(i)).read())
    print(i)
    f.close()

    imgName += 1
print("mission complete!")
