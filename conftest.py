from selene.support.shared import browser
import pytest


@pytest.fixture()
def open_browser():
    browser.config.window_height = 950
    browser.config._window_width = 1600
    browser.open('https://google.com/ncr')