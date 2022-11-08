import json
import requests
from config import events_key


class Events:

    def get_events(self, city):
        """Gets events available in near future for chosen city"""
        url = f"https://serpapi.com/search.json?engine=google_events&q=Events+in+{city}&hl=en&apikey={events_key}"
        response = requests.get(url)
        events = response.json()
        events_result = events['events_results']
        return events_result


    def display_events(self, city):
        events_result = self.get_events(city)
        all_events = [{'city': city}]
        try:
            for n in range(len(events_result)):
                event_name = events_result[n]['title']
                # event_date = events_result[n]['date']['start_date']
                event_start_time = events_result[n]['date']['when']
                event_url = events_result[n]['link']
                picture = events_result[n]['image']
                if 'description' in events_result[n].keys():
                    description = events_result[n]['description']
                else:
                    description = 'Apologies, no description available. Click the link for more info'
                all_events.append({'name': event_name,
                                   # 'date': event_date,
                                   'start_time': event_start_time,
                                   'event_url': event_url,
                                   'image': picture,
                                   'description': description
                                   })
        except KeyError:
            all_events.append("No events available")
        finally:
            return all_events


if __name__ == '__main__':
    event = Events()
    print(event.display_events('Budapest'))
