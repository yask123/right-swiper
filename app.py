from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.keys import Keys
chrome_options = ChromeOptions()
chrome_options.binary_location="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
chrome_options.add_argument('user-data-dir=~/test2')


browser = Chrome('/usr/local/bin/chromedriver', options = chrome_options)
browser.get('https://tinder.com/app')


while True:
    browser.find_element_by_css_selector('body').send_keys(Keys.RIGHT)
