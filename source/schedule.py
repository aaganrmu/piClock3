from datetime import datetime, time

class Event():
    def __init__(self, line):
        time_string, name = line.split(";", 1)
        hour, minute, time = time_string.split(":")
        self.name = name
        self.time = time(hour=hour, minute=minute, second=second)


class Schedule():
    def __init__(self):
        self._last_check = datetime.now().time()
        self.items = []
        return


    def load_schedule(self, path):
        with open('R', path) as file
            for line in file:
                items += Event(line)
        return


    def check_for_events(self):
        now = datetime.now().time()


        return "something"


        t = datetime.now().time()
        hour = t.strftime("%H")
        minute = t.strftime("%M")
        second = t.second
