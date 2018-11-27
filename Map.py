
import folium
import pandas
#open the volcanoes file into python for reading
data = pandas.read_csv("/Users/mehakkumar/Desktop/Mapping/Volc.csv")
#create two diffrent lists for latitute and longitude
lat = list(data["LAT"])
lon = list(data["LON"])
name = list(data["NAME"])
loc = list(data["LOCATION"])
ele = list(data["ELEV"])
def color_producer(elevation):
    if elev <= 1000:
        return "#008000";
    elif elev <= 2000:
        return "#0000ff"
    elif elev <= 3000:
        return "#ff0000"
    else:
        return "#000000"

 #make the base map object
map = folium.Map(location = [38.58,-99.09], zoom_start = 6,tiles = "Mapbox Bright")
#
fgv = folium.FeatureGroup(name = "Volcaoes")
for lt, lg, name, loc, elev in zip(lat,lon, name, loc, ele):

    fgv.add_child(folium.CircleMarker(location = [lt,lg], popup = "Mount " +name + "| Location: " + loc + "| Elevation: " + str(elev), radius = 4, color = color_producer(elev), fill_color = color_producer(elev), fill_opacity = 0.7))

fgp = folium.FeatureGroup(name = "Population")


fgp.add_child(folium.GeoJson(data = open('world.json', 'r', encoding ='utf-8-sig').read(),
style_function = lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] <= 20000000  else 'red'}))
map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())


map.save("Map12.html")
