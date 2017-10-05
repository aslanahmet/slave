from selenium import webdriver



driver = webdriver.Remote(
            command_executor='http://localhost:5550/wd/hub',
            desired_capabilities={'browserName': 'chrome'})
driver.get('https:www.google.com')
driver.quit()