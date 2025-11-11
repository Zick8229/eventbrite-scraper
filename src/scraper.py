thonimport requests
from bs4 import BeautifulSoup
import json

def fetch_event_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    events = []
    
    for event in soup.find_all('div', class_='eds-event-card-content'):
        event_data = {
            "name": event.find('div', class_='eds-event-card-content__primary-content').get_text(strip=True),
            "image.url": event.find('img', class_='eds-event-card-image__image')['src'],
            "primary_organizer.name": event.find('a', class_='eds-text-color--black')['title'],
            "start_date": event.find('time', class_='eds-text-color--gray-500').get('datetime'),
            "start_time": event.find('time', class_='eds-text-color--gray-500').get('datetime'),
            "end_date": event.find('time', class_='eds-text-color--gray-500').get('datetime'),
            "end_time": event.find('time', class_='eds-text-color--gray-500').get('datetime'),
            "url": event.find('a', class_='eds-event-card-content__action-link')['href']
        }
        events.append(event_data)
    return events

def main():
    url = "https://www.eventbrite.com/d/online/events/"
    event_data = fetch_event_data(url)
    with open('events.json', 'w') as f:
        json.dump(event_data, f, indent=4)

if __name__ == "__main__":
    main()