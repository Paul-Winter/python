import requests
import urllib3

userdata = {
    'login': 'student',
    'password': 'qwerty1234',
    'email': 'sdlkfjsdfk@dlfkj.dk',
    'phone': '+7(987)654-32-10'
}

response = requests.post("https://httpbin.org/post", data=userdata, verify=False)
print(response.status_code)
print(response.text)