from selenium import webdriver

driver = webdriver.Chrome(executable_path=("C:\selenium browser driver\chromedriver.exe"))

driver.get( "https://ya.ru/" )
driver.find_element_by_id( "text" ).click()
driver.find_element_by_id( "text" ).clear()
driver.find_element_by_id( "text" ).send_keys( "test" )
driver.find_element_by_css_selector( ".search2" ).submit()
