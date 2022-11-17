from functools import wraps
import logging
import json


def log_info(func):
    def wrapper(*args, **kwargs):
        # kwargs should not have a value of any class/object. 
        # It SHOULD NOT PASS any keyword arguments with value of a class
        logging.info(f"""{"-"*25}
        Function Name:   {func.__name__}()
        Current URL:     {args[0].url}
        Page Title:      {args[0].title()}
        Keyword Arguments: 
{json.dumps(kwargs, indent=2)}\n""")

        result = func(*args, **kwargs)
        return result
    return wrapper

def log_page_info(func):
    def wrapper(*args, **kwargs):
        # kwargs should not have a value of any class/object. 
        # It SHOULD NOT PASS any keyword arguments with value of a class
        logging.info(f"""{"-"*25}
        Function Name:   {func.__name__}()
        Element/Page:    {args}
        Keyword Arguments: 
{json.dumps(kwargs, indent=2)}\n""")

        result = func(*args, **kwargs)
        return result
    return wrapper

def log_assert_actual_expected(func):
    '''Accept only keyword arguments named actual and expected.'''
    def wrapper(*args, **kwargs):
        # kwargs should not have a value of any class/object. 
        # It SHOULD NOT PASS any keyword arguments with value of a class
        logging.info(f"""{"-"*25}
        Function Name:  {func.__name__}()
        Actual:         {kwargs["actual"]}
        Expected:       {kwargs["expected"]}""")

        result = func(*args, **kwargs)
        return result
    return wrapper

def log_test_title(test_title:str):
    logging.info(f"\n{'#'*12} - TESTCASE: {test_title} - {'#'*12}")
