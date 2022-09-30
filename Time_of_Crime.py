#Mapper2
#!/usr/bin/python3
import sys
import datetime
from csv import reader

next(sys.stdin) # Skip first line 
for line in reader(sys.stdin):
    ID, Case_Number, Date, Block, IUCR, Primary_Type, Description, Location_Description, Arrest, Domestic, Beat, District, Ward, Community_Area, FBI_Code, X_Coordinate,\
    Y_Coordinate, Year, Updated_On, Latitude, Longitude, Location = line 
    date_time = datetime.datetime.strptime(Date, '%m/%d/%Y %I:%M:%S %p') 
    hour = str(date_time.hour) #Derive hour from the Date attribute
    print('%s\t%s'% (hour, 1))

#Reducer2
#!/usr/bin/env python3
from operator import itemgetter
import sys

#Maps words to their counts
word2count = {}

#Input comes from STDIN
for line in sys.stdin:
    #Remove leading and trailing whitespace
    line = line.strip()

    #Parse the input we got from mapper.py
    hour, count = line.split('\t ', 1)
    # convert count (currently a string) to int
    try:
        count = int(count)
        word2count[hour] = word2count.get(hour, 0) + count
    except ValueError:
        #Count was not a number
        #Therefore, ignore/discard this line
        pass

#Sort the words lexigraphically;
sorted_word2count = sorted(word2count.items(), key=itemgetter(0))

#Write the results to STDOUT (standard output)
for hour, count in sorted_word2count:
    print ('%s\t%s'% (hour, count))
