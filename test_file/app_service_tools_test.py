from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get("https://appservicetools.azurewebsites.net/")
##element.click()
element=driver.find_elements_by_xpath('//*[@title="Cick to go..."]')
print("Cantidad de elementos: ", len(element))

for i in range(len(element)):
    try:
        element[i].click()
    except:
        print("Elemento # ", i+1, "genera exceptions")
    print("Accesando al elemento # ", i+1)
