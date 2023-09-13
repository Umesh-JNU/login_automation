from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

username = <REPLACE_WITH_YOUR_USERNAME>
password = <REPLACE_WITH_YOUR_PASSWORD>

url = <URL>

driver.get(url)

# select the username input field
username_field = driver.find_element(By.ID, "text") 
# select the password input field
password_field = driver.find_element(By.ID, "password") 
# select the login button
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

# fill the input field or fill the form
username_field.send_keys(username)  
password_field.send_keys(password) 

# Click the login button
login_button.click()

# Perform assertions to verify the successful login
try:
    # wait for some time to get login
    time.sleep(5)
    
    # Replace with your own assertions based on the behavior of the web application
    assert "Dashboard" in driver.page_source  # Check if the word
    print("Login Successful!")
except AssertionError as e:
    print("Login Failed:", e)

# Close the browser
driver.quit()
