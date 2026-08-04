import requests

api_url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(api_url)

print(response)

print("status Code : ", response.status_code)
print(response.json())
#print(response.text)
