from selenium import webdriver
from selenium.webdriver.common.by import By
import time
link = "http://selenium1py.pythonanywhere.com/"


class TestMainPage1():

    @classmethod #декоратор, использованный для удобства чтения кода. Так мы дополнительно размечаем в коде, что метод ниже (в нашем примере с *_class) применяется ко всему классу
    def setup_class(self): #выполняется один раз перед запуском всех тестовых методов в классе
        print("\nstart browser for test suite 1..")
        self.browser = webdriver.Chrome()

    @classmethod
    def teardown_class(self): #выполняется один раз после всех тестовых методов в классе
        print("quit browser for test suite 1..")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        print('start test link 1')
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        #time.sleep(2)

    def test_guest_should_see_basket_link_on_the_main_page(self):
        print('start test basket 1')
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
        #time.sleep(2)


class TestMainPage2():

    def setup_method(self): #выполняется перед запуском каждого тестового метода в классе
        print("start browser for test 2..")
        self.browser = webdriver.Chrome()

    def teardown_method(self): #выполняется каждый раз после каждого тестового метода в классе
        print("quit browser for test 2..")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        print('start test link 2')
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        #time.sleep(10)

    def test_guest_should_see_basket_link_on_the_main_page(self):
        print('start test basket 2')
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
        #time.sleep(10)
