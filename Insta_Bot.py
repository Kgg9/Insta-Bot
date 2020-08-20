from selenium import webdriver
from webdriver_manager.chrome import *
from time import *
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(ChromeDriverManager().install())


# login script
class login:

    def __init__(self, user, psd):
        self.user = user
        self.psd = psd

        self.lscirpt()

    def lscirpt(self):
        driver.get("https://instagram.com")
        sleep(1)
        usearch = driver.find_element_by_name("username").send_keys(self.user)
        psearch = driver.find_element_by_name('password').send_keys(self.psd)




login('fish_can_drown', 'AwAw!234')

