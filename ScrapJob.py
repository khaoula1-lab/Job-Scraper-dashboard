import requests
from bs4 import BeautifulSoup
import pymongo
from pymongo import MongoClient
import schedule
import time

client= MongoClient("mongodb://localhost:27017/")
#On définit la base de données et la collection
db = client["jobscrapper"]
collection = db["offres"]
#la fonction tourne toutes les heures pour scrapper les offres d'emploi

def scrap_offers():   
#le lien qu'on veut scrapper
    for page in range(1, 13):
        url=f"https://www.rekrute.com/offres.html?p={page}&s=1&o=1&query=data&keyword=data"

    #creer un user agent pour simuler un navigateur
        headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
    #GET request to the URL
        response= requests.get(url, headers=headers)
    #parser le html récupéré
        soup = BeautifulSoup(response.text, "html.parser")
    #trouver toutes les liens avec la classe titreJob
        offres= soup.find_all("a", class_="titreJob")
    #boucler sur chaque offre et récupérer le titre et le lien
        for offre in offres:
            titres= offre.text.strip()
            liens= offre["href"]
            ur="https://www.rekrute.com"+liens
            print(f"titre:{titres}, lien:{ur}")
       #On va séparer le poste et la ville
            if "|" in titres:
                parts= titres.split("|")
                poste= parts[0].strip()
                ville= parts[1].strip()
            else:
                poste= titres
                ville= "Non Précisé"
           
            offre_data = {
                "poste": poste,
                "ville": ville,
                "lien" : ur
            }
            collection.insert_one(offre_data) 

def job():
    print("Le Scrapper est en cours d'exécution...")
    scrap_offers()
schedule.every(1).hours.do(job)
job()
while  True:
    schedule.run_pending()
    time.sleep(1)