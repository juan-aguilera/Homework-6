
# **Data Analysis Project: Social and Economic Development**

## **Introduction**
This project aims to analyze social and economic development data using a real data source from the World Bank Open Data. Test Driven Development approach will be applied to ensure at least 90% coverage in unit tests. The analysis results will be presented at the end of this document, including three generated graphs. 

### **Data Source**
The World Bank Open Data database was used, providing free access to a wide variety of economic, social, and environmental indicators for countries worldwide.

### **Public GitHub Repository**
The source code and related files for this project are available in the following GitHub repository: link to repository

## **Project Structure**
The project is organized as follows:

xlsx file : File containing downloaded data files from the World Bank Open Data.

data_parsing_and_plotting/: Folder containing the project's source code.

unitests/: Folder containing unit test files.


README.md: File containing detailed information about the project and how to execute it.

## **Project Description**

### Data Acquisition: Relevant data was downloaded from the World Bank Open Data.
### Exploratory Data Analysis: An exploratory analysis of the data was conducted to understand its structure and characteristics.
### Test Development: Test Driven Development approach was applied to write unit tests covering at least 90% of the code.
### Data Analysis: The data was processed and analyzed to identify significant trends and patterns.
### Graph Generation: Three graphs were created to visualize the analysis results.
### Results Presentation: Analysis to share the findings and conclusions from the graphs.


## **Regions for Analysis**
The data was divided into the following regions for analysis:

Europe & Central Asia,
South Asia,
Middle East & North Africa,
Sub-Saharan Africa,
Latin America & Caribbean,
East Asia & Pacific,
North America

## **Generated Graphs**
### Graph 1: Economic and Social Rights Performance Score evolution (2014-2018) per Región (2014-2018)
![image](https://github.com/juan-aguilera/Real-world-data-analysis-/assets/158538464/089d96f3-c998-49a9-96c0-f4b0300cd376)
Analysis: "the dataset measures how effectively countries use their economic resources to ensure the fulfillment of five economic and 
social rights—the rights to education, food, health, housing and work. The data was hard to collect, the HRMI team at the  University of Georgia’s
GLOBIS Center therefore used a Bayesian latent variable model to estimate a full set of country scores". (https://esgdata.worldbank.org/)
The graph shows a large gap between regions like Europe/North America and Central Africa, Southern Africa, and Southern Asia. According to the narrative we have 
always heard about these regions, one might think that deficiencies mainly arise in their healthcare, education, and food production and distribution systems. 
Although an upward trend is observed in these regions, it is difficult to imagine a short-term scenario (5 years) in which they reach levels similar to those of Europe and North America.


Analysis: Significant variation in the performance of economic and social rights is observed among different regions.

### Graph 2: Access to electricity (% of population) evolution (2014-2018) per Región
![image](https://github.com/juan-aguilera/Real-world-data-analysis-/assets/158538464/b5d2004e-04de-4d00-9631-8b5ffeac6a63)
Analysis: Most countries have high levels of access to electricity, with some exceptions in specific regions. Just like in the previous graph, the most lagging region is 
Central and Southern Africa. Unlike the previous graph, the other regions have very high levels of electrification and are very close to each other on the graph, thus 
representing homogeneity in the data but leaving out the aforementioned region. Despite having a great natural resource for energy generation such as the sun, Central 
and Southern Africa remains a territory that requires large amounts of investment in various fronts.

### Graph 3: CO2 emissions (metric tons per capita) evolution (2014-2018) per Region
![image](https://github.com/juan-aguilera/Real-world-data-analysis-/assets/158538464/71534513-4c35-4be5-980e-a7a34bf1570c)
Analysis: A downward trend in CO2 emissions per capita is observed in most regions, suggesting progress in mitigating climate change. However, it is important to analyze the relationship 
that this graph has with the previous ones. The regions with a better indicator of economic and social rights are the ones that generate more emissions. Additionally, 
despite regions like Latin America and the Caribbean having a high score and also a high electrification percentage, their emissions are very low compared to North America 
and the Middle East. This could indicate that their energy matrices are cleaner and their economies are not largely based on extractivism

For more details about the project and its execution, please refer to the README.md file in the GitHub repository.






















Name                           Stmts   Miss  Cover
--------------------------------------------------
data_parsing_and_plotting.py      74     19    74%
unitest_algorithms.py             34      1    97%
--------------------------------------------------