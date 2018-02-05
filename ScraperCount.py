# WebScraper for pulling images from www.airliners.net
import requests
from bs4 import BeautifulSoup
import os
import pandas as pd
import csv

lookup_table = pd.read_csv("AirlinersIDSSelect.csv")
aircraft_dict = dict(zip(lookup_table.ID, lookup_table.Aircraft))
total_vector = dict()
i = 0

for k, v in aircraft_dict.items():
    i = i + 1
    aircraft_id = k
    aircraft_model = v
    aircraft_model = aircraft_model.replace("/", "")
    aircraft_model = aircraft_model.replace("...", "[]")

    print("Starting on {0} (Aircraft {1})".format(aircraft_model, str(i)))

    page = 1
    total_found = 0
    path = "http://www.airliners.net/search?aircraftBasicType={}&sortBy=dateAccepted".format(str(aircraft_id))\
           + "&sortOrder=desc&perPage=84&display=card&page={}".format(str(page))
    print("Path = {}".format(path))
    r = requests.get(path)
    data = r.text
    soup = BeautifulSoup(data, "html5lib")
    total_found = int(str(soup.find_all("strong")[2]).replace(',', '').replace("<strong>", "").replace("</strong>", ""))

    total_vector[k] = total_found

with open('totals.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    for k, v in total_vector.items():
        writer.writerow([str(k), str(v)])