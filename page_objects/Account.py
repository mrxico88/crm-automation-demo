import uuid
from page_objects.BaseObject import BaseObject
from Browser import SupportedBrowsers
from Browser import ElementState


class Account(BaseObject):

    addNewAccountButtonLocator = "img[title=New]"
    accountTitleLocator = "h1[data-id='header_title']"
    accountNameInputBoxLocator = "input[aria-label='Account Name']"
    saveButtonLocator = "button[aria-label='Save (CTRL+S)']"

    accountName = 'Qaraton' + str(uuid.uuid4())
    
    def __init__(self):
        super(Account, self).__init__()

    def create_new_account(self):
        self.click_and_wait_for_element_state(self.addNewAccountButtonLocator, self.accountTitleLocator, ElementState.visible)
        self.browser.click(self.accountNameInputBoxLocator)
        self.browser.type_text(self.accountNameInputBoxLocator, self.accountName)
        self.browser.click(self.saveButtonLocator)

    def assert_created_account_has_correct_name(self):
        assert self.accountName in self.browser.get_text(self.accountTitleLocator)
