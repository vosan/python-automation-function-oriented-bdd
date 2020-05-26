from behave import *
from environment import get_driver

use_step_matcher("re")

# @given - Pre-condition, start point of the test
# @when - Action (click button, enter text, etc.)
# @then - Verification of some result
# And - Continues previous statement (Given, When, Then)


@given("User is on the Home page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    get_driver().get("https://www.walmart.com")