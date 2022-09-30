#Mapper1
#!/usr/bin/python3
import re
import sys
from csv import reader

next(sys.stdin) #Skip first line 
for line in reader(sys.stdin):
    ID, Case_Number, Date, Block, IUCR, Primary_Type, Description, Location_Description, Arrest, Domestic, Beat, District, Ward, Community_Area, FBI_Code, X_Coordinate,\
    Y_Coordinate, Year, Updated_On, Latitude, Longitude, Location = line
    Location_Description = Location_Description.replace(' / ', '/') #Remove whitespace before ‘/’
    loc_desc = re.sub(r'[^\w\s]', ' ', Location_Description) #Replace punctuations for splitting
    if Location_Description == 'RIVER BANK' or Location_Description == 'TAXI CAB' or Location_Description == ‘POOL ROOM’:
       Location_Description = Location_Description.replace(' ', '')

#Split and count common words of the same location but with different description
    if 'COLLEGE' in Location_Description:
       for word in loc_desc.split():
          if word == 'COLLEGE':
            word = ‘COLLEGE/UNIVERSITY’ + ‘ ‘ + Year
            print('%s\t%s' %(word, 1))
   elif 'RESIDENCE' in Location_Description:
       for word in loc_desc.split():
          if word == 'RESIDENCE':
             word = word + ‘ ‘ + Year
             print('%s\t%s' %(word, 1))                         
    elif 'FACTORY' in  Location_Description:
       for word in loc_desc.split():
          if word == 'FACTORY':
             word = word + ‘ ‘ + Year
             print('%s\t%s' %(word, 1))   
    elif 'GOVERNMENT' in  Location_Description:
       for word in loc_desc.split():
          if word == 'GOVERNMENT':
             word = ‘GOVERNMENT BUILDING’ + ‘ ‘ + Year
             print('%s\t%s' %(word, 1))
    elif 'HOSPITAL' in Location_Description:
       for word in loc_desc.split():
          if word == 'HOSPITAL':
             word = word + ‘ ‘ + Year
             print('%s\t%s' %(word, 1))
    elif 'RETAIL' in Location_Description:
       for word in loc_desc.split():
          if word == 'RETAIL':
            word = word + ‘ ‘ + Year
            print('%s\t%s' %(word, 1))
    elif 'CTA' in Location_Description:
       for word in loc_desc.split():
          if word == 'CTA':
            word = ‘CTA TRAIN/BUS STATION OR OTHER PROPERTIES’ + ‘ ‘ + Year
            print('%s\t%s' %(word, 1))
    elif 'CHA' in Location_Description:
       for word in loc_desc.split():
          if word == 'CHA':
            word = ‘CHA APARTMENT’ + ‘ ‘ + Year
            print('%s\t%s' %(word, 1))
    elif 'AIRPORT' in Location_Description or 'AIRCRAFT' in Location_Description:
       for word in loc_desc.split():
          if word == 'AIRPORT' or word == 'AIRCRAFT':
            word = ‘AIRPORT/AIRCRAFT’ + ‘ ‘ + Year
            print('%s\t%s' %(word, 1))
    elif 'PARKING' in Location_Description or 'GARAGE' in Location_Description:
       for word in loc_desc.split():
          if word == 'PARKING' or word == 'GARAGE':
             word = ‘PARKING LOT/GARAGE’ + ‘ ‘ + Year
             print('%s\t%s' %(word, 1))        
    elif 'VEHICLE' in Location_Description or 'BOAT' in Location_Description or 'TRUCK' in Location_Description:
       for word in loc_desc.split():
          if word == 'VEHICLE' or word == 'BOAT' or 'TRUCK':
             word = ‘VEHICLE’ + ‘ ‘ + Year
             print('%s\t%s' %(word, 1))
    elif 'SCHOOL' in Location_Description:
       for word in loc_desc.split():
          if word == 'SCHOOL':
             word = word + ‘ ‘ + Year
             print('%s\t%s' %(word, 1))  
    elif 'RAILROAD' in Location_Description:
       for word in loc_desc.split():
          if word == 'RAILROAD':
             word = word + ‘ ‘ + Year
             print('%s\t%s' %(word, 1))                                   
    elif 'VACANT' in Location_Description:
       for word in loc_desc.split():
          if word == 'VACANT':
             word = ‘VACANT LOT’ + ‘ ‘ + Year
             print('%s\t%s' %(word, 1))    
    elif 'HOTEL' in Location_Description or 'MOTEL' in Location_Description:
       for word in loc_desc.split():
          if word == 'HOTEL' or word == 'MOTEL':
             word = ‘HOTEL/MOTEL’ + ‘ ‘ + Year
             print('%s\t%s' %(word, 1))
    elif 'NURSING' in Location_Description:
       for word in loc_desc.split():
          if word == 'NURSING':
             word = ‘NURSING HOME’ + ‘ ‘ + Year
             print('%s\t%s' %(word, 1))
    elif 'CHURCH' in Location_Description:
       for word in loc_desc.split():
          if word == 'CHURCH':
             word = word + ‘ ‘ + Year
             print('%s\t%s' %(word, 1))
    elif 'DRIVEWAY' in Location_Description:
       for word in loc_desc.split():
          if word == 'DRIVEWAY':
             word = word + ‘ ‘ + Year
             print('%s\t%s' %(word, 1))
    elif 'RIVERBANK' in Location_Description:
       for word in loc_desc.split():
          if word == 'RIVERBANK':
             word = 'LAKEFRONT/WATERFRONT/RIVERBANK' + ‘ ‘ + Year
             print('%s\t%s' %(word, 1))
    elif 'GAS' in Location_Description:
       for word in loc_desc.split():
          if word == 'GAS':
             word = ‘GAS STATION’ + ‘ ‘ + Year
             print('%s\t%s' %(word, 1)) 
    elif 'TAVERN' in Location_Description:
       for word in loc_desc.split():
          if word == 'TAVERN':
             word = word + ‘ ‘ + Year
             print('%s\t%s' %(word, 1))                                                                               
    elif 'BARBER' in Location_Description:
       for word in loc_desc.split():
          if word == 'BARBER':
             word = word + ‘ ‘ + Year
             print('%s\t%s' %(word, 1))
    elif 'DUMP' in Location_Description:
       for word in loc_desc.split():
          if word == 'DUMP' or word == 'DUMPSTER':
             word = 'DUMPSTER' + ‘ ‘ + Year
             print('%s\t%s' %(word, 1))
    elif 'JAIL' in Location_Description:
       for word in loc_desc.split():
          if word == 'JAIL':
             word = word + ‘ ‘ + Year
             print('%s\t%s' %(word, 1))             
    elif Location_Description == '': #When there is no location recorded
        print('%s\t%s' % ('N/A', 1)) 
    else: #Other unique locations that do not require splitting
        word = Location_Description + ‘ ‘ + Year
        print('%s\t%s' % (word, 1))

#Reducer1
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
    word, count = line.split('\t', 1)
    # convert count (currently a string) to int
    try:
        count = int(count)
        word2count[word] = word2count.get(word, 0) + count
    except ValueError:
        # Count was not a number
        # Therefore, ignore/discard this line
        pass

#Sort the words lexigraphically;
sorted_word2count = sorted(word2count.items(), key=itemgetter(0))
