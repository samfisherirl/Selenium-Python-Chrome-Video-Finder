from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import collections
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(ChromeDriverManager().install())


class Browser:
    def __init__(self, url, keyword):
        self.url = url
        self.keyword = keyword

    def navigate(b):
        driver.get(b.url)
        return driver

    def getlinks(a):
        lnks = driver.find_elements_by_tag_name("a")
        arrays = []
        for lnk in lnks:
            # get_attribute() to get all href
            if a.keyword in lnk.get_attribute("href"):
                arrays.append(lnk.get_attribute("href"))  # remove duplicate
        array = [item for item, count in collections.Counter(arrays).items() if count > 1]
        return array

    def login(self):
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "login"))
            )
        finally:
            time.sleep(0.5)
            element = driver.find_element(By.NAME, "login")
            element.send_keys("samfisherirl")
            element = driver.find_element(By.NAME, "haslo")
            element.send_keys("321eagle")
            element = driver.find_element(By.NAME, "Submit")
            element.click()

    @staticmethod
    def looper(ar):
        links = []
        for i in ar:
            v = Browser(i, ".mp4")
            v.navigate()
            element = driver.find_element(By.CLASS_NAME, "uvmspn7")
            element.click()
            p = ["2160", "1440", "1080"]
            time.sleep(0.5)
            lnks = driver.find_elements_by_tag_name("a")
            x = 0
            for lnk in reversed(lnks):
                if x:
                    break
                arrays = []
                if "mp4" in lnk.get_attribute("href"):
                    arrays.append(lnk.get_attribute("href"))
                for i in arrays:
                    if x:
                        break
                    for pix in p:
                        if pix in i:
                            links.append(i)
                            x = 1
                            break
        print(links)


# identify elements with tagname <a>
# traverse list
pw = Browser("https://www.vimeo.com/login/", "")
pw.navigate()
pw.login()
vr = Browser("https://www.vimeo.com/cat/vr/", "video-")
vr.navigate()
array = vr.getlinks()
vr.looper(array)

driver.quit()
