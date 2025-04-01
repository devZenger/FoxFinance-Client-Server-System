import requests


class ServerRequest:
    def __init__(self, token=None):
        self.token = token

        self.url_server = 'http://127.0.0.1:8000/'

        if self.token is None:
            self.headers = None

        else:
            self.headers = { "Authorization": f"Bearer {self.token['access_token']}"}
            self.url_server = f"{self.url_server}depot/"

    def process_response(sef, server_response):

        status_code = server_response.status_code

        try:
            server_response = server_response.json()
            print("server_response", server_response)
        except:
            pass

        print("server_response", server_response)

        if status_code >= 200 and status_code <= 300:

            if server_response is None: #or "message" not in server_response:
                return True, None
            elif "access_token" in server_response:
                return True, server_response

            else:
                return True, server_response["message"] #server_response is dict or string

        else:
            try:
                server_response = server_response.json()
                print("Ausgabe von server_response (server_request_depot: z23)", server_response)
            except:
                pass

            if "detail" not in server_response:
                server_response = {}
                server_response["detail"] = f"Unbekannter Fehler, Status Code: {status_code}"

            print(f"server_response (server_request_depot: z31): {server_response}")
            print(f"server_response[detail] (server_request_depot: z32): {server_response["detail"]}")

            return False, server_response["detail"] # server_response is string

    def _make_get_request(self, url):

        server_response = requests.get(url, headers=self.headers)

        return self.process_response(server_response)

    def get_without_parameters(self, url_part):

        url = f"{self.url_server}{url_part}"

        return self._make_get_request(url)

    def get_with_parameters(self, url_part, *inputs):

        parameters = ""
        for input in inputs:
            parameters = f"{parameters}{input}/"

        url = f"{self.url_server}{url_part}{parameters}"

        print(f"url in get_with_parameters: {url}")

        return self._make_get_request(url)

    def make_post_request(self, url_part, to_transmit):

        url = f"{self.url_server}{url_part}"

        print(f"url = {url}")

        print(f"to_transmit = {to_transmit}")

        server_response = requests.post(url, json=to_transmit, headers=self.headers)

        return self.process_response(server_response)
