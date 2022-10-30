import googlemaps

gmaps = googlemaps.Client(key="AIzaSyAsqDyB0mVXl9gbM_jyGV9W2Ocxa4BQaXQ")


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
        place = {item['name']: (item['geometry']['location']['lat'], item['geometry']['location']['lng']), "Address": item['formatted_address'],
                 "reference_id": item['photos'][0]['photo_reference']}
        list_of_tourist_places.append(place)

    return [list_of_tourist_places]







