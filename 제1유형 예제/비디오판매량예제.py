

# 비디오게임 판매량 및 등급


'''
데이터셋
설명
** 여러
플랫폼의
년도별
출시된
게임
데이터셋 **
출처: https: // mlcourse.ai /
Name: 게임명
Platform: 출시
플랫폼
Year_of_Release: 출시년도
Genre: 장르
Publisher: 출시
업체
{지역별}
_Sales: 판매량
User_Score: 유저스코어(tbd: 측정
안됨)
Developer: 개발
업체
Rating: 이동등급()

'''


dataUrl = 'https://raw.githubusercontent.com/Datamanim/video/master/video_games_sale.csv'

# 데이터 로드
import pandas as pd
pd.set_option('max_columns', None)
df = pd.read_csv(dataUrl, encoding='utf-8')
print(df)
# print(type(df))



# 데이터셋의(Year_of_Release) 출시년도 컬럼을 10년단위(ex 1990~1999 : 1990)로 변환하여
# 새로운 컬럼(year_of_ten)에 추가하고
# 게임이 가장 많이 출시된 년도(10년단위)와 가장 적게 출시된 년도(10년단위)를 각각 구하여라

df['year_of_ten'] = df['Year_of_Release'].map(lambda x: x//10*10)

Max = int((df['year_of_ten'].value_counts()).index[0])
Min = int((df['year_of_ten'].value_counts()).index[-1])
# print('MAX : ',Max,'Min : ', Min)

# 플레이스테이션 플랫폼 시리즈(PS,PS2,PS3,PS4,PSV)중 장르가 Action로 발매된 게임의 총 수 구하기
# isin() 함수사용

# print(df.Platform.unique())
df_platform =df[df.Platform.isin(['PS','PS2','PS3','PS4','PSV'])]
# print(len(df_platform[df_platform.Genre == 'Action']))


# 게임이 400개 이상 출시된 플랫폼들을 추출하여
# 각 플랫폼의 User_Score 평균값을 구하여 데이터프레임을 만들고
# 값을 내림차순으로 정리하여 출력하라

over_400pf = df.Platform.value_counts()[df.Platform.value_counts() >=400].index
# print(over_400pf)
plover_400 = df[df.Platform.isin(over_400pf)]
scoremean = plover_400.groupby('Platform')['User_Score'].mean().sort_values(ascending=False)
scoremean_df =pd.DataFrame(scoremean)
# print(scoremean_df)
# print(type(scoremean))
# print(type(scoremean_df))


# 게임 이름에 Mario가 들어가는 게임을 3회 개발한 개발자(Developer컬럼)을 구하기
mario_df = df[df.Name.str.contains('Mario')]
# print(mario_df.Developer.value_counts()[mario_df.Developer.value_counts() ==3].index)


# PS2 플랫폼으로 출시된 게임들의 User_Score의 첨도를 구하기
#첨도 kurtosis()

ps2_kurtosis = df[df.Platform == 'PS2'].User_Score.kurtosis()
# print(ps2_kurtosis)

# 각 게임별 NA_Sales,EU_Sales,JP_Sales,Other_Sales 값의 합은 Global_Sales와 동일해야한다.
# 소숫점 2자리 이하의 생략으로 둘의 값의 다른경우가 존재하는데, 이러한 케이스가 몇개 있는지 확인하라
ans = (df[['NA_Sales','EU_Sales', 'JP_Sales', 'Other_Sales']].sum(axis=1) != df.Global_Sales).sum()
# print(ans)

# User_Count컬럼의 값이 120 이상인 게임들 중에서
# User_Score의 값이 9.0이상인 게임의 수를 구하여라
df_120 = df[df.User_Count >=120]
print(len(df_120[df_120.User_Score >=9.0]))

# Global_Sales컬럼의 값들을 robust스케일을 진행하고 40이상인 데이터 수를 구하여라
from sklearn.preprocessing import RobustScaler

rs =RobustScaler()
rs_after = rs.fit_transform(df.Global_Sales.values.reshape(-1,1))
# print(len(rs_after[rs_after>=40]))
