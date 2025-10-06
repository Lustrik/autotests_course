from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button1 = browser.find_element(By.ID, "book")

    price = WebDriverWait(browser, 120).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
   
    button1.click()
    
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)

    button2 = browser.find_element(By.ID, "solve")
    button2.click()

finally:
    
    time.sleep(10)
    browser.quit()
