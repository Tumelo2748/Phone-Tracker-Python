import phonenumbers
import opencage
import folium

from myphone import number 

from phonenumbers import geocoder 

pepnumber = phonenumbers.parse(number, "ZA")
location = geocoder.description_for_number(pepnumber, "en")
print("Location: ", location)

from phonenumbers import carrier 
service_pro = phonenumbers.parse(number, "ZA")
print(carrier.name_for_number(service_pro, "en"))

from opencage.geocoder import OpenCageGeocode
# opencage api key
key = ''

geocoder = OpenCageGeocode(key)
guery = str(location)
results = geocoder.geocode(guery)
#print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat, lng)

myMap = folium.Map(location = [lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=location).add_to(myMap)

myMap.save("Mylocation.html")
