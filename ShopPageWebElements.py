from selenium.webdriver.common.by import By

from PageObjects.confirmationPage import confirmationPage


class shopPage:
    def __init__(self, driver):
        self.driver = driver

    # productListWebElements = (By.CSS_SELECTOR, "div [class='card h-100']")
    # productText=(By.CSS_SELECTOR, ".card-title a")
    # productbutton=(By.CSS_SELECTOR, "button")
    cardTitle = (By.CSS_SELECTOR, ".card-title a")
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")
    checkout = (By.CSS_SELECTOR, "a[class*='nav-link btn btn-primary']")
    checkouttext = (By.XPATH, "//div[@class='media']/div/h4/a")
    finalcheckoutbtn = (By.CSS_SELECTOR, "button[class='btn btn-success']")

    # def getproductlist(self):
    #   return self.driver.find_elements(*shopPage.productListWebElements)
    #
    # def getproducttext(self):
    #     return self.getproductlist().find_element(*shopPage.productText)
    #
    # def productbutton(self):
    #     return self.driver.find_element(*shopPage.productbutton)
    def getCardTitles(self):
        return self.driver.find_elements(*shopPage.cardTitle)

    def getCardFooter(self):
        return self.driver.find_elements(*shopPage.cardFooter)

    def checkoutbutton(self):
        return self.driver.find_element(*shopPage.checkout)

    def checkouttextvalidation(self):
        return self.driver.find_element(*shopPage.checkouttext)

    def finalcheckout(self):
         self.driver.find_element(*shopPage.finalcheckoutbtn).click()
         confirmationPageObj = confirmationPage(self.driver)
         return confirmationPageObj