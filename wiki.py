import requests

search_term = str(input("enter search term: "))
response = requests.get(
    'https://en.wikipedia.org/w/api.php',
    params={
        'action': 'query',
        'format': 'json',
        'titles': search_term,
        'prop': 'extracts',
        'exintro': 1,
        'explaintext': 1,
    }
).json()

page = next(iter(response['query']['pages'].values()))

output = []

try:
    for i in page['extract']:
        output.append(i)
        if i == '\n':
            break
        else:
            continue
except:
    print("Search term could not be found")

string = ""
print(string.join(output))
