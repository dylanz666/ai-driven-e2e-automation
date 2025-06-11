import json

from tools.ai_core import AICore


class AICaseGenerator:
    def __init__(self):
        pass

    @staticmethod
    def generate_test_case(screenshot_data):
        test_case_prompt = '你是一名十分专业的测试工程师。根据提供的网页，设计1个核心功能测试用例，用例可以有多个步骤，步骤中的 assertion 值要有显式的文字关联，element 和 assertion 的值使用纯中文，value 不使用图片中的文本，可随机使用网络上的新闻标题，action 值可以为 input 或者 click，action 为 click 时不提供 value，断言统一写在 assertion 字段，有 action 时不要有 assertion，最终以数组的格式返回，用例模板：[{"element":"xxx","action":"xxx","value":"xxxxx",“assertion”:"xxx"}]。禁止附带任何其他文本或文本格式。做得好有奖励！'
        print(test_case_prompt)
        messages = [{
            "role": "user",
            "content": [
                {"type": "image", "image": screenshot_data},
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
        return case_steps
