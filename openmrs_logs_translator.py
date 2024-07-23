import pandas as pd
from datetime import datetime

# Read the log file
with open('openmrs.log', 'r', encoding="utf8") as file:
    lines = file.readlines()

# Separate INFO lines
# info_lines = [line.strip() for line in lines if line.startswith('INFO')]

# Separate ERROR lines, excluding specific patterns
error_lines = [line.strip() for line in lines if line.startswith('ERROR') and not (
    'ERROR - OpenElis' in line or 'ERROR - TimerSchedulerTask' in line or 'ERROR - ModuleFactory' in line or 'ERROR - BaseRestController' in line or 'ERROR - Bahmni' in line)]

# Create dataframes
# df_info = pd.DataFrame(info_lines, columns=['Log'])
df_error = pd.DataFrame(error_lines, columns=['Log'])
# Get the current date in the desired format
current_date = datetime.now().strftime("%d_%b_%Y")
# Create a new Excel writer object and save the dataframes to different sheets
with pd.ExcelWriter(f'OpenmrsErrorLogs{current_date}.xlsx', engine='openpyxl') as writer:
    # df_info.to_excel(writer, sheet_name='INFO', index=False)
    df_error.to_excel(writer, sheet_name='ERROR', index=False)

print("Logs have been parsed and saved to logs.xlsx")
