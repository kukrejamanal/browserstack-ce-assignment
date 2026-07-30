from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.safari.options import Options as SafariOptions

USERNAME = "manalkukreja_HjOYl1"
ACCESS_KEY = "ubgpxQsKkDTSJR3bVCsi"

URL = f"https://{USERNAME}:{ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub"


def create_browserstack_driver(platform):

    options = Options()

    options.set_capability(
        "browserName",
        platform["browserName"]
    )

    if "browserVersion" in platform:

        options.set_capability(
            "browserVersion",
            platform["browserVersion"]
        )

    bstack_options = {
        "projectName": "El Pais Scraper",
        "buildName": "BrowserStack Assignment",
        "sessionName": platform["name"]
    }

    if "os" in platform:
        bstack_options["os"] = platform["os"]

    if "osVersion" in platform:
        bstack_options["osVersion"] = platform["osVersion"]

    if "deviceName" in platform:
        bstack_options["deviceName"] = platform["deviceName"]

    options.set_capability(
        "bstack:options",
        bstack_options
    )

    return webdriver.Remote(
        command_executor=URL,
        options=options
    )