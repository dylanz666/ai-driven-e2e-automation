import base64

from tools.ai_core import AICore


class AIXpath:

    @staticmethod
    def get_xpath(screenshot_path, xpath_data, element_clue):
        messages = []
        with open(screenshot_path, 'rb') as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode()
        messages.append({
            "role": "user",
            "content": [
                {"type": "image", "image": encoded_string},
            ]
        })

        messages.append({
            "role": "user",
            "content": [
                {"type": "text", "text": xpath_data},
                {"type": "text",
                 "text": f"你是一个专业的设计师和测试工程师，根据提供的数据，'{element_clue}'最有可能是哪个 xpath，仅直接提供 xpath 结果。禁止附带任何其他文本或文本格式。做得好有奖励！"},
            ]
        })
        return AICore().ask_ai(messages)


if __name__ == "__main__":
    screenshot_path = "../screenshots/baidu.png"
    xpath_data = """
    XPath: /html/head[1]/title[1], 文本: '百度一下，你就知道'
    XPath: /html/body[1]/div[1]/div[1]/div[2]/a[1], 文本: '百度首页'
    XPath: //a[@name='tj_settingicon'], 文本: '设置'
    XPath: //a[@name='tj_login'], 文本: '登录'
    XPath: /html/body[1]/div[1]/div[1]/div[3]/a[1], 文本: '新闻'
    XPath: /html/body[1]/div[1]/div[1]/div[3]/a[2], 文本: 'hao123'
    XPath: /html/body[1]/div[1]/div[1]/div[3]/a[3], 文本: '地图'
    XPath: /html/body[1]/div[1]/div[1]/div[3]/a[4], 文本: '贴吧'
    XPath: /html/body[1]/div[1]/div[1]/div[3]/a[5], 文本: '视频'
    XPath: /html/body[1]/div[1]/div[1]/div[3]/a[6], 文本: '图片'
    XPath: /html/body[1]/div[1]/div[1]/div[3]/a[7], 文本: '网盘'
    XPath: /html/body[1]/div[1]/div[1]/div[3]/a[8], 文本: '文库'
    XPath: /html/body[1]/div[1]/div[1]/div[3]/a[9]/img[1], 文本: ''
    XPath: //a[@name='tj_briicon'], 文本: '更多'
    XPath: /html/body[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/a[1]/img[1], 文本: ''
    XPath: /html/body[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/a[1]/div[1], 文本: '翻译'
    XPath: /html/body[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/a[1]/img[1], 文本: ''
    XPath: /html/body[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/a[1]/div[1], 文本: '学术'
    XPath: /html/body[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[3]/a[1]/img[1], 文本: ''
    XPath: /html/body[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[3]/a[1]/div[1], 文本: '百科'
    XPath: /html/body[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[4]/a[1]/img[1], 文本: ''
    XPath: /html/body[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[4]/a[1]/div[1], 文本: '知道'
    XPath: /html/body[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[5]/a[1]/img[1], 文本: ''
    XPath: /html/body[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[5]/a[1]/div[1], 文本: '健康'
    XPath: /html/body[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[6]/a[1]/img[1], 文本: ''
    XPath: /html/body[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[6]/a[1]/div[1], 文本: '营销推广'
    XPath: /html/body[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[7]/a[1]/img[1], 文本: ''
    XPath: /html/body[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[7]/a[1]/div[1], 文本: '直播'
    XPath: /html/body[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[8]/a[1]/img[1], 文本: ''
    XPath: /html/body[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[8]/a[1]/div[1], 文本: '音乐'
    XPath: /html/body[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[9]/a[1]/img[1], 文本: ''
    XPath: /html/body[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[9]/a[1]/div[1], 文本: '橙篇'
    XPath: //a[@name='tj_more'], 文本: '查看全部百度产品 >'
    XPath: //span[@id='s-usersetting-top'], 文本: '设置'
    XPath: //a[@id='s-top-loginbtn'], 文本: '登录'
    XPath: /html/body[1]/div[1]/div[1]/div[4]/div[1]/a[1], 文本: '关闭热搜'
    XPath: /html/body[1]/div[1]/div[1]/div[4]/div[1]/a[2], 文本: '开启热搜'
    XPath: /html/body[1]/div[1]/div[1]/div[4]/div[2]/i[1], 文本: ''
    XPath: /html/body[1]/div[1]/div[1]/div[4]/div[2]/span[1], 文本: '牛年贺岁，登录设置新春皮肤！'
    XPath: /html/body[1]/div[1]/div[1]/div[4]/div[2]/i[2], 文本: ''
    XPath: //div[@id='ent_sug'], 文本: '请按“回车”键发起检索'
    XPath: //img[@id='s_lg_img'], 文本: ''
    XPath: //img[@id='s_lg_img_new'], 文本: ''
    XPath: //img[@id='s_lg_img_aging'], 文本: ''
    XPath: /html/body[1]/div[1]/div[1]/div[5]/div[2]/div[1]/a[1]/img[1], 文本: ''
    XPath: /html/body[1]/div[1]/div[1]/div[5]/div[2]/div[1]/a[1]/img[2], 文本: ''
    XPath: /html/body[1]/div[1]/div[1]/div[5]/div[2]/div[1]/a[1]/img[3], 文本: ''
    XPath: /html/body[1]/div[1]/div[1]/div[5]/div[2]/div[1]/form[1]/div[1]/ul[1]/li[1], 文本: '天气预报15天查询'
    XPath: /html/body[1]/div[1]/div[1]/div[5]/div[2]/div[1]/form[1]/div[1]/ul[1]/li[1]/b[1], 文本: '15天查询'
    XPath: /html/body[1]/div[1]/div[1]/div[5]/div[2]/div[1]/form[1]/div[1]/ul[1]/li[2], 文本: '天气预报30天查询'
    XPath: /html/body[1]/div[1]/div[1]/div[5]/div[2]/div[1]/form[1]/div[1]/ul[1]/li[2]/b[1], 文本: '30天查询'
    XPath: /html/body[1]/div[1]/div[1]/div[5]/div[2]/div[1]/form[1]/div[1]/ul[1]/li[3], 文本: '天气预报全天'
    XPath: /html/body[1]/div[1]/div[1]/div[5]/div[2]/div[1]/form[1]/div[1]/ul[1]/li[3]/b[1], 文本: '全天'
    XPath: /html/body[1]/div[1]/div[1]/div[5]/div[2]/div[1]/form[1]/div[1]/ul[1]/li[4], 文本: '天气预报一周天气'
    XPath: /html/body[1]/div[1]/div[1]/div[5]/div[2]/div[1]/form[1]/div[1]/ul[1]/li[4]/b[1], 文本: '一周天气'
    XPath: /html/body[1]/div[1]/div[1]/div[5]/div[2]/div[1]/form[1]/div[1]/ul[1]/li[5], 文本: '天气预报24小时实时查询'
    XPath: /html/body[1]/div[1]/div[1]/div[5]/div[2]/div[1]/form[1]/div[1]/ul[1]/li[5]/b[1], 文本: '24小时实时查询'
    XPath: /html/body[1]/div[1]/div[1]/div[5]/div[2]/div[1]/form[1]/div[1]/ul[1]/li[6], 文本: '天气预报本地'
    XPath: /html/body[1]/div[1]/div[1]/div[5]/div[2]/div[1]/form[1]/div[1]/ul[1]/li[6]/b[1], 文本: '本地'
    XPath: /html/body[1]/div[1]/div[1]/div[5]/div[2]/div[1]/form[1]/div[1]/ul[1]/li[7], 文本: '天气预报下载安装'
    XPath: /html/body[1]/div[1]/div[1]/div[5]/div[2]/div[1]/form[1]/div[1]/ul[1]/li[7]/b[1], 文本: '下载安装'
    XPath: /html/body[1]/div[1]/div[1]/div[5]/div[2]/div[1]/form[1]/div[1]/ul[1]/li[8], 文本: '天气预报杭州'
    XPath: /html/body[1]/div[1]/div[1]/div[5]/div[2]/div[1]/form[1]/div[1]/ul[1]/li[8]/b[1], 文本: '杭州'
    XPath: /html/body[1]/div[1]/div[1]/div[5]/div[2]/div[1]/form[1]/div[1]/ul[1]/li[9], 文本: '天气预报哪个软件最准确'
    XPath: /html/body[1]/div[1]/div[1]/div[5]/div[2]/div[1]/form[1]/div[1]/ul[1]/li[9]/b[1], 文本: '哪个软件最准确'
    XPath: /html/body[1]/div[1]/div[1]/div[5]/div[2]/div[1]/form[1]/div[1]/ul[1]/li[10], 文本: '天气预报符号'
    XPath: /html/body[1]/div[1]/div[1]/div[5]/div[2]/div[1]/form[1]/div[1]/ul[1]/li[10]/b[1], 文本: '符号'
    XPath: /html/body[1]/div[1]/div[1]/div[5]/div[2]/div[1]/form[1]/div[1]/ul[1]/li[11], 文本: '天气预报15天查询DeepSeek-R1'
    XPath: /html/body[1]/div[1]/div[1]/div[5]/div[2]/div[1]/form[1]/div[1]/ul[1]/li[11]/b[1], 文本: '15天查询'
    XPath: /html/body[1]/div[1]/div[1]/div[5]/div[2]/div[1]/form[1]/div[1]/ul[1]/li[11]/div[1]/img[1], 文本: ''
    XPath: //span[@id='bdsug-ai-text'], 文本: 'DeepSeek-R1'
    XPath: /html/body[1]/div[1]/div[1]/div[5]/div[2]/div[1]/form[1]/div[1]/div[1]/span[1], 文本: '反馈'
    XPath: //input[@name='ie'], 文本: 'utf-8'
    XPath: //input[@name='f'], 文本: '8'
    XPath: //input[@name='rsv_bp'], 文本: '1'
    XPath: //input[@name='rsv_idx'], 文本: '1'
    XPath: //input[@name='ch'], 文本: ''
    XPath: //input[@name='tn'], 文本: 'baidu'
    XPath: //input[@name='bar'], 文本: ''
    XPath: //input[@id='kw'], 文本: ''
    XPath: /html/body[1]/div[1]/div[1]/div[5]/div[2]/div[1]/form[1]/span[1]/i[1], 文本: ''
    XPath: /html/body[1]/div[1]/div[1]/div[5]/div[2]/div[1]/form[1]/span[1]/span[2], 文本: '按图片搜索'
    XPath: //input[@id='su'], 文本: '百度一下'
    XPath: /html/body[1]/div[1]/div[1]/div[5]/div[2]/div[1]/form[1]/span[3]/span[1]/div[1]/span[1], 文本: '输入法'
    XPath: //a[@name='ime_hw'], 文本: '手写'
    XPath: //a[@name='ime_py'], 文本: '拼音'
    XPath: //a[@name='ime_cl'], 文本: '关闭'
    XPath: //input[@name='rn'], 文本: ''
    XPath: //input[@name='fenlei'], 文本: '256'
    XPath: //input[@name='oq'], 文本: ''
    XPath: //input[@name='rsv_pq'], 文本: '0xb362b3ff0027927d'
    XPath: //input[@name='rsv_t'], 文本: '880dH6fHRg2KqtIB79Lw7cPJYfKiLShXFbLhws7XGs1gYRbBzi6aHVmHb+PX'
    XPath: //input[@name='rqlang'], 文本: 'en'
    XPath: //input[@name='rsv_dl'], 文本: 'ib'
    XPath: //input[@name='rsv_enter'], 文本: '1'
    XPath: //input[@name='rsv_sug3'], 文本: '4'
    XPath: //input[@name='rsv_sug1'], 文本: '1'
    XPath: //input[@name='rsv_sug7'], 文本: '100'
    XPath: /html/body[1]/div[1]/div[1]/div[5]/div[2]/div[1]/div[2]/div[1]/a[1]/div[2], 文本: 'AI搜索已支持DeepSeek R1最新版'
    XPath: /html/body[1]/div[1]/div[1]/div[5]/div[2]/div[1]/div[2]/div[1]/a[1]/div[3], 文本: '立即体验'
    XPath: /html/body[1]/div[1]/div[1]/div[7]/div[1]/p[1]/a[1], 文本: '关于百度'
    XPath: /html/body[1]/div[1]/div[1]/div[7]/div[1]/p[2]/a[1], 文本: 'About Baidu'
    XPath: /html/body[1]/div[1]/div[1]/div[7]/div[1]/p[3]/a[1], 文本: '使用百度前必读'
    XPath: /html/body[1]/div[1]/div[1]/div[7]/div[1]/p[4]/a[1], 文本: '帮助中心'
    XPath: /html/body[1]/div[1]/div[1]/div[7]/div[1]/p[5]/a[1], 文本: '企业推广'
    XPath: /html/body[1]/div[1]/div[1]/div[7]/div[1]/p[6]/a[1], 文本: '京公网安备11000002000001号'
    XPath: /html/body[1]/div[1]/div[1]/div[7]/div[1]/p[7]/a[1], 文本: '京ICP证030173号'
    XPath: /html/body[1]/div[1]/div[1]/div[7]/div[1]/p[8]/span[1], 文本: '互联网新闻信息服务许可证11220180008'
    XPath: /html/body[1]/div[1]/div[1]/div[7]/div[1]/p[9]/span[1], 文本: '网络文化经营许可证： 京网文〔2023〕1034-029号'
    XPath: /html/body[1]/div[1]/div[1]/div[7]/div[1]/p[10]/a[1], 文本: '信息网络传播视听节目许可证 0110516'
    XPath: /html/body[1]/div[1]/div[1]/div[7]/div[1]/p[11]/span[1], 文本: '互联网宗教信息服务许可证编号：京（2022）0000043'
    XPath: /html/body[1]/div[1]/div[1]/div[7]/div[1]/p[12]/span[1], 文本: '药品医疗器械网络信息服务备案（京）网药械信息备字（2021）第00159号'
    XPath: /html/body[1]/div[1]/div[1]/div[7]/div[1]/p[13]/span[1], 文本: '医疗器械网络交易服务第三方平台备案凭证（京）网械平台备字（2020）第00002号'
    XPath: /html/body[1]/div[1]/div[1]/div[7]/div[1]/p[14]/span[1], 文本: '药品网络交易服务第三方平台备案凭证（京）网药平台备字〔2023〕第000002号'
    XPath: /html/body[1]/div[1]/div[1]/div[7]/div[1]/p[15]/span[1], 文本: '©2025 Baidu'
    XPath: /html/body[1]/div[1]/div[2]/div[1]/b[1], 文本: '网页'
    XPath: /html/body[1]/div[1]/div[2]/div[1]/a[1]/img[1], 文本: ''
    XPath: /html/body[1]/div[1]/div[2]/div[1]/a[2], 文本: '图片'
    XPath: /html/body[1]/div[1]/div[2]/div[1]/a[3], 文本: '资讯'
    XPath: /html/body[1]/div[1]/div[2]/div[1]/a[4], 文本: '视频'
    XPath: /html/body[1]/div[1]/div[2]/div[1]/a[5], 文本: '笔记'
    XPath: /html/body[1]/div[1]/div[2]/div[1]/a[6], 文本: '地图'
    XPath: /html/body[1]/div[1]/div[2]/div[1]/a[7], 文本: '贴吧'
    XPath: /html/body[1]/div[1]/div[2]/div[1]/a[8], 文本: '文库'
    XPath: /html/body[1]/div[1]/div[2]/div[1]/a[9], 文本: '更多'
    """
    # AIXpath.get_xpath(screenshot_path, xpath_data, "搜索文本框")
    AIXpath.get_xpath(screenshot_path, xpath_data, "百度一下按钮")
