"""
Using Python Selenium Automation And the URL https://www.cowin.gov.in/
you have to
1. click on the "Create FAQ" and "Partners" anchor tags present on the Home Page and open the new windows
2. Now, you have to fetch the opened windows/ frame ID and display the same on the console
3. Kindly close the two new windows and come back to the home page also.
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 15, poll_frequency=1)
driver.maximize_window()
driver.get("https://www.cowin.gov.in/")

element = wait.until(ec.visibility_of_element_located((By.LINK_TEXT, "FAQ")))
element.click()

time.sleep(2)

element = wait.until(ec.visibility_of_element_located((By.XPATH, "//li//a[contains(@href, '/our-partner')]")))
element.click()

time.sleep(3)

windows_list = driver.window_handles
print(windows_list)

time.sleep(5)
driver.quit()

