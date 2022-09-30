if (!require("ggpubr")) {install.packages("ggpubr")}
if (!require("plyr")) {install.packages("plyr")}
if (!require("dplyr")) {install.packages("dplyr")}
library(ggpubr)
library(plyr)
library(dplyr)

#Reading the crime CSV file
crimes <- read.csv(file ='D:\\Users\\User\\Desktop\\Crimes_in_Chicago.csv')

#User-defined function to count the annual rate of crime according to location
count_location <- function() {  
  #Restructuring Crimes_in_Chicago 
  location_year <- crimes %>% #pipe dataframe
    select('Location.Description','Year') #Select variables of interest
  
  #Remove missing values
  location_year <- location_year[-which(location_year$Location.Description == ""), ]
  
  #Remove whitespace before '/'
  location_year$Location.Description <- gsub(' / ', '/', location_year$Location.Description, fixed = TRUE)
  
  #Remove whitespace for these locations
  location_year$Location.Description <- gsub('RIVER BANK', 'RIVERBANK',location_year$Location.Description)
  location_year$Location.Description <- gsub('POOL ROOM', 'POOLROOM',location_year$Location.Description)
  location_year$Location.Description <- gsub('TAXI CAB', 'TAXICAB',location_year$Location.Description)
  
  #Data Cleaning
  location_year$Location.Description <- gsub('.*COLLEGE.*','COLLEGE/UNIVERSITY',location_year$Location.Description)
  location_year$Location.Description <- gsub('.*RESIDENCE.*','RESIDENCE',location_year$Location.Description)
  location_year$Location.Description <- gsub('.*FACTORY.*','FACTORY',location_year$Location.Description)
  location_year$Location.Description <- gsub('.*GOVERNMENT.*','GOVERNMENT',location_year$Location.Description)
  location_year$Location.Description <- gsub('.*HOSPITAL.*','HOSPITAL',location_year$Location.Description)
  location_year$Location.Description <- gsub('.*RETAIL.*','RETAIL',location_year$Location.Description)
  location_year$Location.Description <- gsub('.*CTA.*','CTA TRAIN/BUS STATION OR OTHER PROPERTIES',location_year$Location.Description)
  location_year$Location.Description <- gsub('.*CHA.*','CHA APARTMENT',location_year$Location.Description)
  location_year$Location.Description <- gsub('.*AIRPORT.*','AIRPORT/AIRCRAFT',location_year$Location.Description)
  location_year$Location.Description <- gsub('.*AIRCRAFT.*','AIRPORT/AIRCRAFT',location_year$Location.Description)
  location_year$Location.Description <- gsub('.*PARKING.*','PARKING LOT/GARAGE',location_year$Location.Description)
  location_year$Location.Description <- gsub('.*GARAGE.*','PARKING LOT/GARAGE',location_year$Location.Description)
  location_year$Location.Description <- gsub('.*VEHICLE.*','VEHICLE',location_year$Location.Description)
  location_year$Location.Description <- gsub('.*BOAT.*','VEHICLE',location_year$Location.Description)
  location_year$Location.Description <- gsub('.*TRUCK.*','VEHICLE',location_year$Location.Description)
  location_year$Location.Description <- gsub('.*SCHOOL.*','SCHOOL',location_year$Location.Description)
  location_year$Location.Description <- gsub('.*RAILROAD.*','RAILROAD',location_year$Location.Description)
  location_year$Location.Description <- gsub('.*VACANT.*','VACANT LOT',location_year$Location.Description)
  location_year$Location.Description <- gsub('.*HOTEL.*','HOTEL/MOTEL',location_year$Location.Description)
  location_year$Location.Description <- gsub('.*MOTEL.*','HOTEL/MOTEL',location_year$Location.Description)
  location_year$Location.Description <- gsub('.*NURSING.*','NURSING HOME',location_year$Location.Description)
  location_year$Location.Description <- gsub('.*CHURCH.*','CHURCH',location_year$Location.Description)
  location_year$Location.Description <- gsub('.*RIVERBANK.*','LAKEFRONT/WATERFRONT/RIVERBANK',location_year$Location.Description)
  location_year$Location.Description <- gsub('.*GAS.*','GAS STATION',location_year$Location.Description)
  location_year$Location.Description <- gsub('.*TAVERN.*','TAVERN',location_year$Location.Description)
  location_year$Location.Description <- gsub('.*BARBER.*','BARBER',location_year$Location.Description)
  location_year$Location.Description <- gsub('.*DUMP.*','DUMPSTER',location_year$Location.Description)
  location_year$Location.Description <- gsub('.*DUMPSTER.*','DUMPSTER',location_year$Location.Description)
  location_year$Location.Description <- gsub('.*JAIL.*','JAIL',location_year$Location.Description)
  
  #Concatenate Location.Description and Year
  location_year$Concatenated <- paste(location_year$Location.Description, ' ', location_year$Year)
  
  #Count frequency of distinct rows
  count(location_year,Concatenated)
}

#Measure execution time 
start_time <- Sys.time()

#Execute the user-defined function
count_location()

end_time <- Sys.time()
end_time - start_time

