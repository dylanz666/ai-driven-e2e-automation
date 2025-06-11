from tools.ai_core import AICore


class AIAssertUtil:
    def __init__(self):
        pass

    @staticmethod
    def do_assert(screenshot_data, assertion):
        assertion_prompt = f'你是一名十分专业的测试工程师。图片中展示的结果是否与描述："{assertion}"相符，有90%信心觉得相符则返回 success，否则返回 fail。禁止附带任何其他文本或文本格式。做得好有奖励！'
        print(assertion_prompt)
        assertion_messages = [{
            "role": "user",
            "content": [
                {"type": "image", "image": screenshot_data},
            ]
        }, {
            "role": "user",
            "content": [
                {"type": "text",
                 "text": assertion_prompt}
            ]
        }]
        return AICore().ask_ai(assertion_messages)
