import os
import time

repo_name = input('repo name:   ')


os.system('git init')
os.system('git add .')
os.system('git commit -m "last commit before the push" ')

from selenium import webdriver
PATH = 'your path of the webdriver'




driver = webdriver.Chrome(PATH)
driver.get("https://github.com/organizations/courses-of-it/repositories/new")


username = driver.find_element_by_name('login')
password = driver.find_element_by_name('password')

username.send_keys('username')
password.send_keys('password')
driver.find_element_by_name('commit').click()




name = driver.find_element_by_name('repository[name]')
name.send_keys(repo_name)
driver.find_element_by_name('repository[visibility]').click()
button = driver.find_elements_by_css_selector('.btn-primary')[0]
time.sleep(3)
button.click()


command_origin = driver.find_elements_by_css_selector('.user-select-contain')[5].text

os.system(command_origin)
os.system('git push origin master')