
# Openmrs Logs Converter

## Introduction
This Python script parses through log data and outputs onto an excel file all the lines with Errors.

## Requirements
- Python 3.x
- datetime

## Installation
Clone this repository and navigate into the project directory:
```bash
# Clone the script
git clone https://github.com/MSF-OCB/openmrs_logs_translator.git
cd openmrs_logs_translator

# Paste your logs into the openmrs.logs file

# Run the script to generate the excel file witht he errors
py openmrs_logs_translator.py
```
## You will get an excel output file with the errors in each row.