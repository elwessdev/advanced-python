from pydantic import BaseModel, EmailStr

# class User(BaseModel):
#     id: int
#     name: str
#     email: EmailStr

# user = User(
#     id=1,
#     name="John Doe",
#     email="osama@aa.com"
# )

# print(user)

# user_json = user.model_dump_json()
# print(user_json)

# user_dict = user.parse_raw(user_json)
# print(user_dict)

import requests as req

# res = req.get("https://jsonplaceholder.typicode.com/users/1")
# print(res.json())

# p = req.post("https://jsonplaceholder.typicode.com/posts", json={
#     "title": "foo",
#     "body": "bar",
#     "userId": 1
# })
# print(p.json())

# try:
#     res = req.get("http://0.0.0.0/delay/10", timeout=5)
#     print(res.json())
# except req.exceptions.Timeout as err:
#     print(err)

# res = req.get("http://0.0.0.0/status/404")
# if req.status_codes!=200:
#     print("Error")

# res = req.get("http://0.0.0.0/headers",headers={
#     "Authorization": "Bearer 65746qs6dqs4d89qs4dqs6d84"
# })
# print(res.json())

from bs4 import BeautifulSoup
# res = req.get("http://0.0.0.0/html")
# res = req.get("https://www.lipsum.com/")
# soup = BeautifulSoup(res.content,"html.parser")
# print(soup.findAll("p")[0].text)
