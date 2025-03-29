---
layout: visualization
title: "Assignment 2: \nDrug Offenses in San Francisco (2003-2024)"
description: "Analysis of drug-related offenses in San Francisco using multiple visualization techniques"
date: 2024-03-26
author: s214588
---

# Drug Offenses in San Francisco (2003-2024)
In this assignment we dive deeper into the publically available crime data collected in San Francisco(SF) from 2003 to 2024,
where we specifically investigate the changes in drug realted crime measured through the recorded arrests aptly named "Drug Offenses".

This data has been made available by the SF Police Department themselves, and in summary contains a lot of both data and metadata
about arrests throught the entire city. Most importantly for this assignment, the dataset include information about the time and place
of each arrest, most often stored as both the district it occured in as well and the geographical coordinates.

I specifically decided to investigate the crime category of drug offenses, as it was one of the categories that had a more significant temporal change, as seen in Fig. 1, compared to many of the others.

## Overall Trend (2003-2024)

<iframe src="/assets/plotly/yearly_drug_offenses.html" height="520px"></iframe>

Looking at Fig.1, we specifcally can see that drug offenses were generally on the rise from 2003 to 2009, where it peaked at almost 12.000 arrests, before rapidly declining to its bottom in 2021 at "only" about 2.200 arrests. Now the interesting part then is that the drug offenses seemingly begin to climb again, sitting at around 4000 arrests for the next 3 years.

To explain the rapid decrease in drug related arrests after 2009, we can assume that multiple circumstances might have played a role. Specifically the step decrease just between 2009 and 2010, can partially be attributed to a [major drug enforcement scandal in 2010](https://www.sfchronicle.com/crime/article/sf-drug-cases-police-18262132.php), which resulted in both dismissed drug offense cases, as well as a significant cutback in aggresive drug policing. 

Explaining maybe the more underlying reason for the general reduction in drug related arrests, the state of california [issued a reform in 20210 to make minor possession of marijuana into a infraction rather than a misdeameanor](https://www.nytimes.com/2010/10/02/us/politics/02pot.html)(thus no longer requiring arrest). This combined with multiple other intiatives to generally downgrade the severity of a range of offenses such as [proposition 47 in 2014](https://en.wikipedia.org/wiki/2014_California_Proposition_47), could be potential reasons for the overall decrease in drug realted arrests.

Finally, the all time low was reached during 2021, before an upward surge almost doubled the yearly drug offenses in the following 3 years. While difficult to find any conclusive reason, the time period overlaps well with the outbreak of COVID-19 pandemic, which negatively impacted many peoples lives, and some [ sources claim to have had a negative impact on substance usage](https://nida.nih.gov/research-topics/covid-19-substance-use#increase).


## District-Level Trends
To further understand how drug related crimes developed over time in SF, we also try to use the district data, to understand if the problems were localized or more widespread over time, as seen in Fig 2.

<iframe src="/assets/bokeh/district_trends.html" height="500px"></iframe>

Suprisingly we find that during the peak of drug offenses, the majority of the arrests occured in one district; the Tenderloin district, at almost 5000 arrest in both 2008 and 2009, where the 2nd and 3rd largest districts Southern and Mission, doesnt even get the same combined. However, it is also apparent that the same effects that reduced the overall drug offenses, also impacts the Tenderloin district the most, as it saw a step decline from 2009 to 2017, where it reached a basline not that different from the rest of the districts.

However, the peace was quickly broken as Tenderloin took a sharp breakaway from the rest of the districts, resulting in a [declaration of state of emergency in the Tenderloin](https://sfmayor.org/article/mayor-london-breed-declares-state-emergency-tenderloin#:~:text=conditions%20relating%20to%20the%20health,San%20Franciscans%20in%20serious%20risk) in the end of 2021. From the same source we also learn that SF consideres South of Market(SoMa), to be a area of problems, and while not directly a district in our data, the location is contained by the Southeren district, and looking at Fig. 2 we also find that Southeren indeed sees a similar uptick in drug realted offenses in between 2021 and 2022.


##  District-Level Map

So to better understand how the crime not only develops temporally but also spatially, Fig 3. visualize the same inherent data as Fig 2. but using the geographical data of the district of San Fransisco.

<iframe src="/assets/plotly/district_map.html" height="700px"></iframe>

From this map it is very apperent that during 2009 the Tenderloin was a significant hotspot for Drug realated crime, depsite its smaller size compared to neighboring districts. Likewise we can also see that while the Tenderloin is THE hotspot, the other two district of interest; Mission and Southeren, are neigbouring it.

This trend is maintained even in 2017, where the drug offenses in the Tenderloin is at its lowest, as we still find three of the neighbouring districts to have similar degrees of drug realted offenses, but generally it seems that drug offenses are spread more uniformly throughout the entire city.

Finally going through the years from 2017 up until 2024, you can somewhat consistently see the color of the Tenderloin darkening again, as drug related crime once again begins concetrating in and around the Tenderloin, maintaining its reputation as one of the most problematic districts in all of San Fransisco.



