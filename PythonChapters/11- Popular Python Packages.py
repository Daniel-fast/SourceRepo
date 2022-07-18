
== == == == == == == == == == == ==  4- Searching for Businesses  == == == == == == == == == == == ==
import requests
import config

api_endpoint_url = "https://api.yelp.com/v3/businesses/search"

client_id = "mtjCDf1ZPxNskG8TnS-xSw"


location = "São Paulo"

term = "restaurants"

params = {
    "term": term,
    "location": location
}

headers = {
    "Authorization": "Bearer " + config.api_key
}

response = requests.get(api_endpoint_url, headers=headers, params=params)

businesses = response.json()["businesses"]
names = [business["name"]
         for business in businesses if business["rating"] > 3]

print(names)


# for business in businesses:
#     print(business["name"])



