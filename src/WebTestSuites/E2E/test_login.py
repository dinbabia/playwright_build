from playwright.sync_api import Page
from WebTestSuites.E2E.login_actions import LoginActions
from csv_reader import *
from WebTestSuites.common import CommonActions
from WebTestSuites.checker import Checker



step = LoginActions
common_step = CommonActions
check_step = Checker
VALID_ACCOUNTS = CSVHeaders(filename="loginpage_valid_accounts.csv")
INVALID_ACCOUNTS = CSVHeaders(filename="loginpage_invalid_accounts.csv")


def test_login_success(page : Page) -> None:
   
    common_step.navigate_to_login_page(page)
    # Fill up login form
    step.fill_up_login_form(page, 
        username=VALID_ACCOUNTS.data[0]['username'], 
        password=VALID_ACCOUNTS.data[0]['password'])
    # Click Login
    step.click_login_button(page)
    
    # ---Assertions--- #
    check_step.check_element_url_and_title(page,
        expected_url="https://www.saucedemo.com/inventory.html",
        expected_title="Swag Labs")

def test_login_failed(page : Page) -> None:
   
    common_step.navigate_to_login_page(page)
    # Fill up login form
    step.fill_up_login_form(page, 
        username=INVALID_ACCOUNTS.data[0]['username'], 
        password=INVALID_ACCOUNTS.data[0]['password'])
    # Click Login
    step.click_login_button(page)
    # Get error message
    error_message = step.get_login_error_msg(page)

    # ---Assertions--- #
    check_step.check_element_url_and_title(page,
        expected_url="https://www.saucedemo.com/",
        expected_title="Swag Labs")

    check_step.check_element_string(actual=error_message,
        expected="Epic sadface: Sorry, this user has been locked out.")
    
    


    
    
