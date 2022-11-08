from unittest import TestCase, main, mock
import json
import requests
from config import google_maps_key
from google_maps import geocode_city, list_of_places, display_attractions
import googlemaps



class GoogleMapsTest(TestCase):

    # coordinates from google maps
    budapest = [47.497912, 19.040235]
    london = [51.5072178, -0.1275862]
    prague = [50.0755381, 14.4378005]
    barcelona = [41.3873974, 2.168568]

    def test_gmaps_key(self):
        self.gmaps_client = googlemaps.Client(google_maps_key)
        output = self.gmaps_client.geocode("Budapest")
        self.assertEqual(list(output[0].keys()), ['address_components', 'formatted_address', 'geometry', 'place_id', 'types'])

    def test_geocode(self):
        self.assertEqual(geocode_city("Budapest"), self.budapest)
        self.assertEqual(geocode_city("London"), self.london)
        self.assertEqual(geocode_city("Prague"), self.prague)
        self.assertEqual(geocode_city("Barcelona"), self.barcelona)


if __name__ == '__main__':
    main()