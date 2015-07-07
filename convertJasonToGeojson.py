import urllib2
import json
import os


response = urllib2.urlopen(os.sys.argv[1])
data = json.load(response)   
# The "shape" attribute in this dataset is called "location"
# The geometry type is point

# the head of the geojson file
output = \
    ''' \
{ "type" : "FeatureCollection",
    "features" : [
    '''

template = \
    ''' \
    { "type" : "Feature",
      "geometry" : { "type" : "Point", "coordinates" : [%s,%s]},
      "properties" : %s
        }
    '''
for row in data:
	lat, lon = row["location"]['latitude'], row["location"]['longitude']
	del row["location"]
	allButShape = json.dumps(row)
	output += template % (lon, lat, allButShape)
	output += ","


# Deleting the last ","
output = output[:-1]
# the tail of the geojson file
output += \
    ''' \
    ]
}
    '''
# Check to see if the geojson is valid and if yes put it into a file
import requests
validate_endpoint = 'http://geojsonlint.com/validate'

if requests.post(validate_endpoint, data=output).json()['status'] == "ok":
# opens an geoJSON file to write the output to
	outFileHandle = open("output.geojson", "w")
	outFileHandle.write(output)
	outFileHandle.close()
else:
	print "geojson is NOT valid!"
