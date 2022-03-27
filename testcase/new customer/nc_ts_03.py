from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="F:\pythonTestProject\drivers\chromedriver.exe")
driver.get("http://google.com")

driver.maximize_window()

print("URL : " + driver.current_url)
# open website
driver.get("https://demo.guru99.com/v4/index.php")

# username
username = driver.find_element(By.XPATH, "/html/body/form/table/tbody/tr[1]/td[2]/input")
username.send_keys("mngr393469")

# password
password = driver.find_element(By.XPATH, "/html/body/form/table/tbody/tr[2]/td[2]/input")
password.send_keys("UnEbAmA")

# submit
submit = driver.find_element(By.XPATH, "/html/body/form/table/tbody/tr[3]/td[2]/input[1]")
submit.click()


# open registration page
registration = driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[2]/a")
registration.click()

# name
name2 = driver.find_element(By.XPATH, "/html/body/table/tbody/tr/td/table/tbody/tr[4]/td[2]/input")
name2.send_keys("Shaik MD Ibnay Momen @")