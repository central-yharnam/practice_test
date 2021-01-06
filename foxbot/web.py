
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Firefox

# Start the driver
#with webdriver.Firefox() as driver:
    # Open URL
    
  
driver = Firefox()

driver.get("https://seleniumhq.github.io")

# Setup wait for later
wait = WebDriverWait(driver, 10)

# Store the ID of the original window
original_window = driver.current_window_handle

# Check we don't have other windows open already
assert len(driver.window_handles) == 1


#driver.manage.new_window
driver.execute_script("window.open('https://github.com', 'tab')")
# Click the link which opens in a new window
#driver.find_element(By.LINK_TEXT, "AutomatedTester").click()

# Wait for the new window or tab
wait.until(EC.number_of_windows_to_be(2))

    

# Loop through until we find a new window handle
for window_handle in driver.window_handles:
    if window_handle != original_window:
        driver.switch_to.window(window_handle)
        break

# Wait for the new tab to finish loading content
wait.until(EC.title_contains("G"))


#Close the tab or window
driver.close()

#Switch back to the old tab or window
driver.switch_to.window(original_window)

# Store iframe web element
#iframe = driver.find_element(By.CSS_SELECTOR, "#modal > iframe")

driver.find_elements_by_class_name('person')

driver.switch_to.frame(1)

# switch to selected iframe
#driver.switch_to.frame(iframe)

# Now click on button
driver.find_element(By.TAG_NAME, 'button').click()
