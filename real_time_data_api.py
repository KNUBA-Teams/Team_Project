import pandas as pd
import datetime
import time
import requests
import json

# 한자리수인 숫자를 두자리수인 문자로 변경하는 함수
def str_2words(word):
    word = str(word)
    if len(word)==1:
        word='0'+word
    return word

# 기존의 데이터 불러오기
df = pd.read_csv('./output/Daegu_data.csv')

# 읍면동과 위치 데이터
df_daegu = pd.read_csv('./dataset/daegu_regionXY.csv')
df_daegu.dropna(inplace=True)
drop_list = df_daegu[df_daegu['1단계'] != '대구광역시'].index
df_daegu.drop(drop_list, inplace=True)
df_daegu.drop(['1단계','2단계','경도(시)','경도(분)','경도(초)','위도(시)','위도(분)','위도(초)','경도(초/100)','위도(초/100)'], axis=1, inplace=True)

while(True):
    # 현재 시각
    now = datetime.datetime.now()

    # 1시간 전에 해당하는 과거 데이터가 없을 때
    if datetime.datetime(year=df.iloc[len(df)-1,0], month=df.iloc[len(df)-1,1], day=df.iloc[len(df)-1,2], hour=df.iloc[len(df)-1,3]) <= now - datetime.timedelta(hours=2):
        # api를 부르기 위한 값들 설정
        base_url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst?serviceKey='
        serviceKey = 'U4YvEM6l6J58M949SHQpfEwFm7ZNve4WNkKnXgdeb2mkxFMws8amIjVNvAVyhg5m%2Bht%2BsccUyMv7TnybLn5fzg%3D%3D'
        base_year = now.year
        base_month = now.month
        base_day = now.day
        base_time = now.hour
        if base_time == 0:
            base_day = base_day-1
            base_time = 23
        else:
            base_time = base_time-1
        headers = {'Content-Type': 'application/json', 'charset': 'UTF-8', 'Accept': '*/*'}

        # 읍면동 별로 반복
        for index, rows in df_daegu.iterrows():
            # api를 부르기 위한 값들 설정
            region = rows[0]
            nx = rows[1]
            ny = rows[2]

            # api를 JSON형식으로 읽어와서 Parsing
            res = requests.get(base_url+serviceKey+'&pageNo=1&numOfRows=1000&dataType=JSON&base_date='+str(base_year)+str_2words(base_month)+str_2words(base_day)+'&base_time='+str_2words(base_time)+'00&nx='+str(nx)+'&ny='+str(ny), headers=headers)
            jsonObject = json.loads(res.text).get("response").get("body").get("items").get("item")
            for i in jsonObject:
                if i.get('category') == 'REH':
                    hum = i.get('obsrValue')
                elif i.get('category') == 'RN1':
                    rain = i.get('obsrValue')
                elif i.get('category') == 'T1H':
                    temp = i.get('obsrValue')
                elif i.get('category') == 'VEC':
                    wind_direction = i.get('obsrValue')
                elif i.get('category') == 'WSD':
                    wind_speed = i.get('obsrValue')
            
            # 데이터를 DataFrame에 저장
            df.loc[len(df)] = [base_year,base_month,base_day,base_time,temp,rain,hum,wind_speed,wind_direction,region]
        
        # DF를 local에 저장
        df.to_csv('./output/Daegu_data.csv', index=False)

        # 실행 문구 출력
        print(datetime.datetime.now(), ':', base_time, 'h data addition is success')
    else:
        # 실행 문구 출력
        print(datetime.datetime.now(), ': unnecessary state, already updated data')
    
    # 1분마다 반복하여 갱신
    time.sleep(60)