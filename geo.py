import geopandas as gpd
import matplotlib.pyplot as plt

sa1 = gpd.read_file('Study_Area_1.shx')
sa2 = gpd.read_file('Study_Area_2.shx')
river= gpd.read_file('River.shx')


fig, ax = plt.subplots()
sa1.plot(ax=ax, color='blue', edgecolor='black')
sa2.plot(ax=ax, color='green', edgecolor='black')
river.plot(ax=ax, color='red', edgecolor='black')

#interasection of polygons
intersection = gpd.overlay(sa1, sa2, how='intersection')
intersection.plot(ax=ax, color='yellow', edgecolor='black')
# plt.show()

# union 
union = gpd.overlay(sa1, sa2, how='union')
union.plot(ax=ax, color='purple', edgecolor='black')
# plt.show()

