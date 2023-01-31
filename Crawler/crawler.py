##Import Packages

from selenium import webdriver
from selenium.webdriver.common.by import By



BASE_URL="https://www.esky.bg/oferti/co/bg/0/0/balgariya"


class Crawler:
    def __init__(self,url):
        self.url=url

        self.driver=webdriver.Chrome()

    def take_headwords(self):
        pass

    def get_html(self):
        #Driver takes URL
        self.driver.get(self.url)

        #Allow All Coockies
        btnCookies = self.driver.find_element(By.CSS_SELECTOR, "button.css-47sehv span").click()

        #Open All Deals
        btnMoreDeals=self.driver.find_element(By.CSS_SELECTOR, ".show-more-deals").click()




    def start(self):
        pass

    def stop(self):
        pass






if __name__ == '__main__':
    crawler = Crawler(BASE_URL)

    crawler.start()
    crawler.stop()