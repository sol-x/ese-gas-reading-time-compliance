# Enclosed Space Entry Gas Reading Time Compliance

The crew members working on the vessel are required to enter one enclosed space. According to the safety requirements, a permit to work (PTW) called "Enclosed Space Entry" (ESE) must be submitted by a crew member and get it approved by the captain of the vessel. After the permit gets approved, the crew members can enter the space within the time duration specified on the permit. 

There are several dangers and hazards associated with enclosed spaces, like:
- Lack of oxygen
- toxic vapours
- Leakage of hazardous materials
so it is very important to measure the level of some gases, like Oxygen, Carbon monoxide and Hydrogen sulfide from time to time. If any of the gases has the level mismatched with its required threshold, the PTW has to be terminated immediately and no one is allowed to enter the space.

There are two types of gas readings:
1. Periodical gas reading: The crew member take the required readings of gases and record the data. No one will enter the enclosed space. The `gas reading time` will be recorded into the system. (Of course the gas reader and the readings of each gas should also be recorded, but these info are not required for this test)
2. Entrant gas reading: Before a crew member enter the enclosed space, he must do the gas reading and record the data. If the readings indicate the space is safe, he will enter the space. When he finishes his work in the space, he will get out and submit the time he leaves the space (No gas reading when he leaves the space). `gas reading time`, `entry time`, `exit time` will be recorded. (Of course the entrant and the readings of each gas should also be recorded, but these info are not required for this test)

With in the validity time of the PTW, there can be multiple periodical gas readings and multiple entrant gas readings. The gas reading time compliance requires that for each entrant, if he stays more than 30 minutes, there must be at least one gas reading by the end of the 30 minutes, regardless the gas reading is periodical or for entry. For example, it a crew member does gas reading and enter the space at 08:00 and he leaves at 08:50. There is a periodical gas reading at 08:25, it is compliant.

## Requirement

The data will be given as two csv file, named `periodical_gas_reading.csv` and `entrant_gas_reading.csv`. The format for  `periodical_gas_reading.csv` will look like:
```
gas reading time
2021-12-06T11:00:00.000Z
2021-12-06T11:30:00.000Z
2021-12-06T12:30:00.000Z
```

The format for  `entrant_gas_reading.csv` will look like:
```
gas reading time,entry time,exit time
2021-12-06T12:00:00.000Z,2021-12-06T12:00:00.000Z,2021-12-06T12:50:00.000Z
```

The column `gas reading time` contains the timestamp of the gas reading. For entrant gas reading, there will be`entry time` and `exit time` columns which indicates the timestamps of crew member entering and exiting the space.

Write a python program which can:
1. Read the CSV files
2. Check if the the gas reading time is compliant. Print "Compliant" if it is, print "Not Compliant" if it is not.

> The timestamps in the csv files are in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.

## Bonus 

Write unit test with any testing framework you prefer.