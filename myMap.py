import folium
import pandas
#open the volcanoes file
file = pandas.read_csv("volc.csv")
#get all the lat and longitude from the volcano file
lat = file['LAT']
lon = file['LON']
name = file['NAME']
elevation = file['ELEV']
#make a function for the type of color of the circle marker
def color_Marker(ele):
    if ele < 1000:
        return "red"
    elif ele <2000:
        return "green"
    elif ele < 3000:
        return "blue"
    else:
        return "black"
#this makes the map html and has it focused on the specific lat and long that you want it to see
map = folium.Map(location = [38.58,-99.09], zoom_start = 6, tiles= 'Mapbox Bright')
# makes a Volcanoes layed that you then add the volcano points on top of
fgv = folium.FeatureGroup(name = "Volcanoes")
# takes the lat and long from the csv file and uses a for loop to get all of them from the file
for lat , long, name, elev in zip(lat,lon,name,elevation):
    fgv.add_child(folium.CircleMarker(location = [lat, long], radius = 5, popup = "Mount " + name + " | Elevation: " + str(elev), fill_color = color_Marker(elev), fill_opacity = .75, color = color_Marker(elev)  ))
#makes a population layer
fgp = folium.FeatureGroup(name = "Population")
#takes the data from world.json and using the population changes the color of the countries
fgp.add_child(folium.GeoJson(data = open('world.json', 'r', encoding ='utf-8-sig').read(),
style_function = lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] <= 20000000  else 'red'}))
#adds the volcano layer to the base map
map.add_child(fgv)
#adds the population layer to the base map
map.add_child(fgp)
#allows you to toggle both the volcanoe and population
map.add_child(folium.LayerControl())
#saves the code to map1.html everytime its run
map.save("map1.html")
