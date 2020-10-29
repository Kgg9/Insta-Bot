from selenium import webdriver
from webdriver_manager.chrome import *
from time import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random import randint

driver = webdriver.Chrome(ChromeDriverManager().install())


# login script
class login:

    def __init__(self, user, psd):
        self.user = user
        self.psd = psd

        self.lscirpt()
        self.Lclick()
        self.Nclick()

    def lscirpt(self):
        driver.get("https://instagram.com")
        sleep(2)
        usearch = driver.find_element_by_name("username").send_keys(self.user)
        psearch = driver.find_element_by_name('password').send_keys(self.psd)
        psearch = driver.find_element_by_name('password').send_keys(Keys.RETURN)

    def Lclick(self):
        try:
            LC = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button')))
            LC.click()
        except:
            pass

    def Nclick(self):
        try:
            NC = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/div/div/div[3]/button[2]')))
            NC.click()
        except:
            pass



login('fish_can_drown', '')

class autoFollowSugs:
    def __init__(self):
        driver.find_element_by_xpath('//*[@id="react-root"]/section/main/section/div[3]/div[2]/div[1]/a/div').click()
        fllwBtn = driver.find_elements_by_xpath("//button[contains(.,'Follow')]")

        for i in fllwBtn[:5]:
            driver.execute_script("arguments[0].click();", i)
            sleep(1)


class fllwListCmnt:
    def __init__(self, *comments):

        self.comments = list(comments)
        length = len(self.comments)

        imgAlt = driver.find_elements_by_tag_name("img")
        fPic = imgAlt[0]
        lPic = imgAlt[-1]

        for i in imgAlt:
            while(i!=lPic):
                driver.find_element_by_class_name("RxpZH").click()
                sleep(1)
                cmntBox = driver.find_element_by_css_selector("form textarea").send_keys(self.comments[randint(0, length-1)])
                sleep(2)
                driver.find_element_by_xpath("//button[@type='submit']").click()
        fPic = lPic
        driver.refresh()




fllwListCmnt("bruh", "okurrrr", "boom")
