import pytest

from PageObjects.HomePageWebElements import HomePage
from Utilities.BaseClass import BaseClass
from testData.HomePageData import HomePagedata


class TestE2ELogin(BaseClass):

    def test_formsubmission(self, getData):
        log=self.getlogger()
        HomePageObj = HomePage(self.driver)
        log.info("Data for the form")
        HomePageObj.nameText().send_keys(getData["FirstName"])
        HomePageObj.emailText().send_keys(getData["Email"])
        HomePageObj.passwordText().send_keys(getData["Password"])
        self.selectByText(HomePageObj.dropdownselection(), getData["Gender"])
        HomePageObj.submitbutton().click()
        log.info("Success Message from screen is "+HomePageObj.getSuccessMessage().text)
        assert "Success" in HomePageObj.getSuccessMessage().text
        self.driver.refresh()

    # data passed in tuple and list @pytest.fixture(params=[("Apple","fruits@gmail.com ","Passs","Female"),("Carrot","Vegetable@gmail.com ","Veggie","Female"),("rose","flower@gmail.com ","flowery","Male")])
    # data in dict

    @pytest.fixture(params=HomePagedata.getTestData("Set1"))
    def getData(self, request):
        return request.param
