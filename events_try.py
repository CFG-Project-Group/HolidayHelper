import requests


def get_events(city):
    """Gets events available in near future for chosen city"""
    key = 'c9a9ef15fe0721edb35af6c9c9f0a781f8c47351325c21274dc679982d035be8'
    url = f"https://serpapi.com/search.json?engine=google_events&q=Events+in+{city}&hl=en&apikey={key}"
    response = requests.get(url)
    events = response.json()
    events_result = events['events_results']
    return events_result


def display_events(city):
    events_result = get_events(city)
    all_events = [{'city': city}]
    try:
        for n in range(len(events_result)):
            event_name = events_result[n]['title']
            # event_date = events_result[n]['date']['start_date']
            event_start_time = events_result[n]['date']['when']
            event_url = events_result[n]['link']
            picture = events_result[n]['image']
            description = events_result[n]['description']
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


print(display_events('Prague'))
