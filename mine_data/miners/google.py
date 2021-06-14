from miner import Miner
from selenium import webdriver
import time

from miners.utils.dirs_tools import generate_paths


class MinerGoogle(Miner):
    """
    This code works on Jun 1 2021, in case of change the labels or another name of classes in the tag, please, don't say that my code is sucks.

    """
    SERVICE = "google"
    def __init__(self,env):
        super().__init__(env)
        self.find = env["class"]["name"]
        self.images = env["class"]["numberOfImages"]
        
        self.url = f'https://www.google.co.in/search?q={self.find}&source=lnms&tbm=isch'

        self.save_path = generate_paths(
            env["pathSaved"],
            self.SERVICE,
            self.find
        )

    def start_mining(self):
        
        browser = webdriver.Firefox()
        browser.get(self.url)
        counter = 0
        succounter = 0

        for _ in range(self.images):
            browser.execute_script("window.scrollBy(0,10000)")

        time.sleep(1)

        for x in browser.find_elements_by_css_selector('[class="isv-r PNCib MSM1fd BUooTd"]'):
            counter = counter + 1
            x.click()
            time.sleep(2)
            
            imgSRC = browser.find_element_by_css_selector('[class="T1diZc KWE8qe"]').find_element_by_class_name("mJxzWe")

            try:
                src = imgSRC.find_element_by_id("islsp").find_element_by_id("Sva75c").find_element_by_class_name("A8mJGd").find_element_by_class_name("dFMRD")

                image = src.find_element_by_class_name("pxAole").find_element_by_css_selector('[class="tvh9oe BIB1wf"]').find_element_by_css_selector('[jsname="HiaYvf"]').get_attribute("src")
            
                self.download(image,save_dir=self.save_path)

                succounter = succounter + 1
                buttonClose = src.find_element_by_css_selector('[jsname="cQqtVb"]').find_element_by_css_selector('[jsname="tqp7ud"]')
                
                buttonClose.click()
                time.sleep(2)
                
            except Exception as e:
                print("can't get img: ",e)
                continue

        print(succounter, " Pictures succesfully downloaded")    