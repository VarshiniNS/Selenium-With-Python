import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.ShopPageWebElements import shopPage
from PageObjects.confirmationPage import confirmationPage
from Utilities.BaseClass import BaseClass
from PageObjects.HomePageWebElements import HomePage


class TestOne(BaseClass):

    def test_E2EOne(self):
        log=self.getlogger()
        HomePageObj= HomePage(self.driver)
        ShopPageObj=HomePageObj.shopItem()
        cards = ShopPageObj.getCardTitles()
        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            log.info(cardText)

            if cardText == "Blackberry":
                ShopPageObj.getCardFooter()[i].click()
                break

        ShopPageObj.checkoutbutton().click()
        assert 'Blackberry' == ShopPageObj.checkouttextvalidation().text
        confirmationPageObj=ShopPageObj.finalcheckout()
        confirmationPageObj.dropdowntext().send_keys("ind")
        self.explictwaitforPresence("India")
        CountryList = confirmationPageObj.dropdownlist()
        for country in CountryList:
            countryName = country.text
            if (countryName == "India"):
                country.click()
                break

        confirmationPageObj.checkbox().click()
        confirmationPageObj.submit().click()
        successMessage = confirmationPageObj.success().text
        log.info("Success Musseage from application"+successMessage)
        assert "Success! Thank you!" in successMessage