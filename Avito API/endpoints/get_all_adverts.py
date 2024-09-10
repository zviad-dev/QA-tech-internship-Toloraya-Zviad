import requests
from .base_endpoint import Endpoint

class GetAllAdverts(Endpoint):


    def get_all_adverts(self, id):
        self.response = requests.get(f'https://qa-internship.avito.com/api/1/{id}/item')
        self.response_json = self.response.json() 

    def check(self):
        assert len(self.response_json) > 0