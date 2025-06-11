from lxml import html

from bs4 import BeautifulSoup

from tools.file_util import FileUtil


def _get_xpath(element):
    """生成元素的 XPath，优先考虑 id/name 属性"""
    if 'id' in element.attrib:
        return f"//{element.tag}[@id='{element.attrib['id']}']"
    if 'name' in element.attrib:
        return f"//{element.tag}[@name='{element.attrib['name']}']"

    components = []
    while element is not None:
        # 获取元素的标签名
        tag = element.tag
        # 获取元素的索引
        parent = element.getparent()
        if parent is not None:
            siblings = parent.findall(tag)
            index = siblings.index(element) + 1  # XPath 索引从 1 开始
            components.append(f"{tag}[{index}]")
        else:
            components.append(tag)  # 根元素没有父元素
        element = parent
    components.reverse()
    return '/' + '/'.join(components)


def _is_visible(element):
    """检查元素是否可见"""
    # 排除 script 和 style 标签
    if element.tag in ['script', 'style']:
        return False

    # 检查元素的 CSS 样式
    if 'style' in element.attrib:
        style = element.attrib['style']
        if 'display:none' in style or 'visibility:hidden' in style:
            return False

    # 检查元素是否有文本或其他可见内容
    if element.tag in ['img', 'button', 'input', 'textarea']:
        return True

    # 检查文本内容
    if element.text and element.text.strip():
        return True

    return False


class XpathUtil:
    def __init__(self):
        pass

    @classmethod
    def get_visible_elements_xpath_string(cls, html_content):
        # 使用 BeautifulSoup 解析 HTML
        soup = BeautifulSoup(html_content, 'html.parser')
        # 转换为 lxml 对象
        tree = html.fromstring(str(soup))

        # 存储可见元素的 XPath 和文本
        visible_elements = []

        # 遍历所有元素
        for element in tree.xpath('//*'):
            if _is_visible(element):
                # 获取元素的 XPath
                xpath = _get_xpath(element)
                # 获取元素的文本内容
                if element.tag == 'input':
                    # 对于 input 元素，获取 value 属性作为文本
                    text_content = element.attrib.get('value', '').strip()
                else:
                    # 对于其他元素，获取文本内容
                    text_content = element.text_content().strip() if element.text_content() else ''
                visible_elements.append(f"{xpath}, {text_content}")
        return ";".join(visible_elements)
