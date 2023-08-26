import time
from appium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LaunchPage():
    def __init__(self, driver):
        self.driver = driver

    def Navigate_to_the_URL(self):
        self.driver.get('https://spark.8thwall.app/electrolux-universaldose/')
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "com.android.chrome:id/signin_fre_dismiss_button"))).click()

        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "com.android.chrome:id/negative_button"))).click()
        except:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "com.android.chrome:id/ack_button"))).click()

    def Permissions_interaction(self):
        # cookie permission
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//android.widget.Button[@text='Autoriser']"))).click()

        # Allow permission
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//android.widget.Button[@text='Allow']"))).click()

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//android.widget.Button[@text='While using the app']"))).click()

        # site permission
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View[3]/android.widget.Button"))).click()

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//android.widget.Image[@text='target-brx7nmia36']"))).click()
        time.sleep(40)

    def Exprience(self):
            time.sleep(3)
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//android.widget.Image[@text='icon_subtitles-dif91f04l7']"))).click()
            time.sleep(2)
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH,
                                              "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View/android.view.View[1]"))).click()
            time.sleep(10)
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//android.widget.Image[@text='icon_burger_menu-s1hjgu57gc']"))).click()
            time.sleep(5)
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//android.widget.TextView[@text='Soin du linge']"))).click()
            time.sleep(5)
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//android.widget.Image[@text='icon_burger_menu-s1hjgu57gc']"))).click()
            time.sleep(5)
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//android.widget.TextView[@text='Gain de temps']"))).click()
            time.sleep(5)
            WebDriverWait(self.driver,10).until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//android.view.View[@resource-id='relocateButton']"))).click()
            time.sleep(10)

