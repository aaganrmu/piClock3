from datetime import datetime, time

class Event():
    def __init__(self, line):
        time_string, name = line.split(" ", 1)
        hour, minute, second = time_string.split(":")
        self.name = name
        self.time = time(
                         hour=int(hour), 
                         minute=int(minute),
                         second=int(second)
                         )


class Schedule():
    def __init__(self):
        self._events = []
        self._pointer = 0


    def load(self, path):
        events = []
        with open(path, 'r') as file:
            events = [Event(line) for line in file]
        self._events = sorted(events, key=lambda x: x.time)
        self._pointer = 0
        discard = self.check_for_events()
        print(len(discard))
        
    def check_for_events(self):
        now = datetime.now().time()
        events = []
        while self._pointer < len(self._events):
            event = self._events[self._pointer]
            if event.time < now:
                events.append(event)
                self._pointer += 1
            else:
                break
        return events