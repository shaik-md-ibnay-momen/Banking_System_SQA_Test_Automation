from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="F:\pythonTestProject\drivers\chromedriver.exe")
driver.get("http://google.com")

driver.maximize_window()

print("URL : " + driver.current_url)
# open website
driver.get("https://demo.guru99.com/v4/index.php")

# username
username = driver.find_element_by_xpath("/html/body/form/table/tbody/tr[1]/td[2]/input")
username.send_keys("mngr393469")

# password
password = driver.find_element_by_xpath("/html/body/form/table/tbody/tr[2]/td[2]/input")
password.send_keys("UnEbAmA")

# submit
submit = driver.find_element_by_xpath("/html/body/form/table/tbody/tr[3]/td[2]/input[1]")
submit.click()


# open registration page
registration = driver.find_element_by_xpath("/html/body/div[3]/div/ul/li[2]/a")
registration.click()

# name
name2 = driver.find_element(By.NAME, "name")
name2.send_keys("Shaik MD Ibnay Momen")

# gender
driver.find_element_by_xpath("/html/body/table/tbody/tr/td/table/tbody/tr[5]/td[2]/input[1]").click()

# date of birth
birthdate = driver.find_element_by_xpath("//*[@id='dob']")
birthdate.send_keys("01131997")

# address
address = driver.find_element_by_xpath("/html/body/table/tbody/tr/td/table/tbody/tr[7]/td[2]/textarea")
address.send_keys("House No 318 Road No 21 Mohakhali DOHS")

# city
city = driver.find_element_by_xpath("/html/body/table/tbody/tr/td/table/tbody/tr[8]/td[2]/input")
city.send_keys("Dhaka")

# state
state = driver.find_element_by_xpath("/html/body/table/tbody/tr/td/table/tbody/tr[9]/td[2]/input")
state.send_keys("Dhaka")

# pin
pin = driver.find_element_by_xpath("/html/body/table/tbody/tr/td/table/tbody/tr[10]/td[2]/input")
pin.send_keys("121212")

# Phone_Number
Phone_Number = driver.find_element_by_xpath("/html/body/table/tbody/tr/td/table/tbody/tr[11]/td[2]/input")
Phone_Number.send_keys("01635163488")

# email
email = driver.find_element_by_xpath("/html/body/table/tbody/tr/td/table/tbody/tr[12]/td[2]/input")
email.send_keys("shaikmohammad126@gmail.com")

# password
password = driver.find_element_by_xpath("/html/body/table/tbody/tr/td/table/tbody/tr[13]/td[2]/input")
password.send_keys("shaikh1234")

# submit
submit = driver.find_element_by_xpath("/html/body/table/tbody/tr/td/table/tbody/tr[14]/td[2]/input[1]")
submit.click()

