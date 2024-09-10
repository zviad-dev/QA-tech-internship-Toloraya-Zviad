import requests
from .base_endpoint import Endpoint

class GetAdvertById(Endpoint):


    def get_by_id(self, id):
        self.response = requests.get(f'https://qa-internship.avito.com/api/1/item/{id}')
        self.response_json = self.response.json() 

    def check(self):
        assert self.response_json == [{'createdAt': '2024-09-09 13:20:41.299586 +0300 +0300', 'id': '191382b2-562d-4b9e-98c2-c61a50763ccc', 'name': 'Авито 52', 'price': 152, 'sellerId': 525252, 'statistics': {'contacts': 252, 'likes': 352, 'viewCount': 452}}]