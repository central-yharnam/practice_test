import json
from foxbot.sel import *
from os import listdir
from os.path import isfile, join, abspath, dirname
import os
import sys
from pathlib import Path

direc = ["./students/"+ f for f in listdir("./students/") if isfile(join("./students/", f)) and f.endswith('.txt')]



daemon = selenium_daemon()
driver, wait = daemon.initialize()

for files in direc:
	print(files, "current file")

	test_data = open(files, "r")
	test_number = test_data.readline()[0:-1]
	#print(test_number, len(test_number))
	student_id = test_data.readline()[0:-1]
	#print(student_id, len(student_id))
	answers = test_data.readline()
	#try:
	print(answers)
	try:
		answers = answers.replace("\'", "\"")
		answers = json.loads(answers)
		test_data.close()
		daemon.student_test(test_number, student_id, answers, driver, wait)
		current_file = os.path.basename(files)
		parent = os.path.dirname(os.path.dirname(os.path.abspath(files)))
		os.rename(files, parent + "\\processed tests\\" + current_file)
		print(answers, "answers")

	except Exception as e:
		print(e)
		print("exception occurred")



# Python3 code to demonstrate 
# convert dictionary string to dictionary 
# using json.loads() 
'''import json 
  
# initializing string  
test_string = '{"Nikhil" : 1, "Akshat" : 2, "Akash" : 3}' 
  
# printing original string  
print("The original string : " + str(test_string)) 
  
# using json.loads() 
# convert dictionary string to dictionary 
res = json.loads(test_string) 
  
# print result 
print("The converted dictionary : " + str(res)) 
print(type(res))'''
