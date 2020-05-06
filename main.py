'''

  _____                _____   _    _   ____     ____               _____    _____      _    _   _______   _____   _        _____   _______  __     __
 |  __ \      /\      / ____| | |  | | |  _ \   / __ \      /\     |  __ \  |  __ \    | |  | | |__   __| |_   _| | |      |_   _| |__   __| \ \   / /
 | |  | |    /  \    | (___   | |__| | | |_) | | |  | |    /  \    | |__) | | |  | |   | |  | |    | |      | |   | |        | |      | |     \ \_/ / 
 | |  | |   / /\ \    \___ \  |  __  | |  _ <  | |  | |   / /\ \   |  _  /  | |  | |   | |  | |    | |      | |   | |        | |      | |      \   /  
 | |__| |  / ____ \   ____) | | |  | | | |_) | | |__| |  / ____ \  | | \ \  | |__| |   | |__| |    | |     _| |_  | |____   _| |_     | |       | |   
 |_____/  /_/    \_\ |_____/  |_|  |_| |____/   \____/  /_/    \_\ |_|  \_\ |_____/     \____/     |_|    |_____| |______| |_____|    |_|       |_|   
                                                                                                                                                      
                                                                            BY MULTIVALENCE                                                                                                                                                  

'''



from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
import time

print("\nThis is only Designed for Windows and requires Chrome\n")
print("Download chrome webdriver from : https://sites.google.com/a/chromium.org/chromedriver/downloads")
print("After download is complete extract the file")

name = input("What is your user account name on this computer? CASE SENSITIVE: ")
location = input("Where is the downloaded webdriver located? (e.g. Downloads) CASE SENSITIVE: ")

browser = webdriver.Chrome(f'C:\\Users\\{name}\\{location}\\chromedriver')

browser.get("https://mee6.xyz")

while True:
    selection = input('''\n\nPlease go to mee6.xyz on the new chrome tab that has opened. 
    Go to the moderator plugin and select the input bar for bad words. 
    A cursor should show. After that is done,

    - If you wish to remove in bulk, press "r" then enter.
    - If you wish to add pre-written words in bulk, press "a" then enter
    - If you wish to exit the program, press "e" then enter : ''')
    
    #ADDING ALL BAD WORDS
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
            
        
    #REMOVING ALL BAD WORDS
    elif selection == 'r':
        xmarks = browser.find_elements_by_class_name('TagCross')

        while True:
            try:
                if len(xmarks) == 0:
                    break


                for i in xmarks:
                    i.click()
                    time.sleep(0.1)

            except StaleElementReferenceException:
                xmarks = browser.find_elements_by_class_name('TagCross')
                
    
    #EXITING
    elif selection == 'e':
        break

    else:
        print("\nNot a Valid Option\n")






