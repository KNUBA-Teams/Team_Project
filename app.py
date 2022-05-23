# from flask import Flask, render_template

# app = Flask(__name__)

# ## 변수 -------------------------------------------------------------------------------------------------------------------------
# student_data = {
#     1: {"name": "김형우", "score": {"미술": 90, "씹덕": 100, "정신": -50, "Gay": 250, "문재인님":101}},
#     2: {"name": "박종원", "score": {"컴퓨터": 90, "밈": 150, "사과": 70}},
#     3: {"name": "서석정", "score": {}},
#     4: {"name": "임낙현", "score": {"키": 99, "반장":100, "네다씹": 80, "비정상":70}},
#     5: {"name": "Ropin", "score": {"ApexLegend": 90, "LoL": 90, "DestinyGardians":90, "Discord": 100000000000000}},
#     6: {"name": "유호준", "score": {"이호경": 100, "정희택": 80, "김형우":80}},
#     7: {"name": "정희택", "score": {"춘식":100, "춘배": 100, "영철": 100}}
# }

# ## 웹 디자인 --------------------------------------------------------------------------------------------------------------------
# @app.route('/')
# def index():
#     return render_template("index.html", template_students = student_data)

# @app.route('/home')
# def home():
#     return '''
#     <h1>이건 h1 제목</h1>
#     <p>이건 p 본문 </p>
#     <a href="https://flask.palletsprojects.com">Flask 홈페이지 바로가기</a>
#     '''

# @app.route('/user')
# def user():
# 	return '''
#     Hello, User!
#     <p>주소의 뒤에 "/유저명/유저ID" 를 붙이십시오.
#     '''

# @app.route('/user/<user_name>/<int:user_id>')
# def user_name(user_name, user_id):
#     return f'Hello, {user_name}({user_id})!'

# @app.route("/student/<int:id>")
# def student(id):
#     return render_template("student.html", 
#             template_name=student_data[id]["name"], 
#             template_score=student_data[id]["score"])

# if __name__ == '__main__':
#     app.run(debug=True) 

#=======================================================================================================================================

from flask import Flask, render_template, url_for, flash, redirect

## 변수 -------------------------------------------------------------------------------------------------------------------------
eda_data = {
    1: {"name": "겨울에 따뜻하면 여름에 폭염이 나타난다.", "img": {"1": "static/1.jpg", "2": 'static/김형우2.jpg'}},
    2: {"name": "인구밀도가 높은 지역은 상대적으로 열지수가 높다.", "img": {}},
    3: {"name": "지역용도에 따라 열지수의 차이가 나타난다.", "img": {}},
    4: {"name": "기저질환 환자가 온열질환 취약계층이다.", "img": {}}
}

app = Flask(__name__)
app.config["SECRET_KEY"] = 'd2707fea9778e085491e2dbbc73ff30e'

@app.route('/')
def home():
	return render_template('layout.html')

if __name__ == '__main__':
	app.run(debug=True)
