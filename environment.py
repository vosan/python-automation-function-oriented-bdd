from behave.model_core import Status
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import datetime
import time
import os
import sys


url = "https://www.walmart.com"     # url for local run

# set chromedriver_path value to point to .../chromedrivers/mac or .../chromedrivers/windows
# OR!!! don't be lazy and just add chromedriver to your PATH
chromedriver_path = "/Users/vn0u0xm/git_repos/python-automation-function-oriented-bdd/chromedrivers/mac/chromedriver"


# Chrome download friendly profile
chrome_profile = webdriver.ChromeOptions()
profile_prefs = {"plugins.plugins_list": [{"enabled": False,
                                           "name": "Chrome PDF Viewer"}]}
chrome_profile.add_experimental_option("prefs", profile_prefs)
chrome_profile.add_argument('--dns-prefetch-disable')
chrome_capabilities = DesiredCapabilities.CHROME
chrome_capabilities['loggingPrefs'] = {'browser': 'ALL'}


# Firefox download friendly profile
profile = webdriver.FirefoxProfile()
profile.set_preference('browser.download.folderList', 2)
profile.set_preference('browser.download.manager.showWhenStarting', False)
profile.set_preference('browser.download.panel.shown', False)
profile.set_preference('browser.helperApps.neverAsk.openFile', 'application/pdf')
profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/pdf, text/plain, application/vnd.ms-excel, text/csv, text/comma-separated-values, application/octet-stream, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
profile.set_preference('browser.helperApps.alwaysAsk.force', False)
profile.set_preference('pdfjs.disabled', True)
profile.set_preference('plugin.scan.plid.all', False)
profile.set_preference('plugin.scan.Acrobat', '99.0')


def get_driver():
    """
    webdriver wrapper
    """
    return driver


def close_all_alerts():
    try:
        alert = get_driver().switch_to.alert
        alert.accept()
        time.sleep(2)
        close_all_alerts()
    except:
        return


def before_all(context):
    """
    before_all : a set of actions to do before any steps are executed
    """
    print(sys.version)
    print('\n LOCAL RUN \n')


def before_scenario(context, scenario):
    global driver
    global start
    start = datetime.datetime.now()
    for i in ["\n", "*" * 60, "*" * 60, "*" * 60, "[ " + scenario.name + " ] has began", "*"*60, "*"*60, "*"*60, "\n"]:
        print(i)

    driver = webdriver.Chrome(chrome_options=chrome_profile, executable_path=chromedriver_path)
    driver.set_window_size(1024, 768)   # setup browser resolution
    driver.implicitly_wait(15)          # setup implicit wait
    driver.set_page_load_timeout(120)   # setup page load timeout
    driver.get(url)                     # open the page


def after_step(context, step):
    if step.status == Status.failed:
        global failedStepName
        failedStepName = step.name
        for entry in driver.get_log('browser'):
            print('\n', entry)


def after_scenario(context, scenario):
    close_all_alerts()
    stop = datetime.datetime.now()
    try:
        if scenario.status == Status.failed:
            filename = "[ " + scenario.name + " ]" + " - " + failedStepName.replace("\"", "") + " - " + time.strftime("%d-%m-%Y %I-%M %p") + ".png"
            path = os.path.abspath("failed_scenarios")
            if not os.path.exists(path):
                os.makedirs(path)
            fullpath = os.path.join(path, filename)
            print(scenario.name, " - FAILED")
            number_of_files = len([item for item in os.listdir(path) if os.path.isfile(os.path.join(path, item))])
            get_driver().save_screenshot(fullpath)
            if not len([item for item in os.listdir(path) if os.path.isfile(os.path.join(path, item))]) == number_of_files + 1:
                print('Screenshot has not been saved')
            else:
                print("Screenshot with a failure has been saved")
        else:
            print("\nPASSED\n")
    finally:
        print('Finished in    ', (stop - start).total_seconds())
        driver.delete_all_cookies()
        driver.quit()
