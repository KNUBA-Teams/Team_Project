# Team_Project
KNU Big Data Analyst Team Project (22.04' ~ 22.06')  
최종 결과물 : http://34.64.221.54:8000/  

## Contributor  
서석정 
박종원 
임낙현 
김형우 
구민지 
이은혜

## Index
┌ /dataset : 사용한 데이터를 저장해 놓은 폴더  
│&nbsp;&nbsp;├ /Cheonju : 청주 기상 데이터  ref)기상청  
│&nbsp;&nbsp;├ /Chuncheon : 춘천 기상 데이터  ref)기상청  
│&nbsp;&nbsp;├ /cyclone : 대구에 영향을 미친 태풍 데이터  ref)기상청  
│&nbsp;&nbsp;├ /Daegu : 대구 기상 데이터  ref)기상청  
│&nbsp;&nbsp;│&nbsp;&nbsp;└ 0 토지지목별현황_20220506134728.csv : 녹지 데이터  ref)통계청     
│&nbsp;&nbsp;├ /Daegu height : 대구 고도 데이터  ref)국가공간정보포털  
│&nbsp;&nbsp;├ /Daejeon : 대전 기상 데이터  ref)기상청  
│&nbsp;&nbsp;├ /electrocity : 대구 전력 데이터  ref)한국전력공사  
│&nbsp;&nbsp;├ /population_1 : 대구 읍면동별 인구 수 데이터 ref)대구 통계  
│&nbsp;&nbsp;├ airpollution_daegu.csv : 대구 대기 오염 데이터  
│&nbsp;&nbsp;├ daegu_height.csv : 대구 고도 통합 데이터  
│&nbsp;&nbsp;├ daegu_regionXY.csv : 전국 읍면동의 좌표 및 위도, 고도 데이터 ref)공공데이터  
│&nbsp;&nbsp;├ daegu_regionXY.xlsx : 전국 읍면동의 좌표 및 위도, 고도 데이터 ref)공공데이터  
│&nbsp;&nbsp;├ geo_hangjeongdong.csv  
│&nbsp;&nbsp;└ HangJeongDong.geogson : 대구 읍면동에 대한 GeoJSON  
├ /history  
│&nbsp;&nbsp;├ /Data history : 데이터 전처리를 할 때 사용한 코드들  
│&nbsp;&nbsp;├ /EDA history : 가설 검증할 때 사용한 코드들  
│&nbsp;&nbsp;├ /ML history : 머신러닝/딥러닝 할때 사용한 코드들  
│&nbsp;&nbsp;└ real_time_data_aip.ipynb : 실시간 데이터 수집을 위한 코드  
├ /img : ipynb에서 사용한 이미지들  
├ /model : 학습된 모델을 저장  
├ /output : 출력된 파일들을 저장 ( 용량이 큰 파일이 대부분이라 git에는 올리지 않음 )  
├ /static : html 에서 불러들여 사용하는 파일들 (이미지, 폰트, css)  
├ /templates : Flask에서 사용하는 html 파일들  
├ .gitignore : git에 저장하지 않을 폴더 및 파일을 지정  
├ 01 download_data.ipynb : 기상청 초단기 기상 데이터를 자동으로 다운받게 도와주는 코드  
├ 02 Daegu_combine.ipynb : 기상청에서 받은 데이터를 하나의 파일로 합쳐주는 코드  
├ 03 preprocessing, EDA.ipynb : 전처리 및 가설 검증에 대한 코즈  
├ 04 prototpye.ipynb : 딥러닝에 대한 코드  
├ 10 DB_load_code.ipynb : PostgreSQL과 python을 연결해주는 코드  
├ 98 installing_modules.ipynb : 파이썬에서 사용할 패키지를 설치하는 코드  
├ 99 삽질 기록.txt : 진행하면서 삽질한 기록  
├ app.py : flask를 통해 웹으로 구현하는 코드  
├ chromedrive.exe : 크롤링에서 사용하는 브라우저  
├ README.md : 프로젝트에 대한 설명  
└ real_time_data_api.py : api를 통해 실시간 데이터 수집을 하는 코드(Google Cloud Platform에서 실행했음)  










