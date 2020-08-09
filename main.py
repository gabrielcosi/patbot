from selenium import webdriver
from time import sleep


class PatBot:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(
            executable_path='C:\webdrivers\chromedriver.exe', options=options)
        user = input("Ingresa tu usuario: ")
        pw = input("Ingresa tu contraseña: ")
        self.driver.get("https://patmos.upeu.edu.pe/upeu")
        self.driver.find_element_by_xpath(
            "//input[@name=\"usuario\"]").send_keys(user)
        self.driver.find_element_by_xpath(
            "//input[@name=\"password\"]").send_keys(pw)
        self.driver.find_element_by_xpath("//button[@type=\"submit\"]").click()
        sleep(2)
        self.driver.find_element_by_xpath(
            "//li/following::a[@href=\"/report/dashboardStudent\"]").click()
        sleep(5)
        self.driver.find_element_by_xpath(
            "//label[@for=\"customSwitch5\"]").click()
        sleep(2)

    def checkItems(self):
        table = self.driver.find_element_by_css_selector(
            "table.table")
        for row in table.find_elements_by_tag_name("tr"):
            self.driver.execute_script(
                "window.scrollTo(0,"+str(row.location['y'] - 200)+")")
            row.find_element_by_tag_name("td").click()
            sleep(1)
            self.driver.find_element_by_xpath(
                "//button[contains(text(), 'Cerrar')]").click()


my_bot = PatBot()
my_bot.checkItems()
