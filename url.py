import requests
from time import sleep

url = "https://google.com/"
fail_url = "https://httpbin.org/status/404"

response = requests.get(fail_url)
while response != []:
    if response.status_code == 200:
        print(response.status_code)
        print("Attempt to fetch google.com: Success!")
        print(response.elapsed)
    else: 
        print(response.status_code)
        print("Attempt to fetch google.com: Unsucessful")
    sleep (60)