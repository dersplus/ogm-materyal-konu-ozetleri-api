import requests

# Konu özetlerinde arama yap
response = requests.get('https://api.dersplus.net/ogm/konu-ozetleri/search', params={'text': 'Arama parametreniz'})
print(response.json())

# Sınıf düzeylerini getir
response = requests.get('https://api.dersplus.net/ogm/konu-ozetleri/list-class')
print(response.json())

# Sınıfa göre konu özetlerini getir
response = requests.get('https://api.dersplus.net/ogm/konu-ozetleri/fetch-by-class', params={'id': 1})  # Buraya sınıf ID'nizi girin
print(response.json())
