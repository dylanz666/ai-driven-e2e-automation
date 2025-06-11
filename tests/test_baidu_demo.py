import base64
import json
import time

import pytest
import allure

from browsers.browser_factory import BrowserFactory
from constants.severity import Severity
from pages.base_page import BasePage
from tools.ai_core import AICore
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
        screenshot_path = "screenshots/baidu_home.png"
        self.base_page.take_screenshot(screenshot_path)
        page_source = self.base_page.get_page_source()
        xpath_data = XpathUtil.get_visible_elements_xpath_string(page_source)

        # AI driven to generate test case steps and conduct them
        with open(screenshot_path, 'rb') as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode()
        test_case_prompt = '你是一名十分专业的测试工程师。根据提供的网页，设计1个核心功能测试用例，用例可以有多个步骤，步骤中的 assertion 值要有显式的文字关联，element 和 assertion 的值使用纯中文，value 不使用图片中的文本，可随机使用网络上的新闻标题，action 值可以为 input 或者 click，action 为 click 时不提供 value，断言统一写在 assertion 字段，有 action 时不要有 assertion，最终以数组的格式返回，用例模板：[{"element":"xxx","action":"xxx","value":"xxxxx",“assertion”:"xxx"}]。禁止附带任何其他文本或文本格式。做得好有奖励！'
        print(test_case_prompt)
        messages = [{
            "role": "user",
            "content": [
                {"type": "image", "image": encoded_string},
            ]
        }, {
            "role": "user",
            "content": [
                {"type": "text",
                 "text": test_case_prompt}
            ]
        }]
        case_steps = AICore().ask_ai(messages)
        case_steps = json.loads(case_steps)
        print(case_steps)

        for index, case_step in enumerate(case_steps):
            print(f"用例步骤：{index + 1}", case_step)
            element_xpath = AIXpath.get_xpath(screenshot_path, xpath_data, case_step["element"])
            action = "" if "action" not in case_step else case_step["action"]
            value = "" if "value" not in case_step else case_step["value"]
            if action and value:
                eval(f'self.base_page.{action}(By.XPATH, "{element_xpath}", "{value}")')
            if action and not value:
                eval(f'self.base_page.{action}(By.XPATH, "{element_xpath}")')
            assertion = "" if "assertion" not in case_step else case_step["assertion"]
            if not assertion:
                continue
            assertion_screenshot_file_path = "screenshots/assertion_screenshot.png"
            self.base_page.take_screenshot(assertion_screenshot_file_path)
            with open(assertion_screenshot_file_path, 'rb') as image_file:
                encoded_string = base64.b64encode(image_file.read()).decode()
            assertion_prompt = f'你是一名十分专业的测试工程师。图片中展示的结果是否与描述："{assertion}"相符，有90%信心觉得相符则返回 success，否则返回 fail。禁止附带任何其他文本或文本格式。做得好有奖励！'
            print(assertion_prompt)
            assertion_messages = [{
                "role": "user",
                "content": [
                    {"type": "image", "image": encoded_string},
                ]
            }, {
                "role": "user",
                "content": [
                    {"type": "text",
                     "text": assertion_prompt}
                ]
            }]
            test_result = AICore().ask_ai(assertion_messages)
            assert test_result == "success", "测试失败！"
