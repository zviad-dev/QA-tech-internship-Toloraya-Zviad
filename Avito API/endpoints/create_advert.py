import requests
from .base_endpoint import Endpoint

class CreateAdvert(Endpoint):


    def new_advert(self, payload):
        self.response = requests.post('https://qa-internship.avito.com/api/1/item', json=payload)
        self.response_json = self.response.json() 

    def chek(self):
        assert 'Сохранили объявление' in self.response_json['status'] 
    