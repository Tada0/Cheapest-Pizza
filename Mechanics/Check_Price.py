import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common import action_chains
from selenium.webdriver.chrome.options import Options


def Check_Price(url, meal_id, restaurant_id, city, address):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome('Driver/chromedriver.exe', chrome_options=chrome_options)
    driver.get('http://pyszne.pl')
    action = action_chains.ActionChains(driver)
    try:
        driver.find_element_by_id('imysearchstring').send_keys(address + ', ' + city)
        time.sleep(1)
        driver.find_element_by_id('reference').send_keys(Keys.ENTER)
        action.send_keys(Keys.ENTER)
        time.sleep(2)
        driver.find_element_by_id('irestaurant' + restaurant_id).click()
        time.sleep(1)
        driver.find_element_by_id(meal_id).click()
        time.sleep(1)
        driver.find_element_by_id('isizeselection').click()
        time.sleep(1)
        ret_val = driver.find_element_by_id('isizeselection').text
        time.sleep(1)
    except Exception as e:
        return 'Error occured while searching for price'
    driver.quit()
    return str(ret_val)