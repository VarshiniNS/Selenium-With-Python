# Opening Website
# Navigate to child window
# Get the text and extract mail id from the text
# Close child window
# Navigate back to parent window
# Provide extracted mail id ,password and other details
# Click on Sign In
# Print the error message

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

chromeoptionObj=webdriver.ChromeOptions()
chromeoptionObj.add_argument("headless")
serviceObj = Service()
driver = webdriver.Chrome(service=serviceObj,options=chromeoptionObj)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.find_element(By.LINK_TEXT, "Free Access to InterviewQues/ResumeAssistance/Material").click()
openWindows=driver.window_handles
driver.switch_to.window(openWindows[1])
message = driver.find_element(By.CSS_SELECTOR, ".red").text
mailid = message.split("at")[1].strip().split(" ")[0]
driver.close()
driver.switch_to.window(openWindows[0])
driver.find_element(By.CSS_SELECTOR,"#username").send_keys(mailid)
driver.find_element(By.CSS_SELECTOR,"#password").send_keys("123545")
driver.find_element(By.CSS_SELECTOR,"input[value='admin']").click()
driver.find_element(By.CSS_SELECTOR,"select option:nth-child(1)").click()
driver.find_element(By.CSS_SELECTOR,"span input[name='terms']").click()
driver.find_element(By.CSS_SELECTOR,"input[value='Sign In']").click()
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
driver.get_screenshot_as_png()
print(driver.find_element(By.CSS_SELECTOR, ".alert-danger").text)