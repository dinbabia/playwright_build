from WebTestSuites.E2E.login_actions import LoginActions
from playwright.sync_api import expect
from utils import *

class CommonActions:


    @log_info
    def login(page,
        email :str = None,
        password :str = None
        ):
        LoginActions.fill_up_login_form(page, email=email, password=password)
        LoginActions.click_login_button(page)

    @log_info
    def navigate_to_homepage(page):
        # Go to hompage
        page.goto("")
        # Click My Account Link to login
        expect(page).to_have_url("https://omayo.blogspot.com/search?q=sdf")
        expect(page).to_have_title("omayo (QAFox.com): Search results for sdf")

    @log_info
    def navigate_to_login_page(page):
        # Go to hompage
        page.goto("")
        # Click My Account Link to login
        expect(page).to_have_url("https://www.saucedemo.com/")
        expect(page).to_have_title("Swag Labs")