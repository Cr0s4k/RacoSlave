from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json

def readCredentials():
    with open('credentials.json') as f:
        data = json.load(f)
        return (data["user"], data["password"])

if __name__ == "__main__":
    credentials = readCredentials();

    browser = webdriver.Chrome("./chromedriver")
    browser.get("https://raco.fib.upc.edu/cas/login")

    username = browser.find_element_by_id("username")
    password = browser.find_element_by_id("password")

    username.send_keys(credentials[0])
    password.send_keys(credentials[1])

    browser.find_element_by_id("submit_button").click()

    browser.get("https://raco.fib.upc.edu/home/assignatura?espai=270019")
    avisos = browser.find_element_by_xpath("//*[@class='text avisos']")
    avisos = avisos.find_element_by_tag_name("ul")
    lis = avisos.find_elements_by_tag_name("li")

    '''for li in lis:
        try:
            a = li.find_element_by_tag_name("a")
            print(a.text)
        except Exception as e:
            print(e)
            pass

    '''

    firstLi = lis[0].find_element_by_tag_name("a")
    print(firstLi.text)
    browser.close()