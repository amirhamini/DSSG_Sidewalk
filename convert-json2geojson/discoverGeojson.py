import urllib2
import json
import os
import requests

response = urllib2.urlopen("https://cdn.rawgit.com/amirhamini/DSSG_sidewalk/master/convert-json2geojson/crimeSeattle.geojason")
data = json.load(response)   
for element in data["features"]:
	print element["properties"]["offense_type"]
	

