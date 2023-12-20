from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from PageObjects.ShopPageWebElements import shopPage


class HomePage:
    def __init__(self,driver):
        self.driver=driver

    shop =(By.LINK_TEXT,"Shop")
    NameTextBox =(By.XPATH,"(//input[@name='name'])[1]")
    EmailTextBox=(By.CSS_SELECTOR,"input[name='email']")
    PasswordTextBox=(By.CSS_SELECTOR,"#exampleInputPassword1")
    Dropdownwebelement=(By.ID,"exampleFormControlSelect1")
    submitbtn=(By.CSS_SELECTOR,"input[value='Submit']")
    AlertText=(By.CSS_SELECTOR,"div.alert.alert-success.alert-dismissible")


    def shopItem(self):
       self.driver.find_element(*HomePage.shop).click()
       ShopPageObj = shopPage(self.driver)
       return ShopPageObj

    def nameText(self):
        return self.driver.find_element(*HomePage.NameTextBox)


    def emailText(self):
        return self.driver.find_element(*HomePage.EmailTextBox)

    def passwordText(self):
        return self.driver.find_element(*HomePage.PasswordTextBox)

    def dropdownselection(self):
        return self.driver.find_element(*HomePage.Dropdownwebelement)


    def submitbutton(self):
        return self.driver.find_element(*HomePage.submitbtn)

    def getSuccessMessage(self):
        return self.driver.find_element(*HomePage.AlertText)
