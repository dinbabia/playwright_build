'''
We will separate the locators so that if there are changes with its address/locator,
we can just update/change it here only. We won't be having a hard time updating/changing
each locators called in the test cases.
'''

select_multiple_options_loc = "input[name=\"accessories\"]"
'''Accessories:
* .first = pen
* .nth(1) = book 
* .nth(2) = laptop
* .nth(3) = bag'''

ordered_list_loc = "xpath=//div[@id='HTML25']/div/ol/li"
'''Locator for all text in the ordered list.'''

unordered_list_loc = "xpath=//div[@id='HTML26']/div/ul/li"
'''Locator for all text in the unorrderd list.'''

table_header_loc = "xpath=//table[@id='table1']/thead/tr/th"
'''Table headers locator'''

table_row_loc = "xpath=//table[@id='table1']/tbody/tr[{row_number}]/td"
'''Table row locator.\n 
Required format arguments:
* row_number -> the table row number starting from 1
'''