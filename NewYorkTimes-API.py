import requests

# signup for your own api key
api_key = "xGP9LFHMtESOxR0QonAC1wXyDCZPGkff"

search = input("search by the name of your desired country name=====>  ")
my_url = f"https://api.nytimes.com/svc/search/v2/articlesearch.json?q={search}&api-key={api_key}"

call = requests.get(my_url)
print(call)
print(call.headers)
print(call.headers['date'])
print(call.headers['Content-Type'])

jason_call = call.json()

print("======================================================================")

num = 1
for element in jason_call["response"]["docs"]:
    print(f"Article: {num}")
    print(element["headline"]["main"])
    print(element["abstract"])
    print(element["pub_date"] + "\n")
    num += 1
