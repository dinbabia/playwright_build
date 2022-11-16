from playwright.sync_api import Page, expect
from WebTestSuites.E2E.login_actions import LoginActions
from csv_reader import *
from WebTestSuites.common import CommonActions
import logging


step = LoginActions
common_step = CommonActions
VALID_ACCOUNTS = CSVHeaders(filename="invalid_accounts.csv")
INVALID_ACCOUNTS = CSVHeaders(filename="invalid_accounts.csv")
KEY_VALUES = CSVKeyValue(filename="key_values.csv")

def test_login_success(page : Page) -> None:
   
    step.navigate_to_homepage(page)
    # Fill up login form
    step.fill_up_login_form(page, email=VALID_ACCOUNTS.data[0]['email'], password=VALID_ACCOUNTS.data[0]['password'])
    # Click Login
    step.click_login_button(page)
    
    # ---Assertions---
    expect(page).to_have_url("https://www.coilcraft.com/en-us/profile/")

def test_empty_email_and_password(page : Page) -> None:

    step.navigate_to_homepage(page)
    # Click Login
    step.click_login_button(page)
    #Get validation messages
    empty_email_message = page.get_by_text("The Email address cannot be empty")
    empty_password_message = page.get_by_text("Password cannot be empty")
    
    # ---Assertions---
    expect(empty_email_message).to_have_text("The Email address cannot be empty")
    expect(empty_password_message).to_have_text("Password cannot be empty")


def test_incorrect_email_format(page : Page) -> None:
 
    step.navigate_to_homepage(page)
    # Fill up login form
    step.fill_up_login_form(page, email="invalid_email", password="123")
    # Click Login
    step.click_login_button(page)

    invalid_email_format_message = page.get_by_text("Incorrect E-Mail address format")

    # ---Assertions---
    expect(invalid_email_format_message).to_have_text("Incorrect E-Mail address format")


def test_key_values():
    print(KEY_VALUES.data)    
    print(VALID_ACCOUNTS.data)
    
    
