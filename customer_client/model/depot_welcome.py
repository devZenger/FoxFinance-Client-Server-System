from service import ServerRequest


class Welcome:
    def __init__(self, token):
        self.server_request = ServerRequest(token)
        self.url_part = ""
        self.response = ""

    def customer_name(self):

        success, self.response = self.server_request.get_without_parameters(self.url_part)
        return success
