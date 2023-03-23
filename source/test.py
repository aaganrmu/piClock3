from schedule import Schedule, Event


schedule = Schedule()
schedule.load("schedule.txt")

events = schedule.check_for_events()
print(len(events))