import folium

map = folium.Map(location=[80, -100])
print(map)

map.save("Map2.html")
