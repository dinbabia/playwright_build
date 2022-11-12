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

        func(*args, **kwargs)
    return wrapper

def log_page_info(func):
    def wrapper(*args, **kwargs):
        # kwargs should not have a value of any class/object. 
        # It SHOULD NOT PASS any keyword arguments with value of a class
        logging.info(f"""{"-"*25}
        Function Name:   {func.__name__}()
        Element:         {args}
        Keyword Arguments: 
{json.dumps(kwargs, indent=2)}\n""")

        func(*args, **kwargs)
    return wrapper

