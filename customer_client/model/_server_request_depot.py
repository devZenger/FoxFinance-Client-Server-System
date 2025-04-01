import requests


class ServerRequestDepot:
    def __init__(self, token):
        self.token = token
        self.url='http://127.0.0.1:8000'
        self.url_server_depot =  f'{self.url}/depot/'
        

    def process_response (self, server_response):   

        status_code = server_response.status_code
        
        try:                       
            server_response = server_response.json()
        except:
            pass        
    
        if status_code >= 200 and status_code <= 300:

            if "message" not in server_response:
                return True, server_response
            else:
                return True, server_response["message"] #server_response is dict or string

        else:            
            if "detail" not in server_response:
                server_response = {}
                server_response["detail"]= f"Unbekannter Fehler, Status Code: {status_code}"

            print(f"server_response (server_request_depot: z31): {server_response}")
            print(f"server_response[detail] (server_request_depot: z32): {server_response["detail"]}")

            return False, server_response["detail"] # server_response is string
        
            
    def _make_get_request(self, url):

        headers = { "Authorization": f"Bearer {self.token['access_token']}"}
        
        server_response = requests.get(url, headers=headers)
        
        return self.process_response(server_response)
 

    def get_without_parameters(self, url_part):
        
        url = f"{self.url_server_depot}{url_part}"
        
        print(f"url in get_without_parameters: {url}")
        
        return self._make_get_request(url)


    def get_with_parameters(self, url_part, *inputs):
        
        parameters = ""
        for input in inputs:
            parameters = f"{parameters}{input}/"
    
        url = f"{self.url_server_depot}{url_part}{parameters}"
        
        print(f"url in get_with_parameters: {url}")
        
        return self._make_get_request(url)



    def make_post_request(self, url_part, to_transmit):
        
        url = f"{self.url_server_depot}{url_part}"
        
        headers = { "Authorization": f"Bearer {self.token['access_token']}"}
        
        print(f"to_transmit = {to_transmit}")
        
        server_response = requests.post(url, json=to_transmit, headers=headers)
        
        return self.process_response(server_response)
        
        
