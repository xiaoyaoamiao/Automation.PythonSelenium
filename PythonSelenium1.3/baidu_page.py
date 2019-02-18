class BaiDuPage(object):

    def __init__(self, context):
        self.d = context.driver

    def access_baidu(self):
        self.d.get("http://www.baidu.com")

    def input_value(self, value):
        searchField = self.d.find_element_by_id("kw")
        searchField.clear()
        searchField.send_keys(value)

    def click_search_btn(self):
        self.d.find_element_by_id("su").click()