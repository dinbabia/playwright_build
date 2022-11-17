import pytest
from tkinter import Tk
import os

root = Tk()

PROJECT_NAME = "INSERT PROJECT NAME HERE"
TESTER_NAME = os.getlogin()


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {
            "width" : root.winfo_screenwidth(),
            "height" : root.winfo_screenheight()
        }
    }

def pytest_html_report_title(report):
    report.title = PROJECT_NAME

def pytest_configure(config):
    config._metadata["Tester Name"] = TESTER_NAME

@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session, exitstatus):
    session.config._metadata["Tester Name"] = TESTER_NAME

