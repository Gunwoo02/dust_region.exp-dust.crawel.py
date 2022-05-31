import requests
from bs4 import BeautifulSoup
import csv

url= 'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%AF%B8%EC%84%B8%EB%A8%BC%EC%A7%80&oquery=%EB%AF%B8%EC%84%B8%EB%A8%BC%EC%A7%80+%EC%88%98%EC%B9%98+%ED%81%AC%EB%A1%A4%EB%A7%81&tqi=h5nGWwp0J1ZssEm7srNssssss3w-357383'
response = requests.get(url)

html=response.text
soup = BeautifulSoup(html,'html.parser')

dust=soup.find('div',{'class':'tb_scroll'})
dust_region=dust.select('th')

region_list=[]
for i in dust_region :
  region_list.append(i.text)

region_list.remove('관측지점')
region_list.remove('현재')
region_list.remove('오전예보')
region_list.remove('오후예보')
#print(region_list)

dust_figure=dust.select('td')

dust_figure_list=[]
for k in dust_figure :
  dust_figure_list.append(k.text)

N=[]
n=0
for j in range(0,17):
  N.append(n)
  n+=3

figure_list=[]
for h in N :
  figure_list.append(dust_figure_list[h])
#print(figure_list)

for i in range(len(region_list)):
  region=region_list[i]
  figure=figure_list[i] 
  line=f'{region},{int(figure)}'
  print(line)

with open('dust.csv','w') as fp :
  line='region, figure\n'
  fp.write(line)
  for i in range(len(region)):
    region=region_list[i]
    figure=figure_list[i]
    line=f'{region},{int(figure)}\n'
    fp.write(line)
