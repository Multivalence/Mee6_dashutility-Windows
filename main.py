#REMOVING IN BULK COMING SOON

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

print("\nThis is only Designed for Windows and requires Chrome\n")
print("Download chrome webdriver from : https://sites.google.com/a/chromium.org/chromedriver/downloads")
print("After download is complete extract the file")

name = input("What is your user account name on this computer? CASE SENSITIVE: ")
location = input("Where is the downloaded webdriver located? (e.g. Downloads) CASE SENSITIVE: ")

browser = webdriver.Chrome(f'C:\\Users\\{name}\\{location}\\chromedriver')

browser.get("https://google.com")

while True:
    selection = input('''\n\nPlease go to mee6.xyz on the new chrome tab that has opened. 
    Go to the moderator plugin and select the input bar for bad words. 
    A cursor should show. After that is done, 
    if you wish to remove in bulk, press r then enter.
    If you wish to add in bulk, press a then enter : ''')

    if selection == 'a':

        bar = browser.find_element_by_class_name('TagAddInput')

        with open('words.txt','r') as textfile:
            x = textfile.read()
            x = x.split("\n")
            textfile.close()

        for i in range(len(x)):
            bar.send_keys(x[i])
            time.sleep(0.1)
            bar.send_keys(Keys.ENTER)
        break

    elif selection == 'r':
        print("Removing in Bulk coming soon")
        break

    else:
        print("\nNot a Valid Option\n")






