# %%
import pandas as pd
import datetime as dt
from datetime import datetime, date,  timedelta
import sys
import fileinput
# to run python file
from subprocess import call

'''
Firstly, I want to modify automatically my configuration.yaml file and then run main program python.py script.
This script will help to modify existing date value with current date value get from 'datelist for loop' in python.yaml configuration file and
then run the main python program script for each modfied date configuration.
'''

# %%
# already existing date value in yaml file
previous_date = '2018-02-28'
# starting date that need to be run
start_date = '2018-03-01'
# how many number of dates need to run from start date
nb_date = 20
# frequency of date should be 7 days
frequency = '7D'
# list of all dates including start date with 7 days freq
datelist =  pd.date_range(dt.datetime.strptime(start_date, '%Y-%m-%d'), periods=nb_date, freq ='7D').strftime('%Y-%m-%d').tolist()
datelist

# %%
# function to modify yaml config file
def modifyYaml(previous_date, new_date):
    print(previous_date, new_date)
    # loop to check yaml file line by line
    for line in fileinput.input("/path/to/yaml/configuration/file/configuration.yaml", inplace=True):
        
        # This will replace string "previous_date" with "new_date" in each line
        # it is basically a string value replacer with new given value
        # you can modify here by your own needed value to change
        line = line.replace(previous_date , new_date)
        
        # write() method of sys module redirects the .stdout is redirected to the file
        sys.stdout.write(line)

# %%
# loop to run python script for all dates in datelist
for date in datelist:
    # modify yaml file date value
    modifyYaml(previous_date, date)
    # update new_date as previous_date for next iteration
    previous_date = date
    # call python script to run for new yaml configuration
    call(['python3', '/path/to/main/python/program/file/python.py'])
