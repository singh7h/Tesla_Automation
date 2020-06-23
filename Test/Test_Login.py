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
        model_s = self.driver.find_element_by_link_text(Element.modelS_link)
        self.bp.click_button(model_s)
        time.sleep(2)

    def teardown(self):
        self.driver.close()
        self.driver.quit()
