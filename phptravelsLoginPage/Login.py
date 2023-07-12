from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:/Users/selenium/work space/chromedriver.exe")
driver.get("https://phptravels.org/login")
driver.maximize_window()
driver.implicitly_wait(5)
#driver.find_element(By.XPATH,"//a[@class='jfHeader-menuListLink jfHeader-dynamicLink jfHeader-login-action login']").click()
#driver.switch_to.new_window('https://phptravels.org/login')
driver.find_element(By.XPATH, "//input[@id='inputEmail']").send_keys("harikrishnaperam2@gmail.com")
driver.find_element(By.XPATH, "//input[@id='inputPassword']").send_keys("Harikrishna2@")
Frame=driver.find_element(By.XPATH,"//iframe[@title='reCAPTCHA']")
driver.switch_to.frame(Frame)
#wait = WebDriverWait (driver, 5)
#wait.until(expected_conditions.presence_of_element_located(By.XPATH, "//*[@id='#divDynamicRecaptcha1']/iframe")).click()
driver.switch_to.default_content()
driver.find_element(By.XPATH,"//button[@id='login']").click()