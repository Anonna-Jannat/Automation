from selenium import webdriver

driver = webdriver.Chrome(executable_path= "C:\selenium\chromedriver_win32\chromedriver.exe")
driver.get("https://www.w3schools.com/")
driver.maximize_window()
driver.find_element_by_id("w3loginbtn").click()
driver.find_element_by_xpath('//*[@id="root"]/div/div/div[4]/div[1]/div/div[2]/form/div[1]/div[1]/span/span').click()
driver.find_element_by_id("modalusername").send_keys("anonna071@gmail.com")
driver.find_element_by_id("new-password").send_keys("Anonna@321")
driver.find_element_by_xpath("//*[@id='root']/div/div/div[4]/div[1]/div/div[4]/div[1]/button/span").click()
driver.find_element_by_id("modal_first_name").send_keys("Anonna")
driver.find_element_by_id("modal_last_name").send_keys("Aktar")
driver.find_element_by_xpath('//*[@id="root"]/div/div/div[4]/div[1]/div/div[3]/div/button/span').click()
