if (!require("tidyverse")) {install.packages("tidyverse")}
if (!require("textdata")) {install.packages("textdata")}
if (!require("plyr")) {install.packages("plyr")}
if (!require("dplyr")) {install.packages("dplyr")}
if (!require("lubridate")) {install.packages("lubridate")}
library(tidyverse)
library(textdata)
library(plyr)
library(dplyr)
library(lubridate) #date function

#User-defined function to count the crime frequency according to hour of crime
count_time <- function() {  
  #Restructuring Crimes_in_Chicago
  crimes_hour <- crimes %>% #pipe dataframe
    select('Date') #Select variables of interest
  
  #Datetime is read as characters
  #Convert to timestamp
  crimes_hour <- crimes_hour %>% mutate(Date = mdy_hms(Date))
  
  #Convert Datetime into hours only
  crimes_hour$hour <- format(as.POSIXct(crimes_hour$Date), format = "%H")
  
  #Count frequency of distinct rows
  count(crimes_hour, hour)
}

#Measure execution time 
start_time <- Sys.time()

#Execute the user-defined function
count_time()

end_time <- Sys.time()
end_time - start_time
