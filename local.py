import requests

res = requests.post("http://127.0.0.1:3000/api/courses/3", json={"name": "Golang", "videos": 5})
res = requests.post("http://127.0.0.1:3000/api/courses/4", json={"name": "PHP", "videos": 13})
print(res.json())

# single entry display
# res = requests.get("http://127.0.0.1:3000/api/courses/1")

# delete record method
# res = requests.delete("http://127.0.0.1:3000/api/courses/1")