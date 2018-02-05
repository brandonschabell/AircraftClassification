# WebScraper for pulling images from www.airliners.net

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