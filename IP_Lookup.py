import requests, urllib.parse, sys, json

def getgooglemapsurl(coords):
    coords1,coords2 = coords.split(',')
    unparsed = coords
    parsed = urllib.parse.quote(unparsed)
    url = "https://www.google.com/maps/place/"+parsed+"/@"+coords+",15.45z/data=!4m5!3m4!1s0x0:0x90713deb14e2f7db!8m2!3d"+coords1+"!4d"+coords2+""
    return url

v = json.loads(requests.get(f"http://ipinfo.io/{sys.argv[1]}/json").text)

print("\n      Results      ")
print("-------------------")
print("IP:",v['ip'])
print("Hostname:",v['hostname'])
print("City:",v['city'])
print("Region:",v['region'])
print("Country:",v['country'])
print("Location Coordinates:",v['loc'])
print("ORG:",v['org'])
print("Postal Code:",v['postal'])
print("Timezone:",v['timezone'])
print("Google Maps Link:",getgooglemapsurl(v['loc']))
