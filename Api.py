import requests
import time


def get_data(api):
    response = requests.get(api)
    if response.status_code == 200:
        print("data fetched sucessfully :D")
        return response.json()
    else:
        print(response.status_code)


def get_dog_data():
    api_dog = 'http://dog-api.kinduff.com/api/facts'
    data = get_data(api_dog)['facts'][0]
    while len(data) > 280:
        print(len(data))
        data = get_data(api_dog)['facts'][0]
    return data


def get_cat_data():
    api_cat = "https://meowfacts.herokuapp.com/?count=1"
    data = get_data(api_cat)['data'][0]
    print(len(data))
    while len(data) > 280:
        print(len(data))
        data = get_data(api_cat)['data'][0]
    return data


if __name__ == "__main__":
    print("hello")
