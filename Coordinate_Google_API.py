import pandas as pd
import googlemaps

api_key = ''
gmaps = googlemaps.Client(key=api_key)

df = pd.read_csv('arquivo_com_cep.csv')

unique_addresses = set(df['Endereco'])

latitudes = {}
longitudes = {}

for address in unique_addresses:
    geocode_result = gmaps.geocode(address)
    if len(geocode_result) > 0:
        lat = geocode_result[0]['geometry']['location']['lat']
        lng = geocode_result[0]['geometry']['location']['lng']
        
        latitudes[address] = lat
        longitudes[address] = lng

df['Latitude'] = df['Endereco'].map(latitudes)
df['Longitude'] = df['Endereco'].map(longitudes)

print(df)

df.to_csv('LatLon.csv', index=False)