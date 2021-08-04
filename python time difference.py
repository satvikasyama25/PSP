"""
calculate the difference between two times.
"""
import datetime
curr_time=datetime.datetime.now().time() #current time
print(curr_time) #Around 00:10:00
dt_obj=datetime.time(20,7,21)
print(dt_obj)
#Now calculate the difference
diff= datetime.timedelta(hours=(dt_obj.hour-curr_time.hour),seconds=(dt_obj.second-curr_time.second))
print(diff)

