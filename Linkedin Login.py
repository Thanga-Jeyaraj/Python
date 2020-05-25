from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox(executable_path=r'/Users/thangathiruppathyjeyaraj/PycharmProjects/Sample2/geckodriver.exe')
driver.get('https://www.linkedin.com/')
driver.maximize_window()
signin=driver.find_element_by_xpath('//a[@class="cta-modal__primary-btn"]')
time.sleep(1)
signin.click()
driver.find_element_by_id("username").send_keys("User-ID")
time.sleep(1)
driver.find_element_by_id("password").send_keys("Password")
time.sleep(1)
driver.find_element_by_css_selector('div.login__form_action_container').click()
time.sleep(5)

