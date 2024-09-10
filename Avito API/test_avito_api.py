from typing import Literal
import requests
import pytest
from endpoints.create_advert import CreateAdvert
from endpoints.get_advert_by_id import GetAdvertById
from endpoints.get_all_adverts import GetAllAdverts

@pytest.mark.parametrize(
    'data_create_advert_positive', 
    [
    pytest.param(({"name": "Авито 52","price": 152,"sellerId": 525252,"statistics": {"contacts": 252,"likes": 352,"viewCount": 452}}), id='sellerId=525252 exist')
    ]
)
def test_create_advert_positive(data_create_advert_positive):
    new_advert_endpoints = CreateAdvert()
    payload = data_create_advert_positive
    new_advert_endpoints.new_advert(payload)
    new_advert_endpoints.check_response_is_200()
    new_advert_endpoints.chek()

@pytest.mark.parametrize(
    'data_create_advert_negative', 
    [
    pytest.param(({"name": "Авито 52","price": 152,"sellerId": 123147,"statistics": {"contacts": 252,"likes": 352,"viewCount": 452}}), id='sellerId=123147 doesnt exist'),
    pytest.param(({"name": "","price": 152,"sellerId": 123147,"statistics": {"contacts": 252,"likes": 352,"viewCount": 452}}), id='name advert empty'),
    pytest.param(({"name": "Авито 52","price": -152,"sellerId": 525252,"statistics": {"contacts": 252,"likes": 352,"viewCount": 452}}), id='price=-152 negative'),
    pytest.param(({"name": "Авито 52","price": 152,"sellerId": -525252,"statistics": {"contacts": 252,"likes": 352,"viewCount": 452}}), id='sellerId=-525252 negative'),
    pytest.param(({"name": "Авито 52","price": 152,"sellerId": 525252,"statistics": {"contacts": -252,"likes": 352,"viewCount": 452}}), id='contacts=252 negative'),
    pytest.param(({"name": "Авито 52","price": 152,"sellerId": 525252,"statistics": {"contacts": 252,"likes": -352,"viewCount": 452}}), id='likes=-352 negative'),
    pytest.param(({"name": "Авито 52","price": 152,"sellerId": 525252,"statistics": {"contacts": 252,"likes": 352,"viewCount": -452}}), id='viewCount=-452 negative')
    ]
)
def test_create_advert_negative(data_create_advert_negative):
    new_advert_endpoints = CreateAdvert()
    payload = data_create_advert_negative
    new_advert_endpoints.new_advert(payload)
    new_advert_endpoints.check_response_is_404()

@pytest.mark.parametrize(
    'data_advert_by_id_positive', 
    [
        pytest.param(('191382b2-562d-4b9e-98c2-c61a50763ccc'), id='id=191382b2-562d-4b9e-98c2-c61a50763ccc exists')
    ]
)
def test_get_advert_by_id_positive(data_advert_by_id_positive):
    get_advert_by_id_endpoints = GetAdvertById()
    id = data_advert_by_id_positive
    get_advert_by_id_endpoints.get_by_id(id)
    get_advert_by_id_endpoints.check_response_is_200()
    get_advert_by_id_endpoints.check()

@pytest.mark.parametrize(
    'data_advert_by_id_negative', 
    [
        pytest.param(('191382b2-562d-4b9e-98c2-c61a50763c52'), id='id=191382b2-562d-4b9e-98c2-c61a50763c52 doesnt exist'),
        pytest.param((), id='id empty'),
        pytest.param(('qwerty'), id='id string'),
        pytest.param((-123456), id='id negative'),
        pytest.param((0), id='id=0')
    ]
)
def test_get_advert_by_id_negative(data_advert_by_id_negative):
    get_advert_by_id_endpoints = GetAdvertById()
    id = data_advert_by_id_negative
    get_advert_by_id_endpoints.get_by_id(id)
    get_advert_by_id_endpoints.check_response_is_404()

@pytest.mark.parametrize(
    'data_all_advert_positive', 
    [
        pytest.param((525252), id='id=525252 exists')
    ]
)
def test_get_all_advert_positive(data_all_advert_positive):
    get_all_advert = GetAllAdverts()
    id = data_all_advert_positive
    get_all_advert.get_all_adverts(id)
    get_all_advert.check_response_is_200()
    get_all_advert.check()


@pytest.mark.parametrize(
    'data_all_advert_negative', 
    [
        pytest.param((123149), id='id=123149 doesnt exist'),
        pytest.param((), id='id= empty'),
        pytest.param(('qwerty'), id='id=qwerty string'),
        pytest.param((-123456), id='id=-123456 negative')
    ]
)
def test_get_all_advert_negative(data_all_advert_negative):
    get_all_advert = GetAllAdverts()
    id = data_all_advert_negative
    get_all_advert.get_all_adverts(id)
    get_all_advert.check_response_is_404()
