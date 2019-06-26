from behave import *
from environment import get_driver

use_step_matcher("re")


@given("User is on the Home page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    get_driver().get("https://www.walmart.com")
    print(u'STEP: Given User is on the Home page')