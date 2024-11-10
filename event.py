class Event:
    def __init__(self, name, date, time, location, registration, entry_fee, url, is_food=False):
        self._name = name
        self._date = date
        self._time = time
        self._location = location
        self._registration = registration
        self._entry_fee = entry_fee
        self._url = url  # Store the post's URL
        self._is_food = is_food  # Flag to indicate if the event has food

    def __str__(self):
        return f"Event(name={self._name}, date={self._date}, location={self._location}, is_food={self._is_food}, url={self._url})"
    
    def to_dict(self):
        return {
            "name": self.name,
            "date": self.date,
            "time": self.time,
            "location": self.location,
            "registration": self.registration,
            "entry_fee": self.entry_fee,
            "url": self.url,
            "is_food": self.is_food
        }
