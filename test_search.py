from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import unittest

from Pages.SearchPage import SearchPage
from Pages.ResultsPage import ResultsPage


class SearchTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()

    def test_defaultSearchButtonText(self):
        driver = self.driver
        search_page = SearchPage(driver)
        search_page.go_to_home_page()
        self.assertEqual("Google Search",
                         search_page.get_text_from_element_name(search_page.search_btn),
                         "The button should shows 'Google Search'")


    def test_enterSearchQueryGoesToResults(self):
        driver = self.driver
        search_page = SearchPage(driver)
        search_page.go_to_home_page()
        search_page.enter_search_query("SeleniumHq")
        search_page.click_search()
        results_page = ResultsPage(driver)
        results_page.wait_for_results()
        self.assertRegex(results_page.get_stats_from_results(),
                         "(.*)(results \\()(.*)(seconds)(\\))",
                         "Given search query, when you click search button, then it SHOULD display result stats ")



    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Search Tests Completed")


if __name__ == '__main__':
    unittest.main()