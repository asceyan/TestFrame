import time
from common.com_nblog import use_logger
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from pykeyboard import PyKeyboard   # 模拟全局（系统级）键盘
from pymouse import PyMouse         # 模拟全局（系统级）鼠标
from random import choice
from selenium import webdriver
from config.config import SCREENSHOTS_PATH
logger = use_logger("BasePage")


class LocatorTypeError(Exception):
    pass


class ElementNotFound(Exception):
    pass


"""
    基于原生的selenium做二次封装
"""


class BasePage(object):

    def __init__(self,driver:webdriver.Chrome, timeout=10,t=1):
        """
        :param driver: 打开浏览器驱动
        :param timeout: 等待超时时间上限
        :param t: 检测的轮询周期
        """
        self.driver = driver
        self.timeout = timeout
        self.t = t

    def find(self, loc:tuple):
        """
        定位到元素，返回元素对象，没定位到，Timeout异常
        :param locator: ('loc','value1') ，loc:id,name,xpath,cssSelector，tagName,className,linkText,partialLinkText
        :return: ele
        """
        if not isinstance(loc, tuple):  # isinstance判断对象locator是否为tuple类型，返回布尔值
            logger.error("参数类型错误，locator必须是元祖类型,你输入的locator类型为%s"%type(loc))
            raise LocatorTypeError("参数类型错误，locator必须是元祖类型：loc = ('id','value1')")
        else:
            print("正在定位元素信息：定位方式->%s,value值->%s" % (loc[0], loc[1]))
            logger.info("正在定位元素信息：定位方式->%s,value值->%s" % (loc[0], loc[1]))
            try:
                # WebDriverWait 详解：https://blog.csdn.net/sinat_41774836/article/details/88965281
                ele = WebDriverWait(self.driver, self.timeout,self.t ).until(EC.presence_of_element_located(loc))
            except TimeoutException as msg:
                logger.error("定位元素出现超时,请检查你的定位方式:%s"%msg)
                raise NoSuchElementException("定位元素出现超时,请检查你的定位方式:%s"%msg)
            return ele

    def finds(self, locator):
        """复数定位，返回elements对象 list"""
        if not isinstance(locator, tuple):
            logger.error("参数类型错误，locator必须是元祖类型,你输入的locator类型为%s"%type(locator))
            raise LocatorTypeError("参数类型错误，locator必须是元祖类型：loc = ('id','value1')")
        else:
            print("正在定位元素信息：定位方式->%s,value值->%s" % (locator[0], locator[1]))
            logger.info("正在定位元素信息：定位方式->%s,value值->%s" % (locator[0], locator[1]))
            eles = WebDriverWait(self.driver, self.timeout,self.t ).until(EC.presence_of_all_elements_located(locator))
            return eles

    def send(self, locator:tuple, text=''):
        """发送文本"""
        ele = self.find(locator)
        ele.clear()
        try:
            ele.send_keys(text)
            logger.info("选择元素->{0} , 输入文本->\'{1}\' ..." .format(locator,text))
            print("选择元素->{0} , 输入文本->\'{1}\' ..." .format(locator,text))
        except NameError as e:
            logger.error("输入文本操作失败 %s" % e)

    def click(self, locator):
        """点击元素"""
        ele = self.find(locator)
        try:
            ele.click()
            logger.info("选择并点击元素->{0} ..." .format(locator))
            print("选择并点击元素->{0} ...".format(locator))
        except NameError as e:
            logger.error("Failed to click the element with %s" % e)

    def clear(self, locator):
        """清空输入框文本"""
        ele = self.find(locator)
        try:
            ele.clear()
            logger.info("选择元素->{0}，清除文本框!!!".format(locator))
        except NameError as e:
            logger.error("Failed to clear in input box with %s" % e)

    def is_selected(self, locator):
        """判断元素是否被选中，返回bool值"""
        ele = self.find(locator)
        r = ele.is_selected()
        return r

    def is_element_exist(self, locator):
        """判断元素是否存在，返回bool值"""
        try:
            self.find(locator)
            return True
        except:
            return False

    def is_title(self, title=''):
        """判断页面title，返回bool值"""
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_is(title))
            return result
        except:
            return False

    def is_title_contains(self, title=''):
        """判断页面title"""
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_contains(title))
            return result
        except:
            return False

    def is_text_in_element(self, locator, text=''):
        """判断元素中text值，返回bool值"""
        if not isinstance(locator, tuple):
            raise LocatorTypeError("参数类型错误，locator必须是元祖类型：loc = ('id','value1')")
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.text_to_be_present_in_element(locator, text))
            return result
        except:
            return False

    def is_value_in_element(self, locator, value=''):
        """返回bool值，value为空字符串，返回False"""
        if not isinstance(locator, tuple):
            raise LocatorTypeError("参数类型错误，locator必须是元祖类型：loc = ('id','value1')")
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.text_to_be_present_in_element_value(locator, value))
            return result
        except:
            return False

    def is_alert(self, timeout=3):
        """判断页面是否存在alert弹窗"""
        try:
            result = WebDriverWait(self.driver, timeout, self.t).until(EC.alert_is_present())
            return result
        except:
            return False

    def get_title(self):
        """获取title"""
        logger.info("当前页面的title为: %s" % self.driver.title)
        return self.driver.title

    def get_text(self, locator):
        """获取文本"""
        try:
            t = self.find(locator).text
            print(f'获取text成功，{t}')
            return t
        except Exception as e:
            print(f"获取text失败，{e}")

    def assert_text_contain(self,locator,text=''):
        """判断元素中text值"""
        msg_text = self.find(locator).text
        if text in msg_text:
            return True
        else:
            return False

    def get_attribute(self, locator, name):
        """获取属性"""
        if not isinstance(locator, tuple):
            raise LocatorTypeError("参数类型错误，locator必须是元祖类型：loc = ('id','value1')")
        try:
            element = self.find(locator)
            return element.get_attribute(name)
        except:
            print("获取%s属性失败，返回''"%name)
            return ''

    def js_focus_element(self, locator):
        """聚焦元素"""
        if not isinstance(locator, tuple):
            raise LocatorTypeError("参数类型错误，locator必须是元祖类型：loc = ('id','value1')")
        target = self.find(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    def js_scroll_top(self):
        """滚动到顶部"""
        js = "window.scrollTo(0,0)"
        self.driver.execute_script(js)

    def js_scroll_end(self, x=0):
        """滚动到底部"""
        js = "window.scrollTo(%s, document.body.scrollHeight)"%x
        self.driver.execute_script(js)

    def select(self, locator):
        """处理标准下拉选择框,随机选择"""
        select1 = self.find(locator)
        try:
            options_list = select1.find_elements_by_tag_name('option')
            del options_list[0]
            s1 = choice(options_list)
            Select(select1).select_by_visible_text(s1.text)
            logger.info("随机选的是：%s" % s1.text)
        except NameError as e:
            logger.error("Failed to click the element with %s" % e)

    def select_by_index(self, locator, index=0):
        """通过索引，index是索引第几个，从0开始，默认第一个"""
        if not isinstance(locator, tuple):
            raise LocatorTypeError("参数类型错误，locator必须是元祖类型：loc = ('id','value1')")
        element = self.find(locator)
        Select(element).select_by_index(index)

    def select_by_value(self, locator, value):
        """通过value属性"""
        if not isinstance(locator, tuple):
            raise LocatorTypeError("参数类型错误，locator必须是元祖类型：loc = ('id','value1')")
        element = self.find(locator)
        Select(element).select_by_value(value)

    def select_by_text(self, locator, text):
        """通过文本值定位"""
        element = self.find(locator)
        Select(element).select_by_visible_text(text)

    def switch_iframe(self, id_index_locator):
        """根据iframe的id/name/element/index切换"""
        self.sleep(0.5)
        try:
            if isinstance(id_index_locator, int):
                self.driver.switch_to.frame(id_index_locator)
                print(f"当前页面切换iframe --> iframe_index={id_index_locator} 成功")
            elif isinstance(id_index_locator, str):
                self.driver.switch_to.frame(id_index_locator)
                print(f"当前页面切换iframe --> iframe_id={id_index_locator} 成功")
            elif isinstance(id_index_locator, tuple):
                ele = self.find(id_index_locator)
                self.driver.switch_to.frame(ele)
                print(f"当前页面切换iframe --> Element={ele} 成功")
        except NameError as e:
            logger.error("iframe切换异常 %s" % e)
            print("iframe切换异常 %s" % e)

    def switch_main_iframe(self):
        """切换iframe到主页面"""
        self.sleep(0.5)
        try:
            self.driver.switch_to.default_content()
            logger.info("当前页面的iframe切换至 --> 主页面")
            print("当前页面的iframe切换至 --> 主页面")
        except NameError as e:
            logger.error("iframe切换异常 %s" % e)
            print("iframe切换异常 %s" % e)

    def switch_parent_iframe(self):
        """切换iframe到父页面"""
        try:
            self.driver.switch_to.parent_frame()
            logger.info("当前页面的iframe切换至 --> 父级页面")
            print("当前页面的iframe切换至 --> 父级页面")
            self.sleep(0.5)
        except NameError as e:
            logger.error("iframe切换异常 %s" % e)
            print("iframe切换异常 %s" % e)

    def switch_handle(self, window_name):
        """切换句柄"""
        self.driver.switch_to.window(window_name)

    def switch_alert(self):
        """切换弹窗"""
        r = self.is_alert()
        if not r:
            print("alert不存在")
        else:
            return r

    def move_to_element(self, locator):
        """鼠标悬停操作"""
        if not isinstance(locator, tuple):
            raise LocatorTypeError("参数类型错误，locator必须是元祖类型：loc = ('id','value1')")
        ele = self.find(locator)
        ActionChains(self.driver).move_to_element(ele).perform()

    def refresh(self):
        self.driver.refresh()
        logger.info('刷新浏览器...')
        print('刷新浏览器...')
        time.sleep(0.5)

    def quit_browser(self):
        """退出浏览器"""
        self.driver.quit()
        logger.info("关闭并退出浏览器...")
        print("关闭并退出浏览器...")

    def forward(self):
        """浏览器前进操作"""
        self.driver.forward()
        logger.info("浏览器跳转到下一页...")

    def back(self):
        """浏览器后退操作"""
        self.driver.back()
        logger.info("浏览器后退到上一页...")

    def wait(self, seconds):
        """ 隐式等待"""
        self.driver.implicitly_wait(seconds)
        logger.info("隐式等待：%d seconds." % seconds)

    def close(self):
        """点击关闭当前窗口"""
        try:
            self.driver.close()
            logger.info("关闭当前窗口...")
        except NameError as e:
            logger.error("Failed to quit the browser with %s" % e)

    def get_windows_img(self,img_name=None):
        """
        保存截图到项目根目录的一个文件夹.\img下
        """
        try:
            self.driver.get_screenshot_as_file(f'{SCREENSHOTS_PATH}/{img_name}.png')
            logger.info("保存图片成功，保存目录: \img")
        except NameError as e:
            logger.error("保存图片失败 ！ %s" % e)
            self.get_windows_img(img_name)

    def execute_js(self, js):
        """执行js"""
        self.driver.execute_script(js)

    def key_enter(self):
        """模拟回车键"""
        key = PyKeyboard()
        key.press_key(key.enter_key)
        key.release_key(key.enter_key)

    def key_tab(self):
        """模拟tab键"""
        key = PyKeyboard()
        key.press_key(key.tab_key)
        key.release_key(key.tab_key)

    def mouse_click(self,x,y):
        """鼠标点击x,y坐标"""
        mouse = PyMouse()
        #x, y = mouse.position()
        mouse.click(x, y, button=1)

    def enter(self, selector):
        """模拟回车键"""
        e1 = self.find(selector)
        e1.send_keys(Keys.ENTER)

    def tab(self, selector):
        """模拟tab键"""
        e1 = self.find(selector)
        e1.send_keys(Keys.TAB)

    def left_click(self, element):
        """模拟鼠标左击"""
        # e1 = self.find_element(selector)
        ActionChains(self.driver).click(element).perform()

    def isElementExist(self, xpath):
        """判断元素是否存在"""
        driver = self.driver
        try:
            driver.find_element_by_xpath(xpath)
            return True
        except:
            return False

    def assert_text_equal(self,locator,text):
        """判断元素中text值"""
        msg_text = self.find(locator).text
        if msg_text == text:
            return True
        else:
            return False

    def get_cookies(self,cookie_value):
        self.driver.add_cookie({"name": "ASP.NET_SessionId", "value": cookie_value})
        self.driver.refresh()
        logger.info("添加cookies成功并完成用户登录...")

    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
        logger.info("脚本停顿 {0} s".format(seconds))

    def is_clickable(self, loc, timeout=10):
        """元素可以点击is_enabled返回本身，不可点击返回Fasle"""
        result = WebDriverWait(self.driver, timeout, 1).until(EC.element_to_be_clickable(loc))
        return result

    def is_located(self, loc, timeout=10):
        """判断元素有没被定位到（并不意味着可见），定位到返回element,没定位到返回False"""
        result = WebDriverWait(self.driver, timeout, 1).until(EC.presence_of_element_located(loc))
        return result

    def click_alert(self):
        """操作点击弹窗"""
        alert = self.driver.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(1)

    def alert_text(self):
        """返回弹窗的文本内容"""
        time.sleep(2)
        alert = self.driver.switch_to.alert()
        rel = alert.text()
        return rel



