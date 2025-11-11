thonimport json

def parse_event_data(event_json):
    parsed_data = []
    for event in event_json:
        event_info = {
            'name': event['name'],
            'start_date': event['start_date'],
            'end_date': event['end_date'],
            'venue': event.get('venue_name', 'Unknown Venue'),
            'organizer': event.get('primary_organizer.name', 'Unknown Organizer'),
            'tags': event.get('tags', [])
        }
        parsed_data.append(event_info)
    return parsed_data

def load_and_parse(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return parse_event_data(data)