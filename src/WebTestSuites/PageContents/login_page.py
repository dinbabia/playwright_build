from playwright.sync_api import Page, expect
from utils import *

class LoginPage:

    @log_page_info
    def check_element_attributes(element, attributes:dict = None):
        for attr, val in attributes.items():
            expect(element).to_have_attribute(name=attr, value=val)