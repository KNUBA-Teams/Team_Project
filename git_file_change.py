import pandas as pd
df = pd.read_csv('output/Daegu_data.csv')# 엑셀파일 읽기
df_daegu = pd.read_csv('./dataset/daegu_regionXY.csv')

df_daegu.dropna(inplace=True)

drop_list = df_daegu[df_daegu['1단계'] != '대구광역시'].index
df_daegu.drop(drop_list, inplace=True)

df_daegu.drop(['1단계','2단계','격자 X','격자 Y','경도(시)','경도(분)','경도(초)','위도(시)','위도(분)','위도(초)'], axis=1, inplace=True)
merge_outer = pd.merge(df,df_daegu, how='left', left_on='region', right_on='3단계')
merge_outer.drop('3단계', axis=1, inplace=True)
merge_outer.rename(columns={'경도(초/100)':'long','위도(초/100)':'lat'}, inplace=True)
merge_outer.to_csv('output/Daegu_data.csv', index=False)