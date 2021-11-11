from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from os import getenv
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
# my_driver = webdriver.Chrome(executable_path="c:/Users/avielb/Downloads/chromedriver.exe")
my_driver = webdriver.Chrome(executable_path="/Users/avielb/Downloads/chromedriver")
try:
    my_driver.maximize_window()
    my_driver.get("https://sparknesua.ordernet.co.il/#/auth")
    my_driver.find_element_by_xpath("//*[@id=\"login_form\"]/fieldset/div[1]/input").send_keys(getenv("SPARK_USER"))
    my_driver.find_element_by_xpath("//*[@id=\"password\"]").send_keys(getenv("SPARK_PASS") + Keys.ENTER)
    sleep(5)
    my_driver.find_element_by_xpath("//*[@id=\"scxBody\"]/div[5]/div/div/div/div[2]/div[2]/div[6]/button").send_keys(Keys.SPACE)
    my_driver.find_element_by_xpath("//*[@id=\"navbar\"]/ul[1]/li[2]/a").send_keys(Keys.ENTER)
    my_driver.find_element_by_xpath("//*[@id=\"navbar\"]/ul[1]/li[2]/ul/li[2]/a").send_keys(Keys.ENTER)
    sleep(4)
    my_driver.find_element_by_xpath("//*[@id=\"scxBody\"]/div[3]/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/div[1]/div/div[3]/label/span").click()
    sleep(5)
except BaseException as e:
    print(e.args)
finally:
    my_driver.close()