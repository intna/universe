from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


# 初始化浏览器的driver
def driver_init():
    option = webdriver.ChromeOptions()
    option.add_experimental_option("detach", True)  # 不自动关闭浏览器
    option.add_argument('--window-size=1920,1080')
    option.add_argument('headless')
    driver = webdriver.Chrome(chrome_options=option)  # 添加option到chrome_option中
    return driver


def crawler_xpath(driver, url, elements, data):
    driver.get(url)
    for element in elements:
        WebDriverWait(driver, 5, 0.5).until(EC.presence_of_element_located((By.XPATH, element)),
                                            message="This element does not exist")
        driver.find_element(By.XPATH, element).send_keys(data[0])
        time.sleep(3)
        driver.find_element(By.XPATH, element).click()
        windows = driver.window_handles  # 获取打开的多个窗口句柄
        driver.switch_to.window(windows[-1])  # 去最后一个界面
