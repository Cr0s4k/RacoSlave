from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from configuration import Configuration

if __name__ == "__main__":
    config = Configuration.read_configuration()

    browser = webdriver.Chrome("./chromedriver")
    browser.get("https://raco.fib.upc.edu/cas/login")

    username = browser.find_element_by_id("username")
    password = browser.find_element_by_id("password")

    username.send_keys(config["user"])
    password.send_keys(config["password"])

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