from selenium import webdriver
from selenium.webdriver.common.keys import Keys
user_name = "Chupa Ramirez Pelado "
password = "YOUR PASSWORD"
driver = webdriver.Chrome()
driver.get("https://www.google.com")
element = driver.find_elements_by_class_name("gb_g")
print("Tam de los elementos: ", len(element) )
element = driver.find_elements_by_class_name("gb_g")[0]
element.click()
##element.send_keys(user_name)
##element.send_keys(Keys.RETURN)
element.close()