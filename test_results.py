from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import unittest

from Pages.ResultsPage import ResultsPage


class ResultsTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()

    def test_enterSearchQueryStaysInResults(self):
        driver = self.driver
        results_page = ResultsPage(driver)
        results_page.go_to_results_page_for_query("SeleniumHq")
        results_page.wait_for_results()
        results_page.click_the_seleniumhq_link()
        self.assertEqual("Selenium IDE",
                         "Selenium IDE", "assertion done"
                         )




    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Search Results Tests Completed")


if __name__ == '__main__':
    unittest.main()
