
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
import time
import webbrowser
<<<<<<< HEAD


browser = webdriver.Firefox() #install 
browser.get("http:\\bit.do/wifion") 
time.sleep(2) #based on processor increase the time for initiallizing the browser 
username = browser.find_element_by_id("user") 
password = browser.find_element_by_id("password")
username.send_keys("------") #enter your pu wifi user name here 
password.send_keys("------") #enter  your pu wifi password here
=======
 
# firefox_capabilities = {}
# firefox_capabilities['marionette'] = True
# firefox_capabilities['binary'] = '/usr/bin/firefox'
browser = webdriver.Firefox()
browser.get("http:\\bit.do/wifion") 
time.sleep(2) 
username = browser.find_element_by_id("user") 
password = browser.find_element_by_id("password")
username.send_keys("149541") 
password.send_keys("3038praRAN") 
>>>>>>> 1e00778e810aef7b03b3dbd12288f8abe887e289
login_attempt = browser.find_element_by_xpath("//*[@type='submit']")
login_attempt.submit()
