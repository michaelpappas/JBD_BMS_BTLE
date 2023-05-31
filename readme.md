# JBD BMS BTLE Python Script
A Python script that pulls data from the JBD BMS commonly used for LiFePO4 batteries. The script borrows the data extraction and processing from [this repo](https://github.com/madmacks59/JBD-BMS-Bluetooth) but has been modified to add the data to a postgres database instead of sending it over MQTT. In my case I'm running my MQTT broker on the same Raspberry Pi so the MQTT is unecessary.


## Table of Contents
- [Installaion](#installation)
- [Project Structure](#project-structure)
- [Further Improvements](#further-improvements)

## Installation
Clone the repo:

```bash
git clone https://github.com/michaelpappas/JBD_BMS_BTLE.git
cd JBD_BMS_BTLE
```



To run the script you will need to create a CRONjon.

Example CRONjob
```bash
* * * * * sudo python3 [path_to_directory]/JBD_BMS_BTLE/jbdBMS_db.py -i 0 -n [bms bluetooth name]
# this script will run every minute forever
```

more info about setting up CRONjobs can be found [here](https://crontab.guru/).

## Project Structure

```
\                           # project directory
 |--models.py               # script to create battery table in db and row configuration
 |--jbdBMS_db.py            # main BTLE connection and processing script
```

## Further Improvements

1. Improve stability
2. Finish readme










