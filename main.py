#import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json

# Read config
with open('config.json', 'r') as jsonfile:
    config = json.load(jsonfile)
print(config)

options = webdriver.ChromeOptions()
#prefs = {
#    'profile.default_content_setting_values':
#        {
#            'notifications': 2
#        }
#}
#options.add_experimental_option('prefs', prefs)
options.add_argument("disable-infobars")
options.add_argument("disable-popup-blocking")
options.add_argument("--start-maximized")
#options.add_argument("--incognito")

# Remember to select the chromedriver corresponding with your OS
driver = webdriver.Chrome('./chromedriver', options=options)

# 104 main page
driver.get('https://www.104.com.tw/jobs/main/')
time.sleep(5)

context = driver.find_element('id', 'globalbar')
context = context.find_element('id', 'bar_m104')
context = context.find_element('id', 'global_bk')
context = context.find_element(By.CLASS_NAME, 'global_lr')
context = context.find_element(By.CLASS_NAME, 'right')
context = context.find_element(By.CLASS_NAME, 'global_nav')
login = context.find_element(By.XPATH, '//li[5]')
#login = context.find_element(By.CLASS_NAME, 'personal')
login.click()

# 104 login page
time.sleep(5)
email = driver.find_element(By.NAME, 'username')
passwd = driver.find_element(By.NAME, 'password')
email.send_keys(config.email)
time.sleep(0.5)
passwd.send_keys(config.password)
time.sleep(0.5)
button = driver.find_element(By.CLASS_NAME, 'Login__btn.btn.btn-primary.btn-size-large.w-full.mt-8')
button.click()

# Go to My 104

# Check your name then logout
