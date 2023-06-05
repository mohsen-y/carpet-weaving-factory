from fastapi.testclient import TestClient
from fastapi import status
from main import app

client = TestClient(app=app)

def test_get_list_of_carpets():
    response = client.get(url="/api/carpets")
    assert response.status_code == status.HTTP_200_OK


def test_assign_colors_to_areas():
    response = client.post(
        url="/api/assign-colors",
        json={
            "A": ["B", "C", "G"],
            "B": ["A", "C", "E", "H"],
            "C": ["A", "E"],
            "D": ["F", "G"],
            "E": ["B", "C"],
            "F": ["A", "H"],
            "G": ["A", "D", "H"],
            "H": ["B", "F", "G"],
        },
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "colored_areas": {
            "B": 0, "A": 1, "G": 0, "H": 1,
            "C": 0, "D": 1, "E": 1, "F": 0,
        },
        "min_colors": 2,
    }


def test_purchase_maximum_number_of_carpets():
    response = client.post(url="/api/purchase-carpets?budget=500")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == [
        {
            "name": "Carpet I",
            "price": 90,
        },
        {
            "name": "Carpet H",
            "price": 120,
        },
        {
            "name": "Carpet A",
            "price": 100,
        },
    ]


def test_find_nearest_factory_branch():
    response = client.post(url="/api/nearest-branch?start_point=D")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "start_point": "D",
        "destination": "J",
        "route": "D -> I -> E -> J",
        "distance": 3,
    }
