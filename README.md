# Introduction

This module imports data taken from the Weather Underground API. The subsequent data is parsed and simple weather information is displayed. The module runs from the command line and outputs all results there.

## Requirements

All required files are listed in the *requirements.txt* file. To run, type "pip install -r requirements.txt" in your OS command line. There are no other files needed to install to make the program work, simply copy all of the contents into a directory and type `python weather.py` at the command line prompt.

## Files

Included in this module are: README.md; requirements.txt; weather.py; alerts.py; astronomy.py; current_conditions.py; current_hurricane.py; ten_day_forecast.py; weather_test.py; and web_requester.py.

weather.py is the main file, and is the only file that should be run. All of the remaining .py files are submodules that run when main is run, except for weather_test.py (this file is strictly for debugging only).
