# Program to demonstrate clustering and K-Means
import numpy as np
import sklearn.cluster
# sklearn to perform various statistical analysis

data = np.arange(0,100)
# arange is a method that gives random values between 0 to 100
data = list(zip(data, data)) 

from sklearn.cluster import KMeans
# Pick 3 random values from the above list 
# cluster/group values that are close to it through KMeans algorithm
# find the centroid
model = KMeans(n_clusters=3, init='random', max_iter=50)
print(model.fit(data))
print(model.cluster_centers_) # finding centroids

# The Uber way
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

apr14 = pd.read_csv('uber-raw-data-apr14.csv')
may14 = pd.read_csv('uber-raw-data-may14.csv')
jun14 = pd.read_csv('uber-raw-data-jun14.csv')
jul14 = pd.read_csv('uber-raw-data-jul14.csv')
aug14 = pd.read_csv('uber-raw-data-aug14.csv')
sep14 = pd.read_csv('uber-raw-data-sep14.csv')
merged_df = pd.concat([apr14, may14, jun14, jul14, aug14, sep14])
# Date/Time determines the date and time of booking Lat and Lon determines the location
print(merged_df)

# String to datetime conversion
# Since we need date and time in numerical format from string we convert it
apr14['Date/Time'] = pd.to_datetime(apr14['Date/Time'], format='%m/%d/%Y %H:%M:%S')
may14['Date/Time'] = pd.to_datetime(may14['Date/Time'], format='%m/%d/%Y %H:%M:%S')
jun14['Date/Time'] = pd.to_datetime(jun14['Date/Time'], format='%m/%d/%Y %H:%M:%S')
jul14['Date/Time'] = pd.to_datetime(jul14['Date/Time'], format='%m/%d/%Y %H:%M:%S')
aug14['Date/Time'] = pd.to_datetime(aug14['Date/Time'], format='%m/%d/%Y %H:%M:%S')
sep14['Date/Time'] = pd.to_datetime(sep14['Date/Time'], format='%m/%d/%Y %H:%M:%S')
merged_df['Date/Time'] = pd.to_datetime(merged_df['Date/Time'], format='%m/%d/%Y %H:%M:%S')
dfs = [apr14, may14, jun14, jul14, aug14, sep14, merged_df]
current_df = dfs[0]

# Removing colons from Time
current_df['Time'] = current_df['Date/Time'].dt.time.apply(lambda x: int(x.strftime('%H%M%S')))
print(current_df)

# Histogram
sns.histplot(current_df['Time'])
plt.show()
# the count in graph shows the no of bookings

# Filtering morning and evening rides
morning_df_idx = (current_df['Time'] > 50000) & (current_df['Time'] < 110000)
morning_df = current_df[morning_df_idx]
evening_df_idx = (current_df['Time'] > 150000) & (current_df['Time'] < 220000)
evening_df = current_df[evening_df_idx]

print(morning_df)
print(evening_df)

morning_coordinates = morning_df[['Lat','Lon']].sample(10000,random_state = 10).values
evening_coordinates = evening_df[['Lat','Lon']].sample(10000,random_state = 10).values
# Picking 10000 bookings at random

import folium
# Plotting morning rides on map

# tiles is the styling of map
morning_map = folium.Map(location=[40.79658011772687, -73.87341741832425], zoom_start = 12, tiles='Stamen Toner')
for coordinate in morning_coordinates:
  folium.CircleMarker(radius=1,location=coordinate,fill=True).add_to(morning_map)
morning_map.save('map1.html')
# open with -> browser
# the blue dots represent the no of bookings made in the morning 

# Plotting evening rides on map
evening_map = folium.Map(location=[40.79658011772687, -73.87341741832425], zoom_start = 12, tiles='Stamen Toner')
for coordinate in evening_coordinates:
  folium.CircleMarker(radius=1,location=coordinate,color="#FF0000",fill=True).add_to(evening_map)
evening_map.save('map2.html')
# # the red dots represent the no of bookings made in the evening

from sklearn.cluster import KMeans
import numpy as np

# Finding clusters
# pick 6 random bookings from the list and find centroid

# for morning
n_clusters = 6
model = KMeans(n_clusters=n_clusters, init='random', max_iter=300)
print(model.fit(morning_df[['Lat','Lon']]))
morning_centroids = model.cluster_centers_
print(morning_centroids)

for i, coordinate in enumerate(morning_centroids):
    folium.Marker(coordinate, popup='Centroid {}'.format(i+1), icon=folium.Icon(color='red')).add_to(morning_map)
morning_map.save('map3.html')

# for evening
n_clusters = 6
model = KMeans(n_clusters=n_clusters, init='random', max_iter=300)
print(model.fit(evening_df[['Lat','Lon']]))
evening_centroids = model.cluster_centers_
print(evening_centroids)

for i, coordinate in enumerate(evening_centroids):
    folium.Marker(coordinate, popup='Centroid {}'.format(i+1), icon=folium.Icon(color='blue')).add_to(evening_map)
evening_map.save('map4.html')

# Finding clusters in whole selected dataframe
n_clusters = 8
model = KMeans(n_clusters=n_clusters, init='random', max_iter=300)
print(model.fit(current_df[['Lat','Lon']]))
centroids = model.cluster_centers_
print(centroids)

map = folium.Map(location=[40.79658011772687, -73.87341741832425], zoom_start = 12, tiles='Stamen Toner')
for i, coordinate in enumerate(centroids):
    folium.Marker(coordinate, popup='Centroid {}'.format(i+1), icon=folium.Icon(color='blue')).add_to(map)
map.save('map5.html')

# consider a new ride
new_ride = (40.70647056912189, -73.91116590442799)
folium.Marker(new_ride, popup='New Rider', icon=folium.Icon(color='green')).add_to(map)
map.save('map6.html')

# using predict function to find the nearest cab
centroid_idx = model.predict([new_ride])
centroids[centroid_idx]
folium.Marker(centroids[centroid_idx][0], icon=folium.Icon(color='yellow')).add_to(map)
map.save('map7.html')
