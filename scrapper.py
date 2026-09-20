import requests
from bs4 import BeautifulSoup

url = "https://www.rekrute.com/offres.html?clear=1&keyword=data"
response = requests.get(url)

print("Status code:", response.status_code)
print("Longueur du HTML reçu:", len(response.text))

soup = BeautifulSoup(response.text, "html.parser")
offres = soup.find_all("a", class_="titreJob")
print("Nombre d'offres trouvées:", len(offres))