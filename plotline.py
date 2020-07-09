import sqlite3
import numpy as np
import matplotlib.pyplot as plt

#from datetime import datetime
#import time
#import matplotlib.dates as mdates
#from dateutil import parser

from matplotlib import style
style.use('Solarize_Light2')

conn = sqlite3.connect('DB.sqlite',
                        detect_types=sqlite3.PARSE_DECLTYPES |
                        sqlite3.PARSE_COLNAMES)
cur = conn.cursor()

#WEATHER DATA
cur.execute('''SELECT date, MAX(precipitation) AS precipitation,
            MAX(snowfall) AS snowfall FROM Weather where
            (date BETWEEN '2011-01-01'AND '2011-02-28')group by date''')

dates = []
value_prcp = []

for weather_row in cur:
    # weather_row[0] is date
    # weather_row[1] is precipitation
    #print (weather_row[0])
    date = (weather_row[0]).replace('2011-','')
    np.array(dates.append(date))
    np.array(value_prcp.append(weather_row[1]))

print(dates)
print("Dates type is", type(weather_row[0]))

#TRAIN DATA
cur.execute('''SELECT date, SUM(passengers) AS passengers
            FROM Trains where
            (date BETWEEN '2011-01-01'AND '2011-02-28')group by date''')

value_passengers= []

for train_row in cur:
    # train_row[0] is date(not used)
    # train_row[1] is passengers
    #print (train_row[1])
    train = (train_row[1]/1000)
    np.array(value_passengers.append(train))

#print(value_passengers)
print("Passenger type is", type(train_row[1]))

#rain = fig_1.add_subplot(111)
#passengers = fig_1.add_subplot(122)

fig, ax1 = plt.subplots(figsize=(100, 10))


ax2 = ax1.twinx()
bar = ax1.bar(dates,value_prcp, label='Precipitation')
line = ax2.plot(dates,value_passengers, '-c', linewidth=1, label='Passengers')

ax1.set_xlabel('Day')
ax1.set_ylabel('Precipitation')
ax2.set_ylabel('Passengers (1000)')

#THIS CODE FORMATS THE DATES ON X AXIS. ROTATE 90 IS BETTER
#ax = plt.gca()
#date_formatter = mdates.DateFormatter('%m\n%d')
#MONTH#date_formatter = mdates.DateFormatter('%m')
#ax.xaxis.set_major_formatter(date_formatter)
#ax.xaxis.set_major_locator(mdates.DayLocator())
#MONTH#ax.xaxis.set_major_locator(mdates.MonthLocator())

plt.title('Weather Effect on Train Passengers in Massachusetts (Jan-Feb 2011)')
plt.legend()

# set the xaxis label
plt.setp(ax1.xaxis.get_label(), visible=True, text='Dates')
# set the ticks
plt.setp(ax1.get_xticklabels(), visible=True, rotation=90, ha='right')
#set parameters for tick labels
ax1.xaxis.set_tick_params(labelsize=7)

plt.show()
