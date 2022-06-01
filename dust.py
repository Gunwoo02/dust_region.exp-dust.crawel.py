#학생1-지역별 미세먼지수치의 비교
import requests
from bs4 import BeautifulSoup

url= 'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%AF%B8%EC%84%B8%EB%A8%BC%EC%A7%80&oquery=%EB%AF%B8%EC%84%B8%EB%A8%BC%EC%A7%80+%EC%88%98%EC%B9%98+%ED%81%AC%EB%A1%A4%EB%A7%81&tqi=h5nGWwp0J1ZssEm7srNssssss3w-357383'
response = requests.get(url)

html=response.text
soup = BeautifulSoup(html,'html.parser')

dust=soup.find('div',{'class':'tb_scroll'})
dust_region=dust.select('th')

region_list=[]
for i in dust_region :
  region_list.append(i.text)
#print(region_list)
  
region_list.remove('관측지점')
region_list.remove('현재')
region_list.remove('오전예보')
region_list.remove('오후예보')
#print(region_list)-미세먼지 지역 크롤링

dust_figure=dust.select('td')

dust_figure_list=[]
for k in dust_figure :
  dust_figure_list.append(k.text)
#print(dust_figure_list)
  
N=[]
n=0
for j in range(0,17):
  N.append(n)
  n+=3
#print(N)
  
figure_list=[]
for h in N :
  figure_list.append(dust_figure_list[h])
#print(figure_list)-미세먼지 수치 크롤링

for i in range(len(region_list)):
  region=region_list[i]
  figure=figure_list[i] 
  line=f'{region},{int(figure)}'
  print(line)

#학생2-입력한 지역의 미세먼지 수치와 정도 파악
dust_morning=dust.select('td')

dust_morning_list=[]
for i in dust_morning :
  dust_morning_list.append(i.text)
#print(dust_morning_list)

M=[]
m=1
for k in range(0,17) :
  M.append(m)
  m+=3
#print(M)

morning_list=[]
for j in M :
  morning_list.append(dust_morning_list[j])
#print(moning_list)-오전상태 크롤링
  
dust_afternoon=dust.select('td')

dust_afternoon_list=[]
for i in dust_afternoon :
  dust_afternoon_list.append(i.text)
#print(dust_afternoon_list)
  
A=[]
a=2
for k in range(0,17) :
  A.append(a)
  a+=3
#print(A)
  
afternoon_list=[]
for j in A :
  afternoon_list.append(dust_afternoon_list[j])
#print(afternoon_list)-우후상태 크롤링
  
name=list(input('지역별 미세먼지 정도 비교 : ').split())
for i in name :
  n=region_list.index(i)
  n=int(n)
  print(f'지역 : {region_list[n]}, 수치 : {figure_list[n]}, 오전예보 : {morning_list[n]}, 오후예보 : {afternoon_list[n]}')
