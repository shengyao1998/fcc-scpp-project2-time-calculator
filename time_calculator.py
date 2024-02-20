def add_time(start, duration, weekday=""):

  ############
  # Week Mapping
  ############
  day_to_weekday = ["Sunday",
                   "Monday", 
                   "Tuesday", 
                   "Wednesday", 
                   "Thursday", 
                   "Friday", 
                   "Saturday"]
    
  
  ############
  # Split start time into hours and minutes
  ############
  curr = start.split(" ")
  curr_time = curr[0].split(":")

  curr_day = 0
  curr_hour = int(curr_time[0])
  curr_minute = int(curr_time[1])
  curr_meridian = curr[1]

  if curr_meridian == "PM":
    curr_hour += 12


  
  ############
  # Split duration into hours and minutes
  ############
  duration_time = duration.split(":")
  duration_day = 0
  duration_hour = int(duration_time[0])
  duration_minute = int(duration_time[1])

  

  ############
  # Compute the new time
  ############
  new_min = (curr_minute + duration_minute) % 60
  carry_min = (curr_minute + duration_minute) // 60
  new_hour = (curr_hour + duration_hour + carry_min) % 24
  carry_hour = (curr_hour + duration_hour + carry_min) // 24
  new_day = curr_day + duration_day + carry_hour

  if new_day == 1:
    comment = "(next day)"
  elif new_day > 1:
    comment = "({0} days later)".format(new_day)
  else:
    comment = ""

  if new_hour >= 12:
    if new_hour != 12:
      new_hour -= 12
    new_meridian = "PM"
  else:
    if new_hour == 0:
      new_hour = 12
    new_meridian = "AM"
  

  if weekday:
    weekday = weekday.lower()
    weekday = weekday.capitalize()
    weekday_index = day_to_weekday.index(weekday)
    new_weekday = day_to_weekday[((weekday_index + new_day) % 7)]
    comment = ", " + new_weekday + " " + comment
  else:
    new_weekday = ""
    comment = " " + comment


  new_time = "{0}:{1:02} {2}{3}".format(new_hour, new_min, new_meridian, comment)
  
  return new_time.strip()

