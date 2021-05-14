import requests
from time import sleep

url = "https://google.com/"

response = requests.get(url)
while response != []:
    if response.status_code == 200:
        print(response.status_code)
        print("Attempt to fetch google.com: Success!")
        print(response.elapsed)
    else: 
        print(response.status_code)
        print("Attempt to fetch google.com: Unsucessful")
    sleep (60)
