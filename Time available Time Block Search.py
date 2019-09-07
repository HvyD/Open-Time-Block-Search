#!/usr/bin/env python
# coding: utf-8

# In[1]:


from datetime import datetime, timedelta

appointments = [
    (datetime.strptime('2019-01-01 06:45:00', '%Y-%m-%d %H:%M:%S'), datetime.strptime('2019-01-01 07:00:00', '%Y-%m-%d %H:%M:%S')),
    (datetime.strptime('2019-01-01 01:00:00', '%Y-%m-%d %H:%M:%S'), datetime.strptime('2019-01-01 04:30:00', '%Y-%m-%d %H:%M:%S')),
    (datetime.strptime('2019-01-01 07:10:00', '%Y-%m-%d %H:%M:%S'), datetime.strptime('2019-01-01 09:30:00', '%Y-%m-%d %H:%M:%S')),
    (datetime.strptime('2019-01-01 04:45:00', '%Y-%m-%d %H:%M:%S'), datetime.strptime('2019-01-01 05:00:00', '%Y-%m-%d %H:%M:%S'))]


between = (datetime.strptime('2019-01-01 06:45:00', '%Y-%m-%d %H:%M:%S'), datetime.strptime('2019-01-01 07:00:00', '%Y-%m-%d %H:%M:%S'))


def get_slots(between, appointments, duration=timedelta(hours = .25)):
    slots = sorted([(between[0], between[0])] + appointments + [(between[1], between[1])])
    for start, end in ((slots[i][1], slots[i+1][0]) for i in range(len(slots)-1)):
        while start + duration <= end:
            print (start, start + duration)
            start += duration

get_slots(between, appointments)


# In[ ]:





# In[ ]:




