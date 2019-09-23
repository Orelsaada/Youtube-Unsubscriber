from selenium import webdriver
from os import path
from time import sleep
from selenium.webdriver.common.by import By

# Driver stuff
script_folder = path.dirname(__file__)
driver_folder = path.join(script_folder,'chromedriver.exe')
driver = webdriver.Chrome(driver_folder)
driver.implicitly_wait(10)

# Variables
my_email = input('enter email: ')
email_pass = input('enter email pass: ')
url = 'https://www.youtube.com'
driver.get(url)

# Login to Youtube
youtube_login = driver.find_element(By.XPATH, '//*[@id="buttons"]/ytd-button-renderer/a')
driver.execute_script("arguments[0].click();", youtube_login)

driver.find_element_by_id('identifierId').send_keys(my_email)

next_button = driver.find_element(By.ID, 'identifierNext')
driver.execute_script("arguments[0].click();", next_button)

driver.find_element(By.NAME, 'password').send_keys(email_pass)

pass_next_button = driver.find_element(By.ID, 'passwordNext')
driver.execute_script("arguments[0].click();", pass_next_button)
print("[+] Logged to Youtube. [+]")

subscription_button = driver.find_element_by_link_text('Subscriptions')
driver.execute_script("arguments[0].click();", subscription_button)

manage_button = driver.find_element_by_xpath('//*[@id="subscribe-button"]/ytd-button-renderer/a').click()
sleep(3)

buttons = driver.find_elements_by_xpath('//*[@id="subscribe-button"]/ytd-subscribe-button-renderer/paper-button/yt-formatted-string')
count = 1
for button in buttons:
    try:
        button.click()
        confirm = driver.find_element_by_id('confirm-button').click()
        print(f'[+] Unsubscribe {count} channels. [+]')
        count += 1
    except:
        pass
    sleep(3)
driver.quit()
