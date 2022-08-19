import folium
import geocoder
from geopy.geocoders import Nominatim

# pega o nome da cidade
g = geocoder.ip('me')
city = g.city

loc = Nominatim(user_agent="GetLoc")

# entering the location name
getLoc = loc.geocode(city)

# printing latitude and longitude
latitude = getLoc.latitude
longitude = getLoc.longitude
print(latitude, longitude)


# Criando mapa
m = folium.Map(
    location=[latitude, longitude],
    zoom_start=11, tiles='Stamen Toner'
)

#Criando marcador no mapa(point)
folium.Marker(location=[latitude, longitude],
              popup=city,
              icon=folium.Icon(color='blue', icon='info-sign')
              ).add_to(m)

'''
folium.CircleMarker(
    location=[latitude, longitude],
    radius=50,
    popup=city,
    color='blue',
    fill=True,
    fill_color='lightblue'
).add_to(m)
'''

#salva o arquivo em HTML
m.save(r'.\map.html')
