import requests


class ServerRequest:
    def __init__(self):

        self.url_server_base = 'http://127.0.0.1:8000/'

    def _get_header(self, token: str | None):
        if token is None:
            headers = None
            self.url_server = self.url_server_base

        else:
            headers = {"Authorization": f"Bearer {token['access_token']}"}
            self.url_server = f"{self.url_server_base}depot/"

        return headers

    def _process_response(sef, server_response: requests.models.Response):

        status_code = server_response.status_code

        try:
            server_response = server_response.json()

        except Exception:
            pass

        if status_code >= 200 and status_code <= 300:

            if server_response is None:
                return True, None
            elif "access_token" in server_response:

                return True, server_response

            else:
                # server_response is dict or string
                return True, server_response["message"]

        else:
            try:
                server_response = server_response.json()

            except Exception:
                pass

            if "detail" not in server_response:
                server_response = {}
                server_response["detail"] = f"Unbekannter Fehler, Status Code: {status_code}"

            # server_response is string
            return False, server_response["detail"]

    def _offline(self):
        return False, "Keine Verbindung zum Server."

    def _make_get_request(self, url: str, headers):
        try:
            server_response = requests.get(url, headers=headers)

            return self._process_response(server_response)
        except Exception:
            return self._offline()

    def get_without_parameters(self, url_part: str, token: str | None = None):

        headers = self._get_header(token)

        url = f"{self.url_server}{url_part}"

        return self._make_get_request(url, headers)

    def get_with_parameters(self, url_part: str, token: str | None = None, *inputs):

        headers = self._get_header(token)

        parameters = ""
        for input in inputs:
            parameters = f"{parameters}{input}/"

        url = f"{self.url_server}{url_part}{parameters}"

        return self._make_get_request(url, headers)

    def make_post_request(self, url_part: str, token: str | None, to_transmit: dict):

        headers = self._get_header(token)

        url = f"{self.url_server}{url_part}"

        try:
            server_response = requests.post(url, json=to_transmit, headers=headers)

            return self._process_response(server_response)
        except Exception:
            return self._offline()

    def make_delete_request(self, url_part: str, token: str, to_transmit):

        headers = self._get_header(token)
        url = f"{self.url_server}{url_part}"

        try:
            server_response = requests.delete(url, json=to_transmit, headers=headers)

            return self._process_response(server_response)
        except Exception:
            return self._offline()

    def make_patch_request(self, url_part: str, token: str, to_transmit):

        headers = self._get_header(token)
        url = f"{self.url_server}{url_part}"

        try:
            server_response = requests.patch(url, json=to_transmit, headers=headers)

            return self._process_response(server_response)

        except Exception:
            return self._offline()
