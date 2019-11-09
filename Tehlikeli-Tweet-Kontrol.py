from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium
import time
import datetime

        
def findTweets(user):
    driver.get("https://twitter.com/" + user +"/with_replies")

    time.sleep(2)
    results = []
    

    danger = []
    print("Aranacak her kelime'yi girip enter a basın... Devam Etmek içi '0' a basın.")
    i=0
    while True:
        i+=1
        temp = input(f"aranacak {i}.kelime'yi girin: ")
        temp = temp.lower()
        danger.append(temp)

        print("Devam etmek için '0' a basın")
        if temp == '0':
            break
    danger.pop()
    
    temp = driver.find_elements_by_xpath("//div[@data-testid='tweet']/div[2]")

    for i in temp:

        temp2 = i.find_element_by_xpath("div[2]").text

        if temp2.find("Replying to") == -1:
            if temp2 not in results:
                results.append(temp2)   
        else:
            temp3 = i.find_element_by_xpath("div[3]").text
            temp4 = temp2 +"\n"+ temp3
            if temp4 not in results:
                results.append(temp4) 

        
        
 
    
    last_y = len(results)
    print(last_y)
    count = 0
    action = webdriver.ActionChains(driver)
    while True:
        action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
        time.sleep(2)
 
        temp = driver.find_elements_by_xpath("//div[@data-testid='tweet']/div[2]")
        time.sleep(2)

        for i in temp:
            temp2 = i.find_element_by_xpath("div[2]").text
            if temp2.find("Replying to") == -1:
                if temp2 not in results:
                    results.append(temp2)   
            else:
                temp3 = i.find_element_by_xpath("div[3]").text
                temp4 = temp2 +"\n"+ temp3
                if temp4 not in results:
                    results.append(temp4) 
        
        new_y = len(results)
        
        count +=1
        if count == 5:
            count = 0
            if last_y == new_y:
                break
            else:
                last_y=new_y
                print(last_y)
    
    count = 1
    with open("dangerous.txt","w",encoding="UTF-8") as file:
        for i in results:
            print(f"{count} - {i}")
            temp2 = i.lower()
            count += 1
            print("****")
            for z in danger:
                if temp2.find(z) != -1:
                    file.write(i+"\n **** \n")
                    break
                    
    

     

user = input("username: ")
pasw = input("password: ")

driverOption = webdriver.ChromeOptions()
driverOption.add_experimental_option('prefs',{'intl.accept_languages':'en,en_US'})
driver = webdriver.Chrome('chromedriver.exe',chrome_options=driverOption)

url = "https://twitter.com/login"
driver.get(url)
driver.maximize_window() 

time.sleep(2)

usernameInput = driver.find_element_by_xpath("//*[@id='page-container']/div/div[1]/form/fieldset/div[1]/input").send_keys(user)
passwordInput = driver.find_element_by_xpath("//*[@id='page-container']/div/div[1]/form/fieldset/div[2]/input").send_keys(pasw)

btnSubmit = driver.find_element_by_xpath("//*[@id='page-container']/div/div[1]/form/div[2]/button").click()


user = input("username girin : ")
findTweets(user)


