from selenium import webdriver
import time
#password not filled buddy 


class InstaBot:
    def __init__(self, username , password):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.instagram.com")
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[2]/p/a').click()
        time.sleep(2)
        login_field = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input')\
                      .send_keys(username)
        login_field = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input')\
                      .send_keys(password)
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/section/div[3]/div[1]/div/div[2]/div[1]/a').click()
InstaBot('patil_aniketwagh','')        
