from selenium.webdriver.common.by import By


class confirmationPage:
    def __init__(self,driver):
        self.driver = driver

    dropdowntextbox=(By.CSS_SELECTOR, "#country")
    dropdown=(By.CSS_SELECTOR, "div[class='suggestions'] ul li a")
    termsconditioncheckbox=(By.XPATH, "//div[@class='checkbox checkbox-primary']")
    submitbutton=(By.CSS_SELECTOR, "input[class='btn btn-success btn-lg']")
    successmessage=(By.CSS_SELECTOR, "div[class='alert alert-success alert-dismissible']")
    def dropdowntext(self):
        return self.driver.find_element(*confirmationPage.dropdowntextbox)

    def dropdownlist(self):
        return  self.driver.find_elements(*confirmationPage.dropdown)
    def checkbox(self):
        return self.driver.find_element(*confirmationPage.termsconditioncheckbox)

    def submit(self):
        return self.driver.find_element(*confirmationPage.submitbutton)

    def success(self):
        return self.driver.find_element(*confirmationPage.successmessage)
