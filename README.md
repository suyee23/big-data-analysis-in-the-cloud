# big-data-analysis-in-the-cloud

This assignment allows students to demonstrate and discuss the advantages of Big Data Analytics in the cloud through the implementation of a suitable Big Data Analytics solution for a selected dataset. 

We are required to:
  1. Select a problem based on a dataset that has the size of 1GB or more
  2. Select a suitable mehod to be implemented in MapReduce (MapReduce approach) 
  3. Select any programming language (Conventional approach)
  4. Provide analysis and explanation how the MapReduce, the chosen algorithm and Hadoop system help solve the problem based on the dataset
  5. Compare and identify the differences between the MapReduce approach and Conventional approach

My group chose to analyze a dataset that is retrived from Chicago data portal (1.7GB) using MapReduce Python (MapReduce approach), Python (Conventional approach) and R (Conventional approach). 

Dataset Link: https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-Present/ijzp-q8t2/data 

Our research objectives are:
  1. To identify the locations where frequent crime happens
  2. To pinpoint the association between the number of distinct crimes committed and the time of crime
  3. To investigate the relationship between the primary type of crime and status of arrest

In the end, we found that Python and R (Conventional approach) are slightly less robust as both are not capable of performing parallel processing for large datasets compared to MapReduce Python (MapReduce approach). 

