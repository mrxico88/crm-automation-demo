from page_objects.BaseObject import BaseObject
from Browser import ElementState
from Browser import SupportedBrowsers


class Login(BaseObject):

    emailInputLocator = "input[placeHolder='Email address, phone number or Skype']"
    passwordInputLocator = "input[placeHolder='Password']"
    nextButtonLocator = "input[value='Next']"
    signInButtonLocator = "input[value='Sign in']"
    dontShowAgainLocator = "input[name='DontShowAgain']"
    yesButtonLocator = "button[id='acceptButton']"
    headerPictureLocator = "[id$='headerPicture']"
    viewAccountLocator = "[id$='viewAccount']"
    appBreadCumTextLocator = "[data-id='appBreadCrumbText']"

    def __init__(self):
        super(Login, self).__init__()

    def login_to_microsoft_dynamic_365(self):
        self.browser.new_browser(browser=SupportedBrowsers.chromium, headless=False)
        self.browser.new_page(self.config['APP']['URL'])
        self.browser.type_text(self.emailInputLocator, self.config['APP']['USERNAME'])
        self.browser.click(self.nextButtonLocator)
        self.browser.type_text(self.passwordInputLocator, self.config['APP']['PASSWORD'])
        self.browser.click(self.signInButtonLocator)
        self.browser.click(self.dontShowAgainLocator)
        self.click_and_wait_for_element_state(self.yesButtonLocator, self.appBreadCumTextLocator, ElementState.visible)

    def navigate_to_my_account(self):
        self.browser.click(self.headerPictureLocator)


