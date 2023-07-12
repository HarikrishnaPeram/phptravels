import time

import self as self
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.select import Select


driver = webdriver.Chrome(executable_path="C:/Users/selenium/work space/chromedriver.exe")
driver.get("https://phptravels.com/")
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element(By.XPATH, "//a[@style='color:#000!important;font-size:13px']").click()
driver.get("https://phptravels.org/register.php")
time.sleep(10)
driver.find_element(By.XPATH,"(//input[@id='inputFirstName'])[1]").send_keys("Hari")
driver.find_element(By.XPATH,"//input[@id='inputLastName']").send_keys("Krishna")
driver.find_element(By.CSS_SELECTOR,"#inputEmail").send_keys("Hari47340")
driver.find_element(By.XPATH,"//div[@class='selected-dial-code']").click()
driver.find_element(By.XPATH,"//input[@id='inputPhone']").send_keys("7013568898")
driver.find_element(By.XPATH, "//input[@id='inputCompanyName']").send_keys("ABC Company")
driver.find_element(By.XPATH,"//input[@id='inputAddress1']").send_keys("Street1")
driver.find_element(By.XPATH,"//input[@id='inputAddress2']").send_keys("Street2")
driver.find_element(By.XPATH,"//input[@id='inputCity']").send_keys("City")
driver.find_element(By.XPATH,"//input[@id='stateinput']").send_keys("State")
driver.find_element(By.XPATH,"//input[@id='inputPostcode']").send_keys("524440")
dropdown =Select(driver.find_element(By.XPATH,"//select[@id='inputCountry']"))
dropdown.select_by_visible_text("India")
driver.find_element(By.XPATH,"//input[@id='customfield2']").send_keys("7013568898")
driver.find_element(By.CSS_SELECTOR,"#inputNewPassword1").send_keys(987654321)
driver.find_element(By.CSS_SELECTOR,"#inputNewPassword2").send_keys(987654321)
driver.find_element(By.XPATH,"//input[@value='Register']").click()
