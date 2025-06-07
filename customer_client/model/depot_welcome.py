from service import ServerRequest


class Welcome:
    def __init__(self):
        self.url_part = ""
        self.response = ""

    def customer_name(self, token):
        server_request = ServerRequest()
        success, self.response = server_request.get_without_parameters(self.url_part, token)
        return success
