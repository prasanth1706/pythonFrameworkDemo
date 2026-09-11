from playwright.sync_api import Playwright

from typing import TypedDict

class User(TypedDict):
    id: int
    name: str
    username: str
    email: str
    address: dict
    phone: str
    website: str
    company: dict


def test_post_users(playwright: Playwright):
    request = playwright.request.new_context(
        base_url="https://jsonplaceholder.typicode.com/"
    )

    payload = {
        "name": "John Doe",
        "username": "johndoe",
        "email": "johndoe@example.com"
    }
    
    response = request.post("/users", data=payload)
   # print(response.json())
    data = response.json()
    assert response.status == 201
    assert data["name"] == "John"

  