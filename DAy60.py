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

print("-" * 40)

# Check POST request response

print("Status Code:", response.status_code)

print("Response:")
print(response.json())

print("-" * 40)

# GET data from API

get_url = "https://jsonplaceholder.typicode.com/posts/1"

get_response = requests.get(get_url)

print("GET Status Code:", get_response.status_code)

post = get_response.json()

print("Post ID:", post["id"])
print("User ID:", post["userId"])
print("Title:", post["title"])
print("Body:", post["body"])

print("-" * 40)

# Check Request Success

if get_response.status_code == 200:
    print("API Request Successful")
else:
    print("API Request Failed")

