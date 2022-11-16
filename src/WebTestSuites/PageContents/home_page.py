from playwright.sync_api import Page, expect
from utils import *

class LoginPage:

    @log_page_info
    def check_element_attributes(element, attributes:dict = None):
        '''Usually used with KKV csv reader'''
        for attr, val in attributes.items():
            if val is True:
                expect(element).to_be_checked()
            else:
                expect(element).to_have_attribute(name=attr, value=val)

    @log_page_info
    def check_element_texts_list(actual_list:list=None, expected_list:list = None):
        '''Usually used with KV csv reader'''
        for actual, expected in zip(actual_list, expected_list):
            assert str(actual) == str(expected), f"[FAIL - ASSERTION] ACTUAL: {actual} vs. EXPECTED: {expected}"

    @log_page_info
    def check_element_texts_dict(headers:list=None, actual_list:list=None, expected:dict = None):
        '''Usually used with headers csv reader'''
        actual = {key:value for key, value in zip(headers,actual_list)}
        for count in range(len(expected)):
            assert actual[headers[count]] == expected[headers[count]],  f"[FAIL - ASSERTION] ACTUAL: {actual[headers[count]]} vs. EXPECTED: {expected[headers[count]]}"
        