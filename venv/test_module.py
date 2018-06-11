import unittest
import sys
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

class TestSimple(unittest.TestCase):

    from selenium import webdriver
    from selenium.webdriver.support.wait import WebDriverWait

    driver = 0
    start = 0
    elapsed = 0

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
        search_field.send_keys('dress')
        search_field.submit()
        self.assertTrue(True)

    def test5_ok(self):
        WebDriverWait(driver, 15).until(lambda d: d.find_element_by_class_name('heading-counter'))

        counter = driver.find_element_by_class_name('product-count')
        counter = counter.text
        # get the number of anchor elements found
        self.assertEqual(str(8), counter[12])

    def test6_ok(self):
        # close the browser window
        driver.quit()
        self.assertTrue(True)

    #def test_fail(self):
    #    baz = False
    #    self.assertTrue(baz)

    #def test_raise(self):
    #    raise RuntimeError

    #@unittest.skip("Test skip")
    #def test_skip(self):
    #    raise NotImplementedError

if __name__ == '__main__':
    unittest.main()