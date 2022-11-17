from playwright.sync_api import Page, expect
from utils import *

class PageChecker:

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
        assert len(actual_list) == len(expected_list), f"[FAIL - ASSERTION] ACTUAL len(actual_list): {len(actual_list)} vs. EXPECTED len(expected_list): {len(expected_list)}"
        for i in range(len(expected_list)):
            assert str(actual_list[i]) == str(expected_list[i]), f"[FAIL - ASSERTION] ACTUAL: {actual_list[i]} vs. EXPECTED: {expected_list[i]}"

    @log_page_info
    def check_element_texts_dict(headers:list=None, actual_list:list=None, expected:dict = None):
        '''Usually used with headers csv reader'''
        assert len(headers) == len(actual_list), f"[FAIL - ASSERTION] len(headers): {len(headers)} vs. len(actual_list): {len(actual_list)}"
        assert len(actual_list) == len(expected.values()), f"[FAIL - ASSERTION] ACTUAL len(actual_list): {len(actual_list)} vs. EXPECTED len(expected.values()): {len(expected.values())}"
        actual = {key:value for key, value in zip(headers,actual_list)}
        for count in range(len(expected)):
            assert actual[headers[count]] == expected[headers[count]],  f"[FAIL - ASSERTION] ACTUAL: {actual[headers[count]]} vs. EXPECTED: {expected[headers[count]]}"
        