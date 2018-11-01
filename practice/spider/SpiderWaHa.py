from selenium import webdriver
import time

driver = webdriver.Chrome()
url = "https://bbs.52waha.com/"
login_url = "https://graph.qq.com/oauth2.0/show?which=Login&display=pc&response_type=code&client_id=10035348&redirect_uri=https%3A%2F%2Fbbs.52waha.com%2Fconnect.php%3Fmod%3Dlogin%26op%3Dcallback%26referer%3Dforum.php%253Fmod%253Dviewthread%2526tid%253D548224%2526extra%253Dpage%25253D1%2526page%253D1&state=f575de06c75cc78283e7f1a56853751e&scope=get_user_info%2Cadd_share%2Cadd_t%2Cadd_pic_t%2Cget_repost_list"
driver.get(url)
try:
    driver.find_element_by_id("nv_forum").click()
except:
    print('try')
time.sleep(5)
print("5s 睡眠结束")
driver.find_element_by_xpath('//div[@class="fastlg_fm y"]/p/a[@href]').click()
time.sleep(3)
driver.find_element_by_class_name('lay_login_form').click()
print('登陆成功')
time.sleep(10)
print("签到页面+10")
try:
    driver.find_element_by_xpath('//div[@class="hdc cl"]/div[@id="um"]/p/following-sibling::p/a[@href]').click()
except:
    print("签到页面")

print("签到")
# driver.get("https://bbs.52waha.com/plugin.php?id=gsignin:index")
time.sleep(5)
driver.find_element_by_xpath('//div[@class="top"]/a[@href]').click()
time.sleep(2)
print("签到成功")


driver.quit()
