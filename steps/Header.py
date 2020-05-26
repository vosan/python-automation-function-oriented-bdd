from behave import *
from environment import get_driver

use_step_matcher("re")

# @given - Pre-condition, start point of the test
# @when - Action (click button, enter text, etc.)
# @then - Verification of some result
# And - Continues previous statement (Given, When, Then)


@when('Header - Click (Pickup & delivery|Walmart.com) header tab')
def step_impl(context, button_name):
    locator = '//div[@id="header-tabs"]//a[@title="' + button_name + '"]'
    get_driver().find_element_by_xpath(locator).click()


@when('Header - Click on Hamburger menu header tab')
def step_impl(context):
    locator_ham_menu = '//button[@data-tl-id="header-Header-sparkButton"]'
    get_driver().find_element_by_xpath(locator_ham_menu).click()

@when('Header - Click on Home page')
def step_impl(context):
    locator_header_w = '//a[@id="hf-home-link"]'
    get_driver().find_element_by_xpath(locator_header_w).click()

@when('Header - Click on dropdown toggle')
def step_impl(context):
    locator_dd_toggle = '//button[@id="global-search-dropdown-toggle"]'
    get_driver().find_element_by_xpath(locator_dd_toggle).click()

@when('Header - Click on Baby from dropdown menu')
def step_impl (context):
    locator_filter = '//div[@role="menu"]//button[@data-catid="5427"]'
    get_driver().find_element_by_xpath(locator_filter).click()

@when('Header - Click on search field')
def step_impl(context):
    locator_search_field = '//input[@id="global-search-input"]'
    get_driver().find_element_by_xpath(locator_search_field).click()

@when('Type in "Liza"')
def step_impl(context):
    locator_search_field = '//input[@id="global-search-input"]'
    get_driver().find_element_by_xpath(locator_search_field).send_keys("Liza")

@when('Header - Click on Account header tab')
def step_impl(context):
    locator_account = '//button[@id="header-account-toggle"] '
    get_driver().find_element_by_xpath(locator_account).click()

@when('Header - Click on Reorder header tab')
def step_impl(context):
    locator_reorder = '//a[@aria-label="Reorder"] '
    get_driver().find_element_by_xpath(locator_reorder).click()


@when('Header - Click on Cart icon')
def step_impl(context):
    locator_cart_icon = '//div[@id="header-bubble-links"]//a[starts-with(@aria-label,"Cart")] '
    get_driver().find_element_by_xpath(locator_cart_icon).click()

@when('Header - Click on Cart tooltip')
def step_impl(context):
    locator_cart_tooltip = '//div[@id="header-bubble-links"]//div[@id="header-cart-tooltip"] '
    get_driver().find_element_by_xpath(locator_cart_tooltip).click()


