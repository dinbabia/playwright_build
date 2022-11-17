from utils import *
from WebTestSuites._locators.loginpage_loc import *

class LoginActions:
 
    @log_info
    def fill_up_login_form(page,
        username :str = None,
        password :str = None
        ):
        if username:
            page.locator(username_field_loc).click()
            page.locator(username_field_loc).fill(username)
        if password:
            page.locator(password_field_loc).click()
            page.locator(password_field_loc).fill(password)
            
    @log_info
    def click_login_button(page):
        page.locator(login_button_loc).click()

    @log_info
    def get_login_error_msg(page) -> str:
        error_msg = page.locator(error_msg_loc).inner_text()
        return error_msg



        