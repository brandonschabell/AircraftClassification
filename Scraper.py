# WebScraper for pulling images from www.airliners.net

# AirlinersIDS.csv contains a lookup table for IDs:Aircraft Name

# CSV Data was pulled using the following javascript on www.airliners.net/search:
#   $x('//*[@class="selectize-dropdown-content"]//div').forEach(function(item) {
#       console.log(item.getAttribute("data-value") + "," + item.innerText)
#   })