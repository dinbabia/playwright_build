from playwright.sync_api import Page
from WebTestSuites.E2E.login_actions import LoginActions

class CommonActions:



    def login(page,
        email :str = None,
        password :str = None
        ):
        LoginActions.fill_up_login_form(page, email=email, password=password)
        LoginActions.click_login_button(page)