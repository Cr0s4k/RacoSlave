from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from configuration import Configuration
from pprint import pprint
import json

class Scrapper():
    def start():
        config = Configuration.read_configuration()

        browser = webdriver.Chrome("./chromedriver")
        browser.get("https://raco.fib.upc.edu/cas/login")

        username = browser.find_element_by_id("username")
        password = browser.find_element_by_id("password")

        username.send_keys(config["user"])
        password.send_keys(config["password"])

        browser.find_element_by_id("submit_button").click()
        browser.find_element_by_class_name("botons_form").find_element_by_tag_name("input").click();

        #SUBJECTS  
        main_div = browser.find_element_by_class_name("avisos")
        subjects = main_div.find_elements_by_css_selector("h4 > a")
        subjects = [i.text for i in subjects]

        #NOTICES
        unorderedLists = main_div.find_elements_by_css_selector("ul:not(.links_atenea)")
        notices = []
        for ul in unorderedLists:
            list_items = ul.find_elements_by_tag_name("li")
            notices.append([i.find_element_by_tag_name("a").text for i in list_items])

        #JOIN 
        output = []
        for i, subject in enumerate(subjects):
            item = {'subject': subject, 'notices': notices[i]}
            output.append(item)

        with open("result.json", "w") as file:
            json.dump(output, file, indent=4, ensure_ascii=False)

        browser.close()

if __name__ == "__main__":
    Scrapper.start()