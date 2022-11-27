from selene.support.shared import browser
from selene import be, have


def test_google_search_positive(open_browser):
    browser.element('[name="q"]').should(be.blank).type('selene python').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

def test_google_search_negative(open_browser):
    search = 'hhfhfhfieillls;smcm,vmvjfjk'
    browser.element('[name="q"]').should(be.blank).type(search).press_enter()
    browser.element('[id="result-stats"]').should(have.text('About 0 results'))