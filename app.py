import pandas as pd
from flask import Flask, render_template, request, jsonify
import datetime

app = Flask(__name__)
app.config["SECRET_KEY"] = 'd2707fea9778e085491e2dbbc73ff30e'

df = pd.read_csv('./output/Daegu_data.csv', encoding='cp949')
tempreture = df.loc[len(df)-1,'temp']

def get_dropdown_values():
    class_entry_relations = {
		'중구':{'동인동','삼덕동','성내1동','성내2동','성내3동','대신동','남산1동','남산2동','남산3동','남산4동','대봉1동','대봉2동'},
		'동구':{'신암1동','신암2동','신암3동','신암4동','신암5동','신천1.2동','신천3동','신천4동','효목1동','효목2동','도평동',
				'불로.봉무동','지저동','동촌동','방촌동','해안동','안심1동','안심2동','안심3동','안심4동','혁신동','공산동'},
		'서구':{'내당1동','내당2.3동','내당4동','비산1동','비산2.3동','비산4동','비산5동','비산6동','비산7동','평리1동','평리2동',
				'평리3동','평리4동','평리5동','평리6동','상중이동','원대동'},
		'남구':{'이천동','봉덕1동','봉덕2동','봉덕3동','대명1동','대명2동','대명3동','대명4동','대명5동','대명6동','대명9동',
				'대명10동','대명11동'},
		'북구':{'고성동','칠성동','침산1동','침산2동','침산3동','산격1동','산격2동','산격3동','산격4동','대현동','복현1동','복현2동',
				'검단동','무태조야동','관문동','태전1동','태전2동','구암동','관음동','읍내동','동천동','노원동','국우동'},
		'수성구':{'범어1동','범어2동','범어3동','범어4동','만촌1동','만촌2동','만촌3동','수성1가동','수성2.3가동','수성4가동',
				'황금1동','황금2동','중동','상동','파동','두산동','지산1동','지산2동','범물1동','범물2동','고산1동','고산2동','고산3동'},
		'달서구':{'성당동','두류1.2동','두류3동','감삼동','죽전동','장기동','용산1동','용산2동','이곡1동','이곡2동','신당동','본리동',
				'월성1동','월성2동','진천동','유천동','상인1동','상인2동','상인3동','도원동','송현1동','송현2동','본동'},
		'달성군':{'화원읍','논공읍','다사읍','유가읍','옥포읍','현풍읍','가창면','하빈면','구지면'}
	}                        
    return class_entry_relations

@app.route('/_update_dropdown')
def update_dropdown():
    # 자바스크립트에서 현재 선택된 항목 읽어옴
    selected_class = request.args.get('selected_class', type=str)
    # 선택된 항목에서 사용되는 dropdown의 항목을 읽어오기
    updated_values = get_dropdown_values()[selected_class]
    # 리스트 형식에서 JSON 형태로 변경
    html_string_selected = ''
    for entry in updated_values:
        html_string_selected += '<option value="{}">{}</option>'.format(entry, entry)
	# JSON으로 반환
    return jsonify(html_string_selected=html_string_selected)

@app.route('/_process_data')
def process_data():
    selected_class = request.args.get('selected_class', type=str)
    selected_entry = request.args.get('selected_entry', type=str)
    return jsonify(random_text="선택한 시군구: {} and 선택한 읍면동: {}".format(selected_class, selected_entry))

@app.route('/')
def home():
	df = pd.read_csv('./output/Daegu_data.csv', encoding='cp949')
	now_temp = df.loc[len(df)-1,'temp']
	now = str(datetime.datetime.now())
	default_classes = ['중구','동구','서구','남구','북구','수성구','달서구','달성군']
	default_value = get_dropdown_values()['중구']

	return render_template('layout.html', now_temp = now_temp, all_classes=default_classes, all_entries=default_value, now=now)

if __name__ == '__main__':
	app.run(debug=True)