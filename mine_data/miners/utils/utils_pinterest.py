from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.keys import Keys

import time,socket,unicodedata
import copy

def u_to_s(uni):
    return unicodedata.normalize('NFKD',uni).encode('ascii','ignore')

class Pinterest_Helper(object):
    
    def __init__(self, login, pw, browser = None):
        if browser is None:
            #http://tarunlalwani.com/post/selenium-disable-image-loading-different-browsers/
            profile = webdriver.FirefoxProfile()
            profile.set_preference("permissions.default.image", 2)
            self.browser = webdriver.Firefox(firefox_profile=profile)
        else:
            self.browser = browser
        self.browser.get("https://www.pinterest.com")

        #This want is the part that I modify for new version of piterest
        self.browser.find_element_by_css_selector('[data-test-id="simple-login-button"]').click()
        time.sleep(1)
        emailElem = self.browser.find_element_by_id('email')
        emailElem.send_keys(login)
        passwordElem = self.browser.find_element_by_id('password')
        passwordElem.send_keys(pw)
        passwordElem.send_keys(Keys.RETURN)
        time.sleep(10)

    def runme(self,url, threshold = 500, persistence = 120, debug = False):
        final_results = []
        previmages = []
        tries = 0
        print(url)
        try:
            self.browser.get(url)
            while threshold > 0:
                try:
                    results = []
                    images = self.browser.find_elements_by_tag_name("img")
                    if images == previmages:
                        tries += 1
                    else:
                        tries = 0
                    if tries > persistence:
                        if debug == True:
                            print("Exitting: persistence exceeded")
                        return final_results
                
                    for i in images:
                        src = i.get_attribute("src")
                        if src:
                            if src.find("/236x/") != -1:
                                src = src.replace("/236x/","/736x/")
                                results.append(u_to_s(src))
                    previmages = copy.copy(images)
                    final_results = list(set(final_results + results))
                    dummy = self.browser.find_element_by_tag_name('a')
                    dummy.send_keys(Keys.PAGE_DOWN)
                    time.sleep(2)
                    threshold -= 1

                except (StaleElementReferenceException):
                    if debug == True:
                        print("StaleElementReferenceException")
                    threshold -= 1

        except (socket.error, socket.timeout):
            if debug == True:
                print("Socket Error")
        except KeyboardInterrupt:
            return final_results
        
        if debug == True:
            print("Exitting at end")
        return final_results

    
    def close(self):
        self.browser.close()

"""
This code is take from https://github.com/xjdeng/pinterest-image-scraper, and I did some modifications for combine with this project.
"""