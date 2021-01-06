from flask import Flask, render_template, request, url_for, redirect
from foxbot.sel import *
import time
import random
import string
from datetime import date 
from templates.test import *

app = Flask(__name__)


uh = []

@app.route('/')
@app.route('/index')
def index():
    return render_template("dropdown.html")

@app.route('/test', methods=['GET', 'POST'])
def login():

	print("login active")

	print("what the fuck")
	if request.method == "POST":
		print (request.form['test'])
	return loop()
	'''if request.method == "POST":
		car_brand = request.form.get("cars", None)
		if car_brand!=None:
		return render_template("./dropdown.html", car_brand = car_brand)
	if request.method == 'GET':'''

	#return render_template("dropdown.html")
@app.route('/test/submit', methods=['POST'])
def log2():

	if request.method == "POST":
		print (request.form)
		test_num = request.form['num']
		student_id = request.form['student']
		answers = {}
		for i in request.form:
			uh.append(i)
			if i == 'num':
				test_num = request.form[i]
			elif i == 'student':
				student_id = request.form[i]
			else:
				print(test_num, student_id, answers)
				answers[i] = request.form[i]
				test_data = open("./students/" + str(student_id)+".txt", "w") 
		for items in [test_num + '\n', student_id + '\n', str(answers)]:
			test_data.write(items)
					
		return "Test received"


if __name__ == '__main__':

	app.run(debug=True)