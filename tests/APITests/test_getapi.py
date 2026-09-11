from playwright.sync_api import Playwright, Page    
from user import User
import json

# from typing import TypedDict

# class User(TypedDict):
#     id: int
#     name: str
#     username: str
#     email: str
#     address: dict
#     phone: str
#     website: str
#     company: dict

def save_session_data(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def test_login(page:Page):
    page.goto("https://puredevtools.tools/web-storage-explorer/")  # Navigate to the login page

    # page.locator("button:has-text('Login')").click()  # Click the login button
    # page.locator("button:has-text('Login')").click()  # Click the login button again
    page.wait_for_load_state("load")  # Wait for the page to fully load
    # assert page.title() == "JSONPlaceholder - Free Fake REST API"  # Verify the page title
    save_session_data(page.context.cookies(), "session_data.json")  # Save session data to a file

    
# def test_get_users(playwright: Playwright):
#     request = playwright.request.new_context(
#         base_url="https://jsonplaceholder.typicode.com/"
#     )

#     response = request.get("/users")
#    # print(response.json())
#     assert response.status == 200

#     onpremData = response.json()
#     save_session_data(onpremData, "onprem_data.json")
#     cloudData = response.json()


#     assert onpremData == cloudData, "On-prem and cloud data do not match"



    # user = User(
    #     data[0]["id"],
    #     data[0]["name"], 
    #     data[0]["username"],
    #     data[0]["email"],   
    #     data[0]["address"],
    #     data[0]["phone"],
    #     data[0]["website"],
    #     data[0]["company"]
    # )

    # users = [User(
    #     id=user_data["id"],
    #     name=user_data["name"],
    #     username=user_data["username"],
    #     email=user_data["email"],
    #     address=user_data["address"],
    #     phone=user_data["phone"],
    #     website=user_data["website"],
    #     company=user_data["company"]
    # ) for user_data in data]


   
    # users = []
    # for item in data:
    #     user = User(
    #         id=item["id"],
    #         name=item["name"],
    #         username=item["username"],
    #         email=item["email"],
    #         address=item["address"],
    #         phone=item["phone"],
    #         website=item["website"],
    #         company=item["company"]
    #     )
    #     users.append(user)


    # print("User ID:", users[0].id)
    # print("User Name:", users[0].name)
    # print("User Username:", users[0].username)
    # print("User Email:", users[0].email)
    # print("User Address:", users[0].address)
    # print("User Phone:", users[0].phone)

  