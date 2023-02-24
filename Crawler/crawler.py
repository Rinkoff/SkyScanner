##Import Packages
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

#URL of the webpage that we are scraping information from
BASE_URL="https://www.esky.bg/oferti/co/bg/0/0/balgariya"


class Crawler:
    def __init__(self,url):
        self.url=url

        self.driver=webdriver.Chrome()

    def take_information(self):  #This method takes all the information elements and appends them to the info list.

        self.info=[]

        #Take all Information divs
        divs=self.driver.find_elements(By.CLASS_NAME,"deal-group")

        #We loop through the found elements, and for each of them, we find all the elements with the tag name li.
        for div in divs:
            ul=div.find_elements(By.TAG_NAME,"li")
            for li in ul:
                arrival_country=li.find_element(By.CLASS_NAME,"arrival-country").text
                arrival_city=li.find_element(By.CLASS_NAME,"arrival-city").text
                price_amount=li.find_element(By.CLASS_NAME,"price-amount").text
                self.info.append([arrival_country,arrival_city,price_amount])


    def get_html(self):
        #Driver takes URL
        self.driver.get(self.url)

        #Allow All Coockies
        btnCookies = self.driver.find_element(By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll").click()

        #Open All Deals
        btnMoreDeals=self.driver.find_element(By.CSS_SELECTOR, ".show-more-deals").click()

        # Scroll to the bottom
        for _ in range(50):
            self.driver.execute_script("window.scrollBy(0,250)","")
            time.sleep(0.1)

        self.take_information()

    def start(self):    #This method starts the scraping process.
        self.crawling=self.get_html()

    def stop(self):     #This method stops the scraping process.
        self.driver.quit()






if __name__ == '__main__':
    crawler = Crawler(BASE_URL)

    crawler.start()
    crawler.stop()