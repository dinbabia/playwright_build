from playwright.sync_api import Page
from csv_reader import *
from WebTestSuites.checker import Checker
from WebTestSuites._locators.homepage_loc import *
from WebTestSuites.common import CommonActions
from utils import log_test_title


common_step = CommonActions
check = Checker
SELECT_MULTIPLE_OPTIONS = CSVKeyKeyValue(filename="homepage_select_multiple_options-kkv.csv")
ORDERED_UNORDERED_LISTS = CSVKeyValue(filename="homepage_ordered_unordered_lists-kv.csv")
TABLE_CONTENTS = CSVHeaders(filename="homepage_table-h.csv")

def test_homepage_select_multiple_options(page: Page) -> None:

    common_step.navigate_to_homepage(page)
    # Check First Option Attributes
    pen_checkbox = page.locator(select_multiple_options_loc).first
    check.check_element_attributes(pen_checkbox,
        attributes=SELECT_MULTIPLE_OPTIONS.data["pen"])
    # Check Second Option Attributes (checked)
    book_checkbox = page.locator(select_multiple_options_loc).nth(1)
    check.check_element_attributes(book_checkbox,
        attributes=SELECT_MULTIPLE_OPTIONS.data["book"])
    # Check Third Option Attributes
    laptop_checkbox = page.locator(select_multiple_options_loc).nth(2)
    check.check_element_attributes(laptop_checkbox,
        attributes=SELECT_MULTIPLE_OPTIONS.data["laptop"])
    # Check Fourth Option Attributes
    bag_checkbox = page.locator(select_multiple_options_loc).nth(3)
    check.check_element_attributes(bag_checkbox,
        attributes=SELECT_MULTIPLE_OPTIONS.data["bag"])


def test_homepage_ordered_unordered_lists(page : Page) -> None:

    common_step.navigate_to_homepage(page)
    # Check Ordered List
    ordered_list = page.locator(ordered_list_loc)
    check.check_element_texts_list(actual_list = ordered_list.all_inner_texts(),
        expected_list = ORDERED_UNORDERED_LISTS.data["ordered_list"])
    # Check Unordered List
    unordered_list = page.locator(unordered_list_loc)
    check.check_element_texts_list(actual_list = unordered_list.all_inner_texts(),
        expected_list = ORDERED_UNORDERED_LISTS.data["unordered_list"])

def test_homepage_table(page : Page) -> None:
    
    common_step.navigate_to_homepage(page)
    # Get header names from table
    headers = page.locator(table_header_loc).all_inner_texts()
    # Check row one
    row_one = page.locator(table_row_loc.format(row_number=1)).all_inner_texts()
    check.check_element_texts_dict(headers=headers,
        actual_list=row_one, expected=TABLE_CONTENTS.data[0])
    # Check row two
    row_two = page.locator(table_row_loc.format(row_number=2)).all_inner_texts()
    check.check_element_texts_dict(headers=headers,
        actual_list=row_two, expected=TABLE_CONTENTS.data[1])
    # Check row three
    row_three = page.locator(table_row_loc.format(row_number=3)).all_inner_texts()
    check.check_element_texts_dict(headers=headers,
        actual_list=row_three, expected=TABLE_CONTENTS.data[2])
    # Check row four
    row_four = page.locator(table_row_loc.format(row_number=4)).all_inner_texts()
    check.check_element_texts_dict(headers=headers,
        actual_list=row_four, expected=TABLE_CONTENTS.data[3])

def test_homepage_elements(page: Page) -> None:

    log_test_title(test_title="check_select_multiple_options")
    common_step.navigate_to_homepage(page)
    # Check First Option Attributes
    pen_checkbox = page.locator(select_multiple_options_loc).first
    check.check_element_attributes(pen_checkbox,
        attributes=SELECT_MULTIPLE_OPTIONS.data["pen"])
    # Check Second Option Attributes (checked)
    book_checkbox = page.locator(select_multiple_options_loc).nth(1)
    check.check_element_attributes(book_checkbox,
        attributes=SELECT_MULTIPLE_OPTIONS.data["book"])
    # Check Third Option Attributes
    laptop_checkbox = page.locator(select_multiple_options_loc).nth(2)
    check.check_element_attributes(laptop_checkbox,
        attributes=SELECT_MULTIPLE_OPTIONS.data["laptop"])
    # Check Fourth Option Attributes
    bag_checkbox = page.locator(select_multiple_options_loc).nth(3)
    check.check_element_attributes(bag_checkbox,
        attributes=SELECT_MULTIPLE_OPTIONS.data["bag"])

    log_test_title(test_title="check_ordered_unordered_lists")
    page2 = page.context.new_page()
    common_step.navigate_to_homepage(page2)
    # Check Ordered List
    ordered_list = page2.locator(ordered_list_loc)
    check.check_element_texts_list(actual_list = ordered_list.all_inner_texts(),
        expected_list = ORDERED_UNORDERED_LISTS.data["ordered_list"])
    # Check Unordered List
    unordered_list = page2.locator(unordered_list_loc)
    check.check_element_texts_list(actual_list = unordered_list.all_inner_texts(),
        expected_list = ORDERED_UNORDERED_LISTS.data["unordered_list"])
