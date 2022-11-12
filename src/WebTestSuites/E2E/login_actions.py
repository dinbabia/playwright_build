from playwright.sync_api import Page, expect
from utils import *

class LoginActions:

    @log_info
    def navigate_to_login_page(page):
        # Go to hompage
        page.goto("")
        # Click My Account Link to login
        page.get_by_role("link", name="My Account").click()
        expect(page).to_have_url("https://www.coilcraft.com/en-us/account/signin/?ReturnUrl=%2Fen-us%2Fprofile%2F")
        
    @log_info
    def fill_up_login_form(page,
        email :str = None,
        password :str = None
        ):
        if email:
            page.get_by_label("Your Email").click()
            page.get_by_label("Your Email").fill(email)
        if password:
            page.get_by_label("Password").click()
            page.get_by_label("Password").fill(password)
            
    @log_info
    def click_login_button(page):
        page.get_by_role("button", name="Sign in").click()


        