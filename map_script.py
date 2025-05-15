import folium
# from IPython.display import display
import webbrowser


m = folium.Map(location=[30.741482,76.768066], zoom_start=13)
# display(m)
m.save("map.html")

webbrowser.open("map.html")