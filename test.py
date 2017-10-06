from selenium import webdriver



driver = webdriver.Remote(
            command_executor='http://172.31.36.129:4444/grid/register/',
            desired_capabilities={'browserName': 'chrome'})
driver.get('https:www.google.com')
driver.quit()