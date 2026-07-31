import requests
import pytest

base_url = "https://reqres.in/api/collections/products/records"

@pytest.fixture
def create_product():
    res = requests.post(
        base_url,
        params={
            "project_id" : 40413
        },
        headers={
            "x-api-key" : "pro_2719af3d179fb936e61a289425aeb8661fa255b9130a99c0a45a220e177f9d7b"
        },
        json={
            "data": {
                "name": "example",
                "price": "59.99",
                "category": "example",
                 "in_stock": True
             }
        }
    )

    yield res.json()["data"]["id"]

    requests.delete(
        base_url + "/" + res.json()["data"]["id"],
        params={
            "project_id" : 40413
        },
        headers={
            "x-api-key" : "pro_2719af3d179fb936e61a289425aeb8661fa255b9130a99c0a45a220e177f9d7b"
        }
    )

def test_products_list():

    res = requests.get(
        base_url,
        params={
            "project_id" : 40413
        },
        headers={
            "x-api-key" : "pro_2719af3d179fb936e61a289425aeb8661fa255b9130a99c0a45a220e177f9d7b"
        },
        
    )

    assert res.status_code == 200
    assert "data" in res.json()
    assert "meta" in res.json()
    assert res.json()["meta"]["total"] > 0

def test_get_product_id(create_product):

    res = requests.get(
        base_url + "/" + create_product,
        params={
            "project_id" : 40413
        },
        headers={
            "x-api-key" : "pro_2719af3d179fb936e61a289425aeb8661fa255b9130a99c0a45a220e177f9d7b"
        }
    )

    assert res.status_code == 200

def test_create_product():

    res = requests.post(
       base_url,
       params={
           "project_id" : 40413
        },
        headers={
        "x-api-key" : "pro_2719af3d179fb936e61a289425aeb8661fa255b9130a99c0a45a220e177f9d7b"
       },
       json={
            "data": {
                "name": "example",
                "price": 59.99,
                "category": "example",
                "in_stock": "example"
            }
        }
    )
    assert res.status_code == 201

def test_delete_product(create_product):

    res = requests.delete(
        base_url + "/" + create_product,
        params={
            "project_id" : 40413
        },
        headers={
        "x-api-key" : "pro_2719af3d179fb936e61a289425aeb8661fa255b9130a99c0a45a220e177f9d7b"
        },

    ) 
    assert res.status_code == 204