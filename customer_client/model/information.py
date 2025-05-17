from .server_request import ServerRequest


class Information:
    def __init__(self):
        self.url_part = "information/"
        self.response = ""
        self.server_request = ServerRequest()

    def get_information(self):

        success, self.response = self.server_request.get_without_parameters(self.url_part)
        return success
