from icalendar import Calendar, Event
import pandas as pd
from dateutil.parser import parse
from datetime import datetime
from datetime import timedelta

# read data
data = pd.read_csv('chores.csv')

# determine housemates and create a calendar for each
assignments = data[data.columns[1:]]
housemates = pd.unique(assignments.values.flatten())
calendars = {}
for housemate in housemates:
    calendars[housemate] = Calendar()

# iterate over weeks, creating events for each chore assignment
for i, week in data.iterrows():
    # determine start and end date for this weeks chores
    start = parse(week[0])
    end = start + timedelta(days=7) - timedelta(minutes=1)

    # for each chore column, create an event and add to 
    # housemate calendar
    for j in range(1,len(week)):
        event = Event()
        chore_name = cols[j]
        event.add('summary', chore_name)
        event.add('dtstart', start)
        event.add('dtend', end)
        # lookup housemate calendar and assign chore event
        assigned_housemate = week[chore_name]
        calendars[assigned_housemate].add_component(event)

# write calendars to file
for housemate, cal in calendars.items():
    with open(f'chores-{housemate}.ics', 'wb') as f:
        f.write(cal.to_ical())
