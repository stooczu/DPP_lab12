import unittest
import sys
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class TestSimple2(unittest.TestCase):
    from selenium import webdriver
    from selenium.webdriver.support.wait import WebDriverWait

    driver = 0

    def test1_ok(self):
        # create a new Firefox session
        global driver
        driver = webdriver.Firefox()
        driver.implicitly_wait(15)

    def test2_ok(self):
        driver.maximize_window()

    def test3_ok(self):
        # navigate to the application home page
        driver.get('http://automationpractice.com/index.php')
        self.assertTrue(True)

    def test4_ok(self):
        search_field = driver.find_element_by_name('search_query')
        search_field.clear()
        search_field.send_keys('t-shirt')
        search_field.submit()
        self.assertTrue(True)

    @unittest.skip("Test skip")
    def test5_ok(self):
        raise NotImplementedError

    @unittest.skip("Test skip")
    def test6_ok(self):
        raise NotImplementedError


    def test7_ok(self):
        driver.quit()


if __name__ == '__main__':
    unittest.main()
