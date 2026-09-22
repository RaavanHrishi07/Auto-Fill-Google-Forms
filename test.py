import csv
import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

inputName = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
inputEmailID = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
inputPhone = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'

# Submit Button Xpath
Submit = '/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div/div'


def sleep():
    time.sleep(3)


service = Service(r"C:\Users\hrish\AppData\Local\Microsoft\WinGet\Packages\Mozilla.GeckoDriver_Microsoft.Winget.Source_8wekyb3d8bbwe\geckodriver.exe")
browswer = webdriver.Firefox(service=service)
browswer.get(
    'https://docs.google.com/forms/d/e/1FAIpQLSdpwoyn4MWDLhUgmt3cn3LH8c7337QUuv8v7Ss1kUe9lpa1Vg/viewform?usp=publish-editor'
)
name = []
email = []
phone = []
with open("input.csv", "r") as f_input:
    csv_input = csv.DictReader(f_input)
    for row in csv_input:
        name.append(row['name'])
        email.append(row['email'])
        phone.append(row['phone_number'])

    # print(name,email,phone)
i = 0

while i < len(name):
    browswer.find_element(By.XPATH,inputName).send_keys(name[i])
    browswer.find_element(By.XPATH,inputEmailID).send_keys(email[i])
    browswer.find_element(By.XPATH,inputPhone).send_keys(phone[i])
    sleep()
    browswer.find_element(By.XPATH,Submit).click()
    i += 1
    sleep()
    browswer.back()
    sleep()

# print(name,email,phone)
browswer.quit()
