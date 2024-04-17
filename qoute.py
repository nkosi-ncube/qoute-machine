import requests


def get_quote(user_category):
    category = user_category
    api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
    response = requests.get(api_url, headers={'X-Api-Key': 'H6odIiPP40xwvWhH3xoYBQ==kZLWBhas1FD5YEkv'})
    if response.status_code == requests.codes.ok:
        return response.text
    else:
        print("Error:", response.status_code, response.text)

get_quote()   

# city = 'johannesburg'
# api_url = 'https://api.api-ninjas.com/v1/weather?city={}'.format(city)
# response = requests.get(api_url, headers={'X-Api-Key': 'H6odIiPP40xwvWhH3xoYBQ==kZLWBhas1FD5YEkv'})
# if response.status_code == requests.codes.ok:
#     print(response.text)
# else:
#     print("Error:", response.status_code, response.text)
