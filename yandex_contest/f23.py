import requests
import pickle


url = "https://jsonplaceholder.typicode.com/"

users = requests.get(f"{url}users").json()
users = {
    user["id"]: {
        "id": user["id"],
        "username": user["username"],
        "email": user["email"],
        "posts": 0,
        "comments": 0
    }
    for user in users
}

posts = requests.get(f"{url}posts").json()
for post in posts:
    users[post["userId"]]["posts"] += 1

users = {user["email"]: user for user in users.values()}

comments = requests.get(f"{url}comments").json()
for comment in comments:
    if comment["email"] in users:
        users[comment["email"]]["comments"] += 1

users = list(users.values())

response = requests.post("https://webhook.site/a322c46f-1d33-4a73-a897-9a4e80a49cf7/715e8633-383e-4e1c-b617-6c09fb3efa8c", json={"statistics": users})

with open("solution.py", "wb") as f:
    pickle.dump(response, f)