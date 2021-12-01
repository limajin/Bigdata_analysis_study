# 네이버 영화리뷰 크롤링


# 라이브러리 import
import requests
from bs4 import BeautifulSoup as bs
import warnings
warnings.filterwarnings('ignore')

url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=cur&date=20211001'

# 네이버 영화 평점 순위의 랭킹사이트의 데이터를 requests를 이용하여 가져오고
# parsing 하여 soup 변수에 저장

data = requests.get(url)
soup = bs(data.text)

# print(soup.head()[:5])

# 구조 지켜지게 출력
# print(soup.prettify())


# 메타정보에 관한 모든 파싱값을 meta변수에 저장하기
meta = soup.find_all('meta')
# print(meta)

# 랭킹테이블의 모든 파싱데이터를 가져와 lstRanking 변수에 저장하기
lstRanking = soup.find(class_='list_ranking')
print(lstRanking)
# print(lstRanking.find(class_='blind'))

# <table cellspacing="0" class="list_ranking">
# <caption class="blind">랭킹 테이블</caption>
# <col width="6%"/><col width="*"/><col width="15%"/><col width="3%"/><col width="12%"/><col width="2%"/><col width="5%"/>
# <thead>
# <tr>
# <th scope="col">순위</th>
# <th scope="col">영화명</th>
# <th colspan="3" scope="col">평점</th>
# <th colspan="2" scope="col">변동폭</th>
# </tr>
# </thead>
# <tbody>
# <tr><td class="blank01" colspan="8"></td></tr>
# <!-- 예제
# 				<tr>
# 					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_g50.gif" alt="50" width="14" height="13"></td>
# 					<td class="title"><a href="#">트랜스포머</a></td>
# 					<td class="ac"><img src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_down_1.gif" alt="down" width="7" height="10"></td>
# 					<td class="range ac">7</td>
# 				</tr>
# 				-->
# <tr>
# <td class="ac"><img alt="01" height="13" src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_r01.gif" width="14"/></td>
# <td class="title">
# <div class="tit5">
# <a href="/movie/bi/mi/basic.naver?code=186114" title="밥정">밥정</a>
# </div>
# </td>
# <!-- 평점순일 때 평점 추가하기  -->
# <td><div class="point_type_2"><div class="mask" style="width:96.30000114440918%"><img alt="" height="14" src="https://ssl.pstatic.net/imgmovie/2007/img/common/point_type_2_bg_on.gif" width="79"/></div></div></td>
# <td class="point">9.63</td>
# <td class="ac"><a class="txt_link" href="/movie/point/af/list.naver?st=mcode&amp;sword=186114">평점주기</a></td>
# <!----------------------------------------->
# <td class="ac"><img alt="na" class="arrow" height="10" src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_na_1.gif" width="7"/></td>
# <td class="range ac">0</td>
# </tr>
# <tr>
# <td class="ac"><img alt="02" height="13" src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_r02.gif" width="14"/></td>
# <td class="title">
# <div class="tit5">
# <a href="/movie/bi/mi/basic.naver?code=174830" title="가버나움">가버나움</a>
# </div>
# </td>
# <!-- 평점순일 때 평점 추가하기  -->
# <td><div class="point_type_2"><div class="mask" style="width:95.9000015258789%"><img alt="" height="14" src="https://ssl.pstatic.net/imgmovie/2007/img/common/point_type_2_bg_on.gif" width="79"/></div></div></td>
# <td class="point">9.59</td>
# <td class="ac"><a class="txt_link" href="/movie/point/af/list.naver?st=mcode&amp;sword=174830">평점주기</a></td>
# <!----------------------------------------->
# <td class="new_icon" colspan="2"><img alt="new" height="5" src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_new_1.gif" width="20"/></td>
# </tr>
# <tr>
# <td class="ac"><img alt="03" height="13" src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_r03.gif" width="14"/></td>
# <td class="title">
# <div class="tit5">
# <a href="/movie/bi/mi/basic.naver?code=151196" title="원더">원더</a>
# </div>
# </td>
# <!-- 평점순일 때 평점 추가하기  -->
# <td><div class="point_type_2"><div class="mask" style="width:95.29999732971191%"><img alt="" height="14" src="https://ssl.pstatic.net/imgmovie/2007/img/common/point_type_2_bg_on.gif" width="79"/></div></div></td>
# <td class="point">9.53</td>
# <td class="ac"><a class="txt_link" href="/movie/point/af/list.naver?st=mcode&amp;sword=151196">평점주기</a></td>
# <!----------------------------------------->
# <td class="ac"><img alt="down" class="arrow" height="10" src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_down_1.gif" width="7"/></td>
# <td class="range ac">1</td>
# </tr>
# <tr>
# <td class="ac"><img alt="04" height="13" src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_r04.gif" width="14"/></td>
# <td class="title">
# <div class="tit5">
# <a href="/movie/bi/mi/basic.naver?code=201073" title="코다">코다</a>
# </div>
# </td>
# <!-- 평점순일 때 평점 추가하기  -->
# <td><div class="point_type_2"><div class="mask" style="width:93.50000381469727%"><img alt="" height="14" src="https://ssl.pstatic.net/imgmovie/2007/img/common/point_type_2_bg_on.gif" width="79"/></div></div></td>
# <td class="point">9.35</td>
# <td class="ac"><a class="txt_link" href="/movie/point/af/list.naver?st=mcode&amp;sword=201073">평점주기</a></td>



# lstRanking에서 모든 영화의 순위, 이름, 평점, 영화정보링크를 가져와서 데이터프레임을 만들고
# movieTable 변수에 저장

import pandas as pd

title= [x.text.strip() for x in lstRanking.find_all('div',class_='tit5')]
point =[x.text for x in lstRanking.find_all('td',class_='point')]
rank = range(1,len(point)+1)
link = ['https://movie.naver.com' + x.a.get('href') for x in lstRanking.find_all('div',class_='tit5')]

movieTable = pd.DataFrame({'rank':rank,'title':title,'point':point,'link':link})

print(movieTable.head(4))

