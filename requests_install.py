import requests

# creating a GET request
r = requests.get('https://jsonplaceholder.typicode.com/posts/1')

response_dict = r.json
response_header = r.headers
status_code = r.status_code

print(response_dict, "\n")
print(response_header, "\n")
print(status_code, "\n")

r = requests.put(
    url='https://jsonplaceholder.typicode.com/posts/1',
    data={"id": 1, "content": "hello world"},
    headers={"Content-Type": "application/json"}
    )

print(response_dict, "\n")
print(response_header, "\n")
print(status_code, "\n")