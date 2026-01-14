
# importing necessary libraries
import numpy as np
import pandas as pd
import os
import glob

# folder path where the csv files are stored
path = r"C:\Users\farih\Project\HIT 137 Assignment 2 codes\temperatures"

# finding the list of all csv file in that 'temperatures' folder
csv_files = glob.glob(path + "/*.csv")

# creating an empty list for storing all the temperature data from each csv file
all_temperatures = []

# looping through each csv files and adding them to the created list
for filename in csv_files:
    df = pd.read_csv(filename, index_col=None)
    all_temperatures.append(df)

# merging all the individual csv files into one dataframe
final_df = pd.concat(all_temperatures)

# printing the final dataframe
print(final_df)



#......processing part start......

# creating list of all months 
months_name= ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

# converting columns into numeric if in text
for data_column in months_name:
    final_df[data_column] = pd.to_numeric(final_df[data_column], errors='coerce')

#......processing part ends.......



#......SEASONAL AVERAGE part starts.......

# grouping months into season
summer = ['December', 'January', 'February']
autumn = ['March', 'April', 'May']
winter = ['June', 'July', 'August']
spring = ['September', 'October', 'November']

# calculating average temperature for each season as per their station
final_df['summer_average'] = final_df[summer].mean(axis=1)
final_df['autumn_average'] = final_df[autumn].mean(axis=1)
final_df['winter_average'] = final_df[winter].mean(axis=1)
final_df['spring_average'] = final_df[spring].mean(axis=1)

# calculating average temperature fpr each season across all the stations
final_summer_average = final_df['summer_average'].mean()
final_autumn_average = final_df['autumn_average'].mean()
final_winter_average = final_df['winter_average'].mean()
final_spring_average = final_df['spring_average'].mean()

# displaying the final results
seasonal_average_temp = (f"Summer: {final_summer_average:.1f}°C\n"
                         f"Autumn: {final_autumn_average:.1f}°C\n"
                         f"Winter: {final_winter_average:.1f}°C\n"
                         f"Spring: {final_spring_average:.1f}°C\n")

# saving results to the 'average_temp.txt' file
seasonal_average_temp_file = open('average_temp.txt', 'w')
seasonal_average_temp_file.write(seasonal_average_temp)
seasonal_average_temp_file.close()

# checking if the file has been saved or not
if os.path.exists('average_temp.txt'):
    print("average temperature has been saved in the text file")
else:
    print("average temperature not saved")

#......SEASONAL AVERAGE part ends.......


# ---------------------------------------------------------------------------------------------------------



#-----------------------=--------------- SOLVED BY TANJIMA PARVIN TANNA -------------------------------------------------------------

#......TEMPERATURE RANGE part starts.......

# Finding the largest temperature range by subtracting the highest and lowest temperature
final_df['maximum_temperature'] = final_df[months_name].max(axis=1)
final_df['minimum_temperature'] = final_df[months_name].min(axis=1)
final_df['largest_temperature_range'] = final_df['maximum_temperature'] - final_df['minimum_temperature']

# Finding the highest temperature value
highest_temperature = final_df['largest_temperature_range'].max()

# handling ties
multiple_station_tie = final_df[final_df['largest_temperature_range'] == highest_temperature]

#Looping through the row and column of the stations that tied and display the largest temperature range 
for index, row in multiple_station_tie.iterrows():
    temperature_range = (f"Station {row['STATION_NAME']}: Range {row['largest_temperature_range']:.1f}°C "
                         f"(Max: {row['maximum_temperature']:.1f}°C, Min: {row['minimum_temperature']:.1f}°C)\n")

# saving results to the 'largest_temp_range_station.txt' file
temperature_range_file = open('largest_temp_range_station.txt', 'w')
temperature_range_file.write(temperature_range)
temperature_range_file.close()

# checking if the file has been saved or not
if os.path.exists('largest_temp_range_station.txt'):
    print("temperature range has been saved in the text file")
else:
    print("temperature range not saved")

#......TEMPERATURE RANGE part ends.......



#......TEMPERATURE STABILITY  part starts.......

# Calculating standard deviatio for each station 
final_df['standard_deviation'] = final_df[months_name].std(axis=1)

# finding the smallest and largest standard deviation
smallest_standard_deviation = final_df['standard_deviation'].min()
largest_standard_deviation = final_df['standard_deviation'].max()

# handling ties
stable_temperature_stations = final_df[final_df['standard_deviation'] == smallest_standard_deviation ]
variable_temperature_stations = final_df[final_df['standard_deviation'] == largest_standard_deviation]

# displaying the results
for index, row in stable_temperature_stations.iterrows():
    most_stable_temperature_station = (f"Most Stable: Station {row['STATION_NAME']}: StdDev {row['standard_deviation']:.1f}°C\n")

for index, row in variable_temperature_stations.iterrows():
    most_variable_temperature_station = (f"Most Variable: Station {row['STATION_NAME']}: StdDev {row['standard_deviation']:.1f}°C\n")

# saving results to the 'temperature_stability_stations.txt' file
temperature_stability_stations_file = open('temperature_stability_stations.txt', 'w')
temperature_stability_stations_file.write(most_stable_temperature_station)
temperature_stability_stations_file.write(most_variable_temperature_station)
temperature_stability_stations_file.close()

# checking if the file has been saved or not
if os.path.exists('temperature_stability_stations.txt'):
    print("temperature stability has been saved in the text file")
else:
    print("temperature stability not saved")

#......TEMPERATURE STABILITY part ends.......

# -----------------------------------------------------
