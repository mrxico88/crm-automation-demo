from page_objects.BaseObject import BaseObject


class Navigation(BaseObject):

    accountsLocator = "div[title=Accounts]"

    def __init__(self):
        super(Navigation, self).__init__()

    def open_accounts(self):
        self.browser.click(self.accountsLocator)
