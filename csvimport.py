import csv
import sqlite3
import datetime
import time
import re

#defining object to change date format in CSV: ie.19040605(yyyymmdd) to date object
def parsedate(s):
    s_date = None
    try:
        s_date = datetime.datetime.strptime(s, '%Y%m%d').date()
    except:
        s_date = datetime.datetime.strptime(s, '%m%d%Y').date()

    return s_date


#sql setup
conn = sqlite3.connect('DB.sqlite')
cur = conn.cursor()

#Clean slate & add tables
cur.executescript('''
DROP TABLE IF EXISTS Weather;
DROP TABLE IF EXISTS Trains;
''')

cur.execute('''
CREATE TABLE IF NOT EXISTS Weather (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    station_name TEXT,
    date TEXT,
    precipitation INTEGER,
    snowfall INTEGER
    )
    ''')

cur.execute('''
CREATE TABLE IF NOT EXISTS Trains (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    train_number TEXT,
    date TEXT,
    Route TEXT,
    passengers INTEGER,
    trip_status TEXT
    )
    ''')

#Open weather CSV as dictionary
with open('noaa_weather.csv','r') as csv_weather:
    csv_reader = csv.DictReader(csv_weather)

#debug code
#    for line in csv_reader:
#        print(line['DATE'])

#Read CSV lines and record in SQL
    for line in csv_reader:
        OLD_DATE = line['DATE'];
        STATION_NAME = line['STATION_NAME'];
        PRCP = (line['PRCP']).replace('-9999','0');
        SNOW = (line['SNOW']).replace('-9999','0');
        DATE = parsedate(OLD_DATE);
        #print(line['DATE'])
        #print(DATE)

#Skips dates if not the year 2011 because we only want to compare train data in 2011
        if DATE.year != 2011 : continue

        print('---reading one line---')
        print('---still reading   ---')

        cur.execute ('''INSERT OR IGNORE INTO Weather (station_name, date, precipitation, snowfall)
            VALUES ( ?, ?, ?, ? )''', ( STATION_NAME, DATE, PRCP, SNOW ))

conn.commit()
print('---Weather data input done---')
print('--- Moving to next task ---')
time.sleep (5)


with open('MBCR_Trip_Records_2011.csv','r') as csv_train_2011:
    csv_reader_train_2011 = csv.DictReader(csv_train_2011)

#debug code
#    for line in csv_reader_train_2011:
#        print(line['tTrip'])

#Read CSV lines and record in SQL

    for line in csv_reader_train_2011:
        OLD_DATE = line['tTrip'];
        CLEAN_DATE = OLD_DATE.replace('/','');
        TRAIN_NUMBER = line['cTrainNo'];
        ROUTE = line['Route'];
        PASSENGERS = line['iPassenger'];
        TRIP_STATUS = line['TripStatus'];
        DATE = parsedate(CLEAN_DATE)
        #print(DATE)

#Skips dates if not the year 2011 because we only want to compare train data in 2011
        if DATE.year != 2011 : continue

        print('---reading one line---')
        print('---still reading   ---')

        cur.execute ('''INSERT OR IGNORE INTO Trains (train_number, date, route, passengers, trip_status)
            VALUES ( ?, ?, ?, ?, ? )''', ( TRAIN_NUMBER, DATE, ROUTE, PASSENGERS, TRIP_STATUS ))

conn.commit()
cur.close()
print('--- Train data input done ---')
print('--- Moving to next task ---')
time.sleep (5)
print('--- ALL DONE! ---')
