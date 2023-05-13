
PLATFORM = {
    'realtime': 'REALTIME',
    'webphone': 'WEBPHONE'
}


class Error(Exception):
    def __init__(self, locator, typing, platform, method, page):
        self.locator = locator[1]
        self.typing = typing
        self.page = page
        self.platform = platform
        self.method = method

    def message(self):
        return f'{self.platform.upper()} | {self.typing} - {self.locator} | Page: {self.page} - Method: {self.method}'
