import requests

# Collect URL from Wiki
headers = {
    'User-Agent': 'MyCustomUserAgent/1.0'
}

result = requests.get('https://en.wikipedia.org/wiki/Special:Random', headers=headers)
read_url = result.request.url

# Post URL
data = {
    'todo': f"Read: {read_url}",
}

response = requests.post('http://the-project-app-svc:5000/', data=data)
