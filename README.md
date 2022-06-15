# Team_Project
KNU Big Data Analyst Team Project (22.04' ~ 22.06')  

## Contributor  
서석정
박종원
임낙현
김형우
구민지
이은혜

## Index
>/dataset : 사용한 데이터를 저장해 놓은 폴더
>>/Cheonju : 청주 기상 데이터  ref)기상청
>>/Chuncheon : 춘천 기상 데이터  ref)기상청
>>/cyclone : 대구에 영향을 미친 태풍 데이터  ref)기상청
>>/Daegu : 대구 기상 데이터  ref)기상청
>>>0 토지지목별현황_20220506134728.csv : 녹지 데이터  ref)통계청
>>> 
>>/Daegu height : 대구 고도 데이터  ref)기상청
>>/Daejeon : 대전 기상 데이터  ref)기상청
>>/electrocity : 대구 전력 데이터  ref)한국전력공사
>>/population_1 : 
>>airpollution_daegu.csv : 
>>daegu_height.csv : 
>>daegu_regionXY.csv
>>daegu_regionXY.xlsx
>>geo_hangjeongdong.csv
>>HangJeongDong.geogson : 대구 읍면동에 대한 Geo
>/history
>>/Data history : 데이터 전처리를 할 때 사용한 코드들
>>/EDA history : 가설 검증할 때 사용한 코드들
>>/ML history : 머신러닝/딥러닝 할때 사용한 코드들
>/img : ipynb에서 사용한 이미지들
>/model : 학습된 모델을 저장
>/output : 출력된 파일들을 저장 ( 용량이 큰 파일이 대부분이라 git에는 올리지 않음 )
>/static : html 에서 불러들여 사용하는 파일들 (이미지, 폰트, css)
>/templates : Flask에서 사용하는 html 파일들
>.gitignore : git에 저장하지 않을 폴더 및 파일을 지정

┌ /dataset : 사용한 데이터를 저장해 놓은 폴더
│  ├ /Cheonju : 청주 기상 데이터  ref)기상청
│  ├ /Chuncheon : 춘천 기상 데이터  ref)기상청
│  ├ /cyclone : 대구에 영향을 미친 태풍 데이터  ref)기상청
│  ├ /Daegu : 대구 기상 데이터  ref)기상청
│  │  ├ 0 토지지목별현황_20220506134728.csv : 녹지 데이터  ref)통계청
│  │  └ 
│  ├ /Daegu height : 대구 고도 데이터  ref)기상청
│  ├ /Daejeon : 대전 기상 데이터  ref)기상청
│  ├ /electrocity : 대구 전력 데이터  ref)한국전력공사
│  ├ /population_1 : 
│  ├ airpollution_daegu.csv : 
│  ├ daegu_height.csv : 
│  ├ daegu_regionXY.csv
│  ├ daegu_regionXY.xlsx
│  ├ geo_hangjeongdong.csv
│  └ HangJeongDong.geogson : 대구 읍면동에 대한 Geo
├ /history
│  ├ /Data history : 데이터 전처리를 할 때 사용한 코드들
│  ├ /EDA history : 가설 검증할 때 사용한 코드들
│  └ /ML history : 머신러닝/딥러닝 할때 사용한 코드들
├ /img : ipynb에서 사용한 이미지들
├ /model : 학습된 모델을 저장
├ /output : 출력된 파일들을 저장 ( 용량이 큰 파일이 대부분이라 git에는 올리지 않음 )
├ /static : html 에서 불러들여 사용하는 파일들 (이미지, 폰트, css)
├ /templates : Flask에서 사용하는 html 파일들
├ .gitignore : git에 저장하지 않을 폴더 및 파일을 지정









ㅂ


01 download_data : 기상청 초단기 기상 데이터를 자동으로 다운받게 도와주는 파일