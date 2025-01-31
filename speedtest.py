from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

EMAIL = "pratipravadawn962@gmail.com"
PASS = "Xdawn1234"
USER = "dawn_takamine"

class InternetSpeedtestBot:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)
        self.up = 0
        self.down = 0


    def get_internet(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(10)
        trust = self.driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
        trust.click()
        button = self.driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/'
                                                    'div/div[2]/div[3]/div[1]/a')
        button.click()
        time.sleep(60)
        self.down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/'
                                                       'div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/'
                                                       'div/div[2]/span').text
        self.up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]'
                                                     '/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text

    def do_the_x(self):
        self.driver.get('https://x.com/i/flow/login')
        time.sleep(10)
        email = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/'
                                                   'div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')
        email.send_keys(EMAIL)
        email.send_keys(Keys.ENTER)
        time.sleep(5)
        username = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        username.send_keys(USER)
        username.send_keys(Keys.ENTER)
        time.sleep(5)
        password = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/'
                                                      'div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/'
                                                      'div[1]/input')
        password.send_keys(PASS)
        password.send_keys(Keys.ENTER)
        time.sleep(5)
        compose = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/header/div/div/'
                                                     'div/div[1]/div[3]/a')
        compose.click()
        time.sleep(3)
        msg = f'My internet speed is {self.down}down/{self.up}up. This is done by an automated robot.'
        post = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        post.send_keys(msg)
        button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div/button[2]')
        button.click()
