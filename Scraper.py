# WebScraper for pulling images from www.airliners.net
import requests
from bs4 import BeautifulSoup
import os
import pandas as pd

# AirlinersIDS.csv contains a lookup table for IDs:Aircraft Name

# CSV Data was pulled using the following javascript on www.airliners.net/search:
#   $x('//*[@class="selectize-dropdown-content"]//div').forEach(function(item) {
#       console.log(item.getAttribute("data-value") + "," + item.innerText)
#   })

# Search is of form:
#   http://www.airliners.net/search?aircraftBasicType={ID}&sortBy=dateAccepted&sortOrder=desc&perPage=84&display=card
# Where {ID} corresponds to the ID found in AirlinersIDS.csv

# On each page, images can be found with:
#   $x("//*[@class='card-image']//a//img").forEach(function(item) {console.log(item.src)})

lookup_table = pd.read_csv("AirlinersIDSQuarter1.csv")
aircraft_dict = dict(zip(lookup_table.ID, lookup_table.Aircraft))
i = 0

for k, v in aircraft_dict.items():
    i = i + 1
    aircraft_id = k
    aircraft_model = v
    aircraft_model = aircraft_model.replace("/", "")

    print("Starting on {0} (Aircraft {1})".format(aircraft_model, str(i)))
    directory = os.getcwd() + "\\{}".format(aircraft_model).replace(" ", "")
    os.mkdir(directory)

    page = 1
    while True:
        path = "http://www.airliners.net/search?aircraftBasicType={}&sortBy=dateAccepted".format(str(aircraft_id))\
               + "&sortOrder=desc&perPage=84&display=card&page={}".format(str(page))
        print("Path = {}".format(path))
        page = page + 1
        r = requests.get(path)
        data = r.text
        soup = BeautifulSoup(data, "html5lib")
        num_found = 0
        
        # for link in soup.find_all("img"):
        #    image = link.get("src")
        #    if image.startswith("http://imgproc.airliners.net/photos/airliners/"):
    
        for link in soup.find_all(class_='card-image'):
            image = link.find('img').get('src')
            
            num_found = num_found = 1
            image_name = os.path.split(image)[1]
            r2 = requests.get(image)
            with open(directory + "\\" + image_name, 'wb') as f:
                f.write(r2.content)

        if num_found == 0:
            break
