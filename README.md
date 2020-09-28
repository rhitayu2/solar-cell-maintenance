# Automatic Solar Cell Maintenance
Python script to read the input from a solar cell and compare with the input coming from Light Dependent Resistors and report in case of any discrepancy. 



## Requirements and Set Up
* Used a Raspberry Pi 3 Model B+ for the project.
* Used Analog-to-Digital converter to read the signal from the solar cell.
* Connected the LDR to the RPI and used a time interval to compute the time intensity.
* Sign Up for a ThingSpeak account and require keys to POST messages to dashboard.
* Use any notification app and configure with ThingSpeak to send notifications in case of discrepancy.

## Running
* Simultaneously run`solar_cell.py` and `thingspeak.py`.
* `solar_cell.py` stores the result in a text file, regarding the solar cell input and configure 
  the relationship between LDR reading and solar cell reading based on requirements.
