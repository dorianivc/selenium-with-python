from analizador_de_texto import analizador_de_texto
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

analizador_de_archivos=None
try:
    analizador_de_archivos= analizador_de_texto()
    analizador_de_archivos.leer_archivo("tools\keys.txt")
    analizador_de_archivos.procesa_lineas()

except:
    print("No se leyo el archivo")
busqueda=str("Saludos desde Selenium usando Python")
user_name="dorianivc1@gmail.com"


chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
password=analizador_de_archivos.lineas[0]
driver =  webdriver.Chrome(chrome_options=chrome_options)
driver.get("https://www.facebook.com")
element = driver.find_element_by_id("email")
element.send_keys(user_name)
element = driver.find_element_by_id("pass")
element.send_keys(password)
element.send_keys(Keys.RETURN)
element= driver.find_element_by_name("xhpc_message")
element.send_keys(busqueda)
element= driver.find_elements_by_xpath('/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div[2]/div/div[3]/div/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div[3]/div[2]/button')[0]
element.click()
