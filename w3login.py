from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\selenium\chromedriver_win32\chromedriver.exe")
driver.get("https://www.w3schools.com/")
driver.maximize_window()
driver.find_element_by_id("w3loginbtn").click()
driver.find_element_by_name("email").send_keys("anonnajannat22@gmail.com")
driver.find_element_by_name("current-password").send_keys("Anonna@321")
driver.find_element_by_xpath("//*[@id='root']/div/div/div[4]/div[1]/div/div[4]/div[1]/button/span").click()
driver.find_element_by_xpath('//*[@id="navigation"]/a[5]').click()
driver.find_element_by_id('search')
driver.find_element_by_xpath("//*[@id='htmltext']").click()
driver.find_element_by_xpath("//*[@id='csstext']").click()
driver.find_element_by_id("w3log").click()