import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common import action_chains
from selenium.webdriver.chrome.options import Options


def Get_Url(city, address, wait_time):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome('Driver/chromedriver.exe', chrome_options=chrome_options)
    driver.get('http://pyszne.pl')
    action = action_chains.ActionChains(driver)
    try:
        driver.find_element_by_id('imysearchstring').send_keys(address + ', ' + city)
        time.sleep(wait_time)
        driver.find_element_by_id('reference').send_keys(Keys.ENTER)
        action.send_keys(Keys.ENTER)
        time.sleep(wait_time)
    except Exception as e:
        return 'Wrong address'
    link = driver.current_url
    driver.quit()
    return str(link)
