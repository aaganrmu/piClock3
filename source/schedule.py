import logging
import os

logging.basicConfig(level=logging.INFO)
from datetime import datetime, time

class Event():
    def __init__(self, line):
        time_string, name = line.split(" ", 1)
        hour, minute, second = time_string.split(":")
        self._file_time = 0
        self._file_path = ''
        self._current_day = 0

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
        self._current_date = datetime.now().date()

    def file_outdated(self):
        logging.debug(f"Checking if file {self.file_path} is outdated")
        new_time = os.stat(self.file_path).st_mtime
        outdated = new_time > self._file_time
        return outdated

    def load_file(self):
        logging.debug(f"Loading schedule file {self.file_path}")
        self._file_time = os.stat(self.file_path).st_mtime
        events = []
        with open(self.file_path, 'r') as file:
            events = [Event(line) for line in file]
        self._events = sorted(events, key=lambda x: x.time)
        self._pointer = 0
        discard = self.check_for_events()
        logging.info(f"Loaded {len(events)} events, of which {len(discard)} already happened today")


    @property
    def file_path(self):
        return self._file_path


    @file_path.setter
    def file_path(self, path):
        logging.debug(f"File set to {path}")
        self._file_path = path
        self.load_file()


    def check_for_events(self):
        logging.debug(f"Checking for new events")
        if self.file_outdated():
            logging.info(f"Schedule file {self.file_path} is outdated, reloading")
            self.load_file()

        if self._current_date:
            new_date = datetime.now().date()
            if self._current_date != new_date:
                logging.info("Starting new day")
                self._pointer = 0
                self._current_date = new_date
        else:
            self._current_date = new_date


        now = datetime.now().time()
        events = []
        while self._pointer < len(self._events):
            event = self._events[self._pointer]
            if event.time < now:
                events.append(event)
                self._pointer += 1
            else:
                break
        if events:
            logging.info(f"Found {len(events)} recent events while checking")
        return events