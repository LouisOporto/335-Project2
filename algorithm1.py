def findSchedule(scheduleList, availTime, limit):
  '''Given a list of schedules, available time, and meeting limit in minutes, will return a list of available time'''
  list = []
  n = len(scheduleList)
  min = "00:00" # Min Value
  max = "99:99" # Max Value

  # Combine all schedules into a single list to be sorted and analyzed
  for x in range(n):
    min = availTime[x][0] if min < availTime[x][0] else min
    max = availTime[x][1] if max > availTime[x][1] else max
    for time in scheduleList[x]:
      list.append(time)

  list.sort(key=lambda x: (x[0], x[1]))

  # Removes any outliers to the available time and floors any other time periods that exceed.
  for x in list[::-1]:
    if x[0] < min:
      if x[1] < min:
        list.remove(x)
      else:
        x[0] = min

    if x[1] > max:
      if x[0] > max:
        list.remove(x)
      else:
        x[1] = max

  list_avail = []
  n = len(list)

  # Makes intervals between min and max time, where all members are available
  for x in range(n):
    if x == 0: #First Item
      list_avail.append([min, list[x][0]])
    elif x == n - 1: # Last item
      list_avail.append([list[x][1], max])
    list_avail.append([list[x - 1][1], list[x][0]])

  # Removes any interval that is less than the given limit convert from hour & min to min
  for x in list_avail[::-1]:
    hr_diff = int(x[1][:2]) - int(x[0][:2])
    min_diff = int(x[1][3:5]) - int(x[0][3:5])
    if limit >= (hr_diff * 60 + min_diff):
      # If the difference is less than the limit remove the time interval
      if x[1] == max and not limit > (hr_diff * 60 + min_diff):
        pass
      elif x[0] == min and not limit > (hr_diff * 60 + min_diff):
        pass
      else:
        list_avail.remove(x)

  return list_avail


# Asking for user to provide member schedules, interval available, time limit
time = 0
members = int(input("How many members are there?: "))
schedule = []
avail = []
for x in range(members):
  schedule.append([])
  print(f"Person {x + 1}")

  while(True):
    first = input(f"Enter your interval schedule one-by-one(HH:MM-HH:MM). Type \'next\' when done:\nInterval: ")
    if first == "next":
      break
    else:
      schedule[x].append([first.split('-')[0],first.split('-')[1]])

  temp = input("Between what time can you meet up? (HH:MM-HH:MM): ")
  avail.append([temp.split('-')[0],temp.split('-')[1]])

time = int(input("How long will the meeting take (min): "))

result = findSchedule(schedule, avail, time)
print("Printing possible time period for all members...")
print(result)