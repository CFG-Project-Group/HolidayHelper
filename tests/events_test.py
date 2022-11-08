from unittest import TestCase, main, mock
from api.events import Events
import json
import requests
from config import events_key



class MyTestEvents(TestCase):

    def test_request_response(self):
        # Send a request to the API server and store the response.
        city = 'London'
        url = f"https://serpapi.com/search.json?engine=google_events&q=Events+in+{city}&hl=en&apikey={events_key}"
        response = requests.get(url)

        # Confirm that the request-response cycle completed successfully.
        self.assertTrue(response.ok)

    def test_display_events_api_keys(self):
        event = Events()
        """Checking if keys hasn't changed - not values as values are not constant"""
        result = event.display_events('Budapest')[1]
        keys_to_compare = ['name', 'start_time', 'event_url', 'image', 'description']
        self.assertEqual(list(result.keys()), keys_to_compare)

    def mock_get_events_budapest(self):
        with open('mock_event_Budapest.json') as file:
            data = json.load(file)
            new_data = data["events_results"]
            return new_data

    @mock.patch('api.events.Events.get_events')
    def test_display_events_budapest(self, mock_get_events):
        event = Events()
        expected_response = [{'city': 'Budapest'},
 {'description': 'A heavy metal group from Copenhagen, Denmark, Volbeat '
                 "enjoyed success in the band's homeland during the early "
                 '2000s before earning international acclaim with records like '
                 "2013's Outlaw Gentlemen ...",
  'event_url': 'https://www.deezer.com/hu/artist/13953',
  'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTQ0Sfum2uMYYnlNN3XEG0ZkKIKNxnZqtVVe_Benc6Hfw&s=10',
  'name': 'Volbeat Budapest',
  'start_time': 'Sat, Nov 5, 18:30 – 23:00 GMT+1'},
 {'description': 'Apologies, no description available. Click the link for more '
                 'info',
  'event_url': 'https://www.ticketswap.com/event/boris-brejcha/9635f43d-a783-444f-b87d-18b988429487/info',
  'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRJKs3kZaOymTfTS-DESGMsaOTkD6qK_-az4HTPlHoXkznXbvjBFxunsl7lnrQt&s=10',
  'name': 'Boris Brejcha @ Budapest Arena',
  'start_time': 'Sat, Nov 5, 21:00 – Sun, Nov 6, 06:00 GMT+1'},
 {'description': 'ANNEKE VAN GIERSBERGEN acoustic - Budapest is on Facebook. '
                 'To connect with ANNEKE VAN GIERSBERGEN acoustic - Budapest, '
                 'join Facebook today.',
  'event_url': 'https://m.facebook.com/events/760557144895637/',
  'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTsUcnqn77flvNiptEj-k6rR1taHoBqS32vhSlUjAw_HQ&s=10',
  'name': 'ANNEKE VAN GIERSBERGEN acoustic - Budapest',
  'start_time': 'Sun, Nov 6, 19:00 – 23:00 GMT+1'},
 {'description': 'Apologies, no description available. Click the link for more '
                 'info',
  'event_url': 'https://www.salsamadras.com/event-details/all-stars-festival-budapest-2022',
  'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTijIaucePDd74xwk83UDxlph6OrxM6QtwIMvp5vhY3g2Og2krsJ7422niQ_A&s=10',
  'name': 'All Stars Festival Budapest 2022',
  'start_time': 'Fri, Nov 4, 19:00 – Mon, Nov 7, 03:00 GMT+1'},
 {'description': 'Slovenian industrial-pioneering-artist-musician cult-group '
                 'Laibach returns to the Ship with their latest material. '
                 'Milan Fras, in his legendary pilot’s cap, with his pounding '
                 'bass voice, will be...',
  'event_url': 'https://www.a38.hu/en/program/laibach-si-23828',
  'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTMb4MkwAoOHlCM9NCmbIpfpmQvjR1OFjw77t-7rxU_mnOprPByRoleKSLKlA&s=10',
  'name': 'Laibach (SI)',
  'start_time': 'Sat, Nov 5, 20:00 – 23:59 GMT+1'},
 {'description': 'A Dürer Kert bemutatja: Nasip Kısmet (HU/TR) // Psychedelic '
                 'Night @Dürer Kert - Vendégek: The Swamp Creatures és Ìkatí ? '
                 'Időpont: 2022. November 3. (csütörtök) ? Helyszín: Dürer '
                 'Kert - Kisterem',
  'event_url': 'https://allevents.in/budapest/bass%20guitar',
  'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRwcvqIdqh6mkBr2LTKEsuYoE2TBOPtPaDGvCW3KOI6DO-NxkE2u1kWsj3zlQ&s=10',
  'name': 'Nasip Kısmet (HU/TR) @Dürer Kert // Psychedelic...',
  'start_time': 'Thu, Nov 3, 18:30 – 22:30 GMT+1'},
 {'description': 'abbr Saturday, 5 November 2022, 23:00 – 05:30 abbr Big gay '
                 'party with shows and performances. Music: Disco, House and '
                 'TechHouse. Tickets: 2500-3500 HUF '
                 'facebook.com/garconsbudapest...',
  'event_url': 'https://www.patroc.com/gay/budapest/d/garcons-xxl-party.html',
  'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTxgxy2yqFpdT_aIpRxw1DPF9rxfi5eQ3Pxw17GaRVKojq83rE3NJk7k7GuJGA&s=10',
  'name': 'Garçons – XXL Edition',
  'start_time': 'Sat, Nov 5 – Sun, Nov 6'},
 {'description': 'Apologies, no description available. Click the link for more '
                 'info',
  'event_url': 'https://www.onlineticketsshop.com/se/lander/ungern-evenemang',
  'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTTHd2qy4llqEvTwI-zq9o8Y3DHZ_0_FdciqAq4OQpX-2Bp7-xnRAH-0neNTA&s=10',
  'name': 'Alanis Morissette',
  'start_time': 'Thu, Nov 3, 19:00 – 22:00 GMT+1'},
 {'description': 'Explore all upcoming milky chance events in Budapest, find '
                 'information & tickets for upcoming milky chance events '
                 'happening in Budapest.',
  'event_url': 'https://www.songkick.com/concerts/40352292-milky-chance-at-akvarium-klub',
  'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRe8CKvusmwRxh_mSxV8l_7zfc2B3tof_yH1BiMpm1Dvb1NhEliavKE4xFqhQ&s',
  'name': 'Milky Chance',
  'start_time': 'Sat, Dec 3, 19:30 – 23:59 GMT+1'},
 {'description': 'Apologies, no description available. Click the link for more '
                 'info',
  'event_url': 'https://www.songkick.com/concerts/40368191-kraak-and-smaak-at-akvarium-klub',
  'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR2IxYbn08LbHzcL9jdK9tkYlOlPgxJ13kPxsRHbuRuigN7ofBYE4Ph4E5mUw&s',
  'name': 'Kraak & Smaak',
  'start_time': 'Thu, Nov 3, 20:00 – 23:59 GMT+1'}]

        mock_get_events.return_value = self.mock_get_events_budapest()
        actual = event.display_events('Budapest')
        self.assertEqual(actual, expected_response)


if __name__ == '__main__':
    main()
