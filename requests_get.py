import requests



r = requests.get('http://10.20.78.204/xampp/')
print r.content
print