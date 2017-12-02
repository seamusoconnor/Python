import json
import xml.etree.ElementTree

import requests

response = requests.get("https://data.dublinked.ie/cgi-bin/rtpi/realtimebusinformation?stopid=1904&format=xml")

e = xml.etree.ElementTree.parse(response)

print e.findall("route")
#print response.txt

#json_data = json.loads(response.text)


#response = response.text

#print response





#for line in json_data["results"]:

    #print "timestamp {}".format(line["timestamp"])


 #   print "\n\n","Route {} From {} to {}".format(line["route"], line["origin"], line["destinationlocalized"])
  #  print "Time to this stop is: {} minutes".format(line["departureduetime"])
   # break





