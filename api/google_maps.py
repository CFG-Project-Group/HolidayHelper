import googlemaps
from config import google_maps_key


# change the key to secret
gmaps = googlemaps.Client(key=google_maps_key)


# get the latlong coordinates given the name of the city
def geocode_city(city):
    geographic_coordinates = []
    geocoded = gmaps.geocode(city)
    geographic_coordinates = [geocoded[0]['geometry']['location']['lat'], geocoded[0]['geometry']['location']['lng']]
    return geographic_coordinates


def list_of_places(city):
    list_of_tourist_places = []
    coordinates = geocode_city(city)
    query_result = gmaps.places(query="tourist attraction", location=coordinates, radius=50000)
    for item in query_result['results']:
        if 'photos' in item:
            place = [item['name'], (item['geometry']['location']['lat'], item['geometry']['location']['lng']),
                     item['photos'][0]['photo_reference'], item['formatted_address']]
            list_of_tourist_places.append(place)
        else:
            continue

    return list_of_tourist_places


def display_attractions(city):
    attraction_attributes = []
    list_of_attractions = list_of_places(city)
    for item in list_of_attractions:
        name = item[0]
        address = item[3],
        photo_reference = f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photo_reference={item[2]}&key={google_maps_key}"
        attraction_attributes.append({'name': name, 'address': address, 'image': photo_reference})

    return attraction_attributes


if __name__ == '__main__':
    print(geocode_city("Budapest"))
    print(geocode_city("London"))
    print(geocode_city("Prague"))
    print(geocode_city("Barcelona"))

    print(list_of_places("Budapest"))
    print(list_of_places("London"))
    print(list_of_places("Prague"))
    print(list_of_places("Barcelona"))

    print(display_attractions("Budapest"))
    print(display_attractions("London"))
    print(display_attractions("Prague"))
    print(display_attractions("Barcelona"))







