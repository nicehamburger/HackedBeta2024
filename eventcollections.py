import json

class EventCollection:
    def __init__(self):
        self.events = []

    def add_event(self, event):
        self.events.append(event)

    def export_to_json(self, file_path):
        event_data = [event.to_dict() for event in self.events]  # Convert each event to a dictionary
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(event_data, file, ensure_ascii=False, indent=4)  # Save as formatted JSON

    def __str__(self):
        return f"EventCollection({len(self.events)} events)"
