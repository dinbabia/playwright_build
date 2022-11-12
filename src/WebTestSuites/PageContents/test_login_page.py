from playwright.sync_api import Page, expect
from WebTestSuites.E2E.login_actions import LoginActions
from csv_reader import ExcelFile
from WebTestSuites.PageContents.login_page import LoginPage
import logging


step = LoginActions
check = LoginPage


def test_login_page_contents(page : Page) -> None:
   
    step.navigate_to_login_page(page)

    sign_in_tab = page.get_by_role("link", name="Sign in")
    register_tab = page.get_by_role("link", name="Register")
    expect(sign_in_tab).to_be_visible()

    text_input_email = page.get_by_label("Your Email")
    text_input_password = page.get_by_label("Password")
    a = {
            "data-val-maxlength" : "The maximum length for this field is 254 characters.",
            "data-val-maxlength-max" : "254",
            "type" : "email"
        }
    check.check_element_attributes(text_input_email,
        attributes=a)

    expect(text_input_email).to_be_empty()
    
    expect(text_input_password).to_be_empty()
    expect(text_input_email).to_be_editable()
    expect(text_input_password).to_be_editable()
    expect(text_input_email).to_be_enabled()
    expect(text_input_password).to_be_enabled()
    expect(text_input_email).to_be_visible()
    expect(text_input_password).to_be_visible()
    

    forgot_pass_link = page.get_by_role("link", name="Forgot Password?")
    button_sign_in = page.get_by_role("button", name="Sign in")
    image_presentation = page.get_by_role("presentation")


    
    
   