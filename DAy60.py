import requests
response = requests.get("https://www.google.com")
print(response.text)

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title":'foo',
    "body":'bar',
    "userID": 1,

}
headers = {
    'Content-type': 'application/json; charset=UTF-8',
}
response = requests.post(url,headers=headers,json=data)