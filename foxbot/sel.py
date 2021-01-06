from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
import random
import string
from datetime import date 

#answer is a list of a list, when it is popped into the elem = driver.find_element_by_xpath("//input[@tabindex=4]")
# elem.send_keys(answer.pop()), it fills out every subsequent field perfectly, until question 114 then all of them get bunched up into
# one field. I have no idea why.

#answer = [random.choices(string.ascii_uppercase + string.digits, k=110)]

class selenium_daemon:
	
	def initialize(self):
		driver = webdriver.Firefox()
		wait = WebDriverWait(driver, 5)

		driver.get("https://onlinescoretracker.com/company/sap2356")
		elem = driver.find_element_by_name("username")
		elem.send_keys("XXXXXXXXXXXX")
		elem = driver.find_element_by_name("password")
		elem.send_keys("XXXXXXXXXXXX")
		elem = driver.find_element_by_name("submit")
		elem.click()
		return driver, wait

	def student_test(self, test_num, student_id, answers, driver, wait):

		driver.get("https://onlinescoretracker.com/user-panel/tests/addTest")
		wait.until(ec.invisibility_of_element_located((By.XPATH, "//div[@class='se-pre-con']")))

		elem = driver.find_element_by_name("test_type")
		select_element = Select(elem)

		select_element.select_by_value('9')

		today = date.today() 
		print("Today date is: ", today) 
		elem = driver.find_element_by_name("test_date")
		elem.send_keys(str(today))
		driver.find_element_by_xpath("//body").click()

		wait.until(ec.invisibility_of_element_located((By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-e']")))
		elem = driver.find_element_by_name("test_name")

		select_element = Select(elem)
		select_element.select_by_value('SAT Practice Test #'+str(test_num))

		elem = driver.find_element_by_name("studentid")

		elem = driver.find_element_by_xpath("//div[@class='chosen-container chosen-container-single']").click()

		elem = driver.find_element_by_xpath("/html/body/div[19]/div/div/div[2]/div[4]/div/div[1]/fieldset/form/table/tbody/tr[6]/td[3]/div/div/div/input")

		elem.send_keys(str(student_id))

		elem = driver.find_element_by_xpath("/html/body/div[19]/div/div/div[2]/div[4]/div/div[1]/fieldset/form/table/tbody/tr[6]/td[3]/div/div/ul/li")
		elem.click()

		elem = driver.find_element_by_name("")
		elem.click()


		for res in answers:
			a = res[0:-1]
			ind = int(a) + 3
			print(res)
			elem = driver.find_element_by_xpath("//input[@tabindex="+str(ind)+"]")
			elem.send_keys(answers[res])

		elem = driver.find_element_by_xpath("/html/body/div[19]/div[1]/div/div[2]/form/div/div[1]/div[2]/ul/li[1]/input")
		wait.until(ec.invisibility_of_element_located((By.XPATH, "/html/body/div[18]")))
		elem.click()

