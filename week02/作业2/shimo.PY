from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get('https://shimo.im/welcome')
    time.sleep(5)

    find_tm = browser.find_element_by_xpath('//*[@id="homepage-header"]/nav/div[3]/a[2]/button')
    find_tm.click()

    browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/input')\
        .send_keys('18210357370')
    time.sleep(3)
    browser.find_chelement_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/input')\
        .send_keys('zjyxxxx')
    time.sleep(3)
    browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/button').click()

    print('登录成功')
    time.sleep(3)
except Exception as everay_error:
    print(everay_error)
