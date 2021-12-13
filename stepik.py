from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/alert_accept.html"



try:
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
  
    
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css("button[type='submit']")
    button.click()
    
    confirm = browser.switch_to_alert
    confirm.accept()
    
    x_element = browser.find_element_by_css("span[id='input_value']")
    x = x_element.text
    y = calc(x)
    
    promt = browser.find_element_by_css("input[id='answer']")
    promt.send_keys(y)
    
    submit_btn = browser.find_element_by_css("button[type='submit']")
    submit_btn.click()
    
    

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()