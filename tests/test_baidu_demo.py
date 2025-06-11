import time

import pytest
import allure

from browsers.browser_factory import BrowserFactory
from constants.severity import Severity
from pages.base_page import BasePage
from tools.ai_assert_util import AIAssertUtil
from tools.ai_case_generator import AICaseGenerator
from tools.ai_xpath import AIXpath
from tools.decorators import screenshot_on_failure
from tools.xpath_util import XpathUtil
from selenium.webdriver.common.by import By


@allure.feature("Feature: Demo test baidu")
class TestBaidu:
    def setup_class(self):
        self.driver = BrowserFactory.create_browser().create_driver()
        self.base_page = BasePage(self.driver)

    def teardown_class(self):
        self.base_page.close()

    def setup_method(self):
        self.base_page.open_url("https://www.baidu.com")
        time.sleep(3)

    def teardown_method(self):
        pass

    @pytest.mark.P1
    @allure.severity(Severity.CRITICAL.value)
    @allure.title("Demo baidu")
    @allure.description("Demo baidu")
    @allure.testcase("https://platform/test/case?id=1245")
    @screenshot_on_failure
    # @pytest.mark.skip
    def test_baidu(self):
        # prepare basic info of test page
        screenshot_data = self.base_page.get_screenshot_as_base64()
        page_source = self.base_page.get_page_source()
        xpath_data = XpathUtil.get_visible_elements_xpath_string(page_source)

        # AI driven to generate test case steps and conduct them
        case_steps = AICaseGenerator.generate_test_case(screenshot_data)

        for index, case_step in enumerate(case_steps):
            print(f"用例步骤：{index + 1}", case_step)
            element = "" if "element" not in case_step else case_step["element"]
            action = "" if "action" not in case_step else case_step["action"]
            value = "" if "value" not in case_step else case_step["value"]
            assertion = "" if "assertion" not in case_step else case_step["assertion"]
            if not action and assertion:
                assertion_screenshot_data = self.base_page.get_screenshot_as_base64()
                test_result = AIAssertUtil.do_assert(assertion_screenshot_data, case_step["assertion"])
                assert test_result == "success", "测试失败！"
                continue
            if not action or not element:
                continue
            element_xpath = AIXpath.get_xpath(screenshot_data, xpath_data, element)
            if value:
                eval(f'self.base_page.{action}(By.XPATH, "{element_xpath}", "{value}")')
                continue
            eval(f'self.base_page.{action}(By.XPATH, "{element_xpath}")')
