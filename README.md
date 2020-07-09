# Massachusetts-Train-Passengers-and-Weather-Analysis
This project uses python to analyse the correlation of weather conditions and mass transit use in Massachusetts

Source of dataset: http://academictorrents.com/details/1938b67c7db77f878a56256e9958bb20801b9ddd

Background:
I'm in urban planning with a particular interest in traffic/mass transit so I chose some data from the Massachusetts Department of Transportation. It comes with a lot of CSV data from weather reports, cars and to number of train passengers. As this is a learning process, I included a list of problems and solutions used in the readme.

Part 1-Database entry
So I began analysing the dataset to figure out what I wanted to find.
It was a huge dataset so i chose to compare just the weather data and train passenger numbers to see if there is any correlation between the two.
From here I drew a simple ER Diagram for the SQL database. There were problems faced and below were the solutions.

Problems faced:
-Data from different sources had different date formats, one in 20110101 and another in 01/01/2011
-Data from sensors gave readings of negative numbers ie.-9999

Solution:
-Used datetime.datetime.strptime(s, '%Y%m%d').date() and try and except to try many formats and returning a standardised format for input to SQL
-Used the (line_name).replace('-9999','0'), could have added range or try and except but this was working so i was happy enough
Link to dataset:http://academictorrents.com/details/1938b67c7db77f878a56256e9958bb20801b9ddd

Part 2- Data Visualization
It took a total of 2 days to figure out Matplotlib. The chart I wanted to plot had two Y-axes and two different types of charts (Bar and line).

The end result was was that passenger counts were influenced by train numbers and not so much the weather. Some days, like 12 Jan and 27 jan with higher than normal rainfall did influence passenger counts but generally the trend is based on available trains. It would be interesting to find the % capacity of each train vs. rainy days, however the dataset did not provide the data.

Overall, i learnt how to quickly process and analyse large volumes of data,(something like 14k plus entries), clean them up efficiently and produce a visualization for human analysis.

I will explain issues faced during this part.

Problems:

1-Datetime object does not carry on into SQL, and SQLite date class is different, hence data from SQL had to be parsed as strings. This left me with strings like of 2011-01-01. May not be a big deal but i wanted to clean out the '2011'.
2-Passenger numbers were in the hundreds of thousands and this left the rain data range in the chart tiny in comparison   
3-There were many weather stations collecting data on the same day
4-There were many trains running on the same day
5-Data range to plot the whole year is ok but tells little data
6-Labeling was messy and overlapping. 

Solution:

1-Used (date).replace('2011-','') leaving me with just month and day ie. 01-20
2-I divided the passenger count by 1000
3-Used the MAX and group by function to only show the maximum rain collected among all stations on that day. I could have made another table, but I felt this solution was adequate. 
4-Like before for trains, i used the SUM and group by function to sum up all passengers from all trains on the same day.
5-The data range was set to just show data for the months of Jan and Feb. 2011 was not a leap year hence 28 days.
6-Rotate the dates 90 deg so that they are more compact and show well. Finally I adjusted the label size to 7 so it is easily readable.

Files included:
Chart image
https://github.com/ehlexlee/Massachusetts-Train-Passengers-and-Weather-Analysis/blob/master/Chart.png
CSV to SQL import code
https://github.com/ehlexlee/Massachusetts-Train-Passengers-and-Weather-Analysis/blob/master/csvimport.py
Chart plot code
https://github.com/ehlexlee/Massachusetts-Train-Passengers-and-Weather-Analysis/blob/master/plotline.py
