from random import randint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep, ctime
from selenium.common.exceptions import NoSuchElementException
import os
from selenium.webdriver.common.action_chains import ActionChains

# 随机数1-9
# number = randint(1, 9)
#
# if number % 2 == 0:
#     raise NameError('%d is even' % number)
# else:
#     raise NameError('%d is odd' % number)

driver = webdriver.Chrome(r'D:\2zyyyyy\chromedriver_win32\chromedriver.exe')
driver.maximize_window()
# driver.implicitly_wait(10)  # 设置隐式等待
# driver.get('http://www.baidu.com')

# element = WebDriverWait(driver, 5, 0.5).until(
#           EC.presence_of_element_located((By.ID, 'kw'))
#                                              )
# element.send_keys('selenium')
# driver.quit()
# 判断元素是否可见
# print(ctime())
# for i in range(10):
#     try:
#         element = driver.find_element_by_id('kw2')
#         if element.is_displayed():
#             print('定位成功')
#             break
#     except: pass
#     sleep(1)
# else:
#     print('time out')
# driver.close()
# print(ctime())

# try:
#     print(ctime())
#     driver.find_element_by_id('kw').send_keys('selenium')
#     sleep(2)
#     driver.find_element_by_id('su').click()
#     sleep(2)
# except NoSuchElementException as e:
#     print(e)
# finally:
#     print(ctime())
#     driver.quit()

# file_path = 'file:///' + os.path.abspath('checkbox.html')
# file_path = 'D:\\2zyyyyy\\__MACOSX\\Spider\\htmlDemo\\frame.html'
# driver.get(file_path)
# driver.maximize_window()

# # 选择页面上所有的tag name为input的元素
# inputs = driver.find_elements_by_tag_name('input')
#
# # 过滤出type为CheckBox的元素 单击勾选
# for i in inputs:
#     if i.get_attribute('type') == 'checkbox':
#         i.click()
#         sleep(1)
# driver.quit()

# 通过xpath找到type==CheckBox的元素信息
# checkboxs = driver.find_elements_by_xpath("//inputs[@type='checkbox']")

# 通过css找到type==CheckBox的元素信息
# checkboxs = driver.find_elements_by_css_selector("input[type=checkbox]")
# for checkbox in checkboxs:
#     checkbox.click()
#     sleep(1.5)
#
# # 打印CheckBox的个数
# print(len(checkboxs))
#
# # 把页面上最后一个CheckBox的勾去掉
# driver.find_elements_by_css_selector("input[type=checkbox]").pop(0).click()
# sleep(2)
#
# driver.quit()

# 切换到iframe(id==if)
# driver.switch_to.frame('if')
#
# # 切换到frame之后就可以正常操作页面元素
# driver.find_element_by_id('kw').send_keys('selenium')
# driver.find_element_by_id('su').click()
# sleep(3)
#
# driver.quit()

# 获得百度搜索窗口的句柄
# search_windows = driver.current_window_handle
#
# driver.find_element_by_link_text('登录').click()
# driver.find_element_by_link_text('立即注册').click()
#
# # 获取当前所有打开窗口的句柄
# all_handles = driver.window_handles
#
# # 进入注册窗口
# for handle in all_handles:
#     if handle != search_windows:
#         driver.switch_to.window(handle)
#         print('当前为注册窗口')
#         driver.find_element_by_id('TANGRAM__PSP_3__userName').send_keys('TANGRAM__')
#         driver.find_element_by_id('TANGRAM__PSP_3__phone').send_keys('18545124781')
#         driver.find_element_by_id('TANGRAM__PSP_3__password').send_keys('asd2156')
#         sleep(2)
#
# # 回到搜索窗口
# for handle in all_handles:
#     if handle == search_windows:
#         print('当前为搜索窗口')
#         driver.switch_to.window(handle)
#         sleep(1)
#         driver.find_element_by_id('TANGRAM__PSP_4__closeBtn').click()
#         driver.find_element_by_id('kw').send_keys('selenium')
#         driver.find_element_by_id('su').click()
#         sleep(2)
#
# driver.quit()

# 鼠标悬停设置 链接
# link = driver.find_element_by_link_text('设置')
# ActionChains(driver).move_to_element(link).perform()
#
# # 打开搜索设置
# driver.find_element_by_link_text('搜索设置').click()
# sleep(2)
#
# # 保存设置
# driver.find_element_by_class_name("prefpanelgo").click()
# sleep(2)
#
# # 接收警告框
# driver.switch_to.alert.accept()
#
# driver.quit()

# url = 'D:\\2zyyyyy\\__MACOSX\\Spider\\htmlDemo\\upload_file.html'
# driver.get(url)
#
# sleep(2)
# print('正在上传...')
# driver.find_element_by_name('file').send_keys('C:\\Users\\admin\\Desktop\\other\\张昀.txt')
# sleep(2)
# print('上传成功')
#
# driver.quit()

# fp = webdriver.ChromeOptions()
# '''
#     download.default_directory:设置下载路径
#     profile.default_content_settings.popups:设置为0禁止弹出窗口
# '''
# prefs = {'profile.default_content_setting.popups': 0, 'download.default_directory': 'C:\\Users\\admin\\Desktop'}
# fp.add_experimental_option('prefs', prefs)
# driver = webdriver.Chrome(r'D:\2zyyyyy\chromedriver_win32\chromedriver.exe')
# driver.maximize_window()
# driver.get('http://sahitest.com/demo/saveAs.htm')
# driver.find_element_by_link_text('testsaveas.zip').click()
# sleep(3)
# print('测试通过.')
#
# driver.quit()

# driver.get('http://www.youdao.com')
#
# # 向cookie中的那么和value属性添加会话信息
# driver.add_cookie({'name': 'key-2zyyyyy', 'value': 'value-testing!!!'})
# # 遍历cookie中的name和value信息并打印
# for cookie in driver.get_cookies():
#     print('%s -> %s' % (cookie['name'], cookie['value']))
# driver.quit()

# driver.get('http://www.baidu.com')
# # 控制浏览器窗口大小
# driver.set_window_size(800, 800)
#
# driver.find_element_by_id('kw').send_keys('selenium')
# driver.find_element_by_id('su').click()
# sleep(2)
#
# # 通过JavaScript设置浏览器窗口的滚动条位置
# javaScripts = 'window.scrollTo(100, 500);'
# driver.execute_script(javaScripts)
# sleep(3)
#
# print('test success!!')
# driver.quit()

# driver.get('http://videojs.com/')
#
# video = driver.find_element_by_id('preview-player_html5_api')
#
# # 返回播放文件地址
# url = driver.execute_script('return arguments[0].currentSrc;', video)
# print(url)
#
# # 播放视频
# print('video play test start.')
# driver.execute_script('return arguments[0].play()', video)
#
# # 设置播放时长
# sleep(15)
#
# # 暂停视频
# print('video play stop.')
# driver.execute_script('arguments[0].pause', video)
# # 窗口截图
# driver.get_screenshot_as_file('C:\\Users\\admin\\Desktop\\playimg.jpg')
#
# print('video play success.')
# driver.quit()

# 万恶的验证码之设置万能验证码
# 生成一个1000-9999之间的随机数
verify = randint(1000, 9999)
print('生成的随机数: %d' % verify)

number = input('请输入验证码')
print(number)
number = int(number)

if number == verify:
    print('login success.')
elif number == 1234:
    print('万能验证码登录成功')
else:
    print('验证码错误')