from flask import Flask, render_template, url_for, flash, redirect

app = Flask(__name__)
app.config["SECRET_KEY"] = 'd2707fea9778e085491e2dbbc73ff30e'

@app.route('/')
def home():
	return render_template('layout.html')

if __name__ == '__main__':
	app.run(debug=True)
