from pages.base_page import *
from pages.Drivers import *
import pytest
from Objects.object_properties import Element
import time


class TestLogin:

    @pytest.fixture()
    def setup(self):
        self.driver = drivers("chrome")
        self.bp = BasePage(self.driver)
        self.ele = Element()


    @pytest.mark.parametrize('tcid',["1"])
    def test_open_url(self, setup, tcid):
        self.bp.open_browser("https://www.tesla.com")
        time.sleep(2)
        # self.driver.find_element(object_properties.visit_button).click()
        # self.driver.find_element_by_class_name("tds-o-btn_group--item").click()
        self.driver.find_element_by_name(self.ele.order_now).click()

    def teardown(self):
        self.driver.close()
        self.driver.quit()
