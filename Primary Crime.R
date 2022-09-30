if (!require("tidyverse")) {install.packages("tidyverse")}
if (!require("textdata")) {install.packages("textdata")}
if (!require("plyr")) {install.packages("plyr")}
if (!require("dplyr")) {install.packages("dplyr")}
library(tidyverse)
library(textdata)
library(dplyr)
library(plyr)

#User-defined function to count the primary type of crime according to status of arrest
count_arrest <- function() {  
  #Restructuring Crimes_in_Chicago
  primary_crime <- crimes %>% #pipe dataframe
    select('Primary.Type','Arrest') #Select variables of interest
  
  #Select only not arrested crimes
  not_arrested <- filter(primary_crime, Arrest %in% c('false'))
  
  #Count frequency of distinct rows according to primary crime and status of arrest
  count(not_arrested, Primary.Type)
}

#Measure execution time 
start_time <- Sys.time()

#Execute the user-defined function
count_arrest()

end_time <- Sys.time()
end_time - start_time
