import requests

response = requests.get('https://api.github.com/users/devAnnaEliza/repos')

# check if the request was successful
#print(response.status_code)

#print(response.headers['Content-Type'])

for item in range(len(response.json())):
    print((response.json()[item]['name']))
    